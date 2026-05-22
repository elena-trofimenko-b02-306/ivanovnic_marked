import os
import sqlite3
import uuid
from datetime import datetime
from functools import wraps

from flask import (Flask, abort, flash, g, redirect, render_template,
                   request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me-in-production-" + str(uuid.uuid4()))

UPLOAD_FOLDER = os.path.join(app.root_path, "static", "uploads")
ALLOWED_VIDEO_EXT = {"mp4", "webm", "mov", "avi", "mkv"}
ALLOWED_THUMB_EXT = {"jpg", "jpeg", "png", "webp"}
MAX_CONTENT_LENGTH = 2 * 1024 * 1024 * 1024  # 2 GB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

DATABASE = os.path.join(app.root_path, "site.db")

OWNER_USERNAME = "sergey_barinov"


# ---------------------------------------------------------------------------
# DB helpers
# ---------------------------------------------------------------------------

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
    return db


@app.teardown_appcontext
def close_db(exc):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            username  TEXT    NOT NULL UNIQUE,
            email     TEXT    NOT NULL UNIQUE,
            password  TEXT    NOT NULL,
            is_owner  INTEGER NOT NULL DEFAULT 0,
            created_at TEXT   NOT NULL
        );

        CREATE TABLE IF NOT EXISTS videos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT    NOT NULL,
            description TEXT,
            filename    TEXT    NOT NULL,
            thumbnail   TEXT,
            created_at  TEXT    NOT NULL
        );

        CREATE TABLE IF NOT EXISTS comments (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            video_id   INTEGER NOT NULL REFERENCES videos(id) ON DELETE CASCADE,
            user_id    INTEGER NOT NULL REFERENCES users(id)  ON DELETE CASCADE,
            body       TEXT    NOT NULL,
            created_at TEXT    NOT NULL
        );
    """)
    db.commit()
    db.close()


# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            flash("Войдите в аккаунт, чтобы продолжить.", "info")
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated


def owner_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get("is_owner") != 1:
            abort(403)
        return f(*args, **kwargs)
    return decorated


def current_user():
    if "user_id" not in session:
        return None
    db = get_db()
    return db.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()


app.jinja_env.globals["current_user"] = current_user


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def allowed_video(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_VIDEO_EXT


def allowed_thumb(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_THUMB_EXT


def save_file(file_obj, subfolder):
    ext = file_obj.filename.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    dest_dir = os.path.join(app.config["UPLOAD_FOLDER"], subfolder)
    os.makedirs(dest_dir, exist_ok=True)
    file_obj.save(os.path.join(dest_dir, unique_name))
    return f"{subfolder}/{unique_name}"


# ---------------------------------------------------------------------------
# Routes – public
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    db = get_db()
    videos = db.execute(
        "SELECT * FROM videos ORDER BY created_at DESC"
    ).fetchall()
    return render_template("index.html", videos=videos)


@app.route("/video/<int:video_id>")
def video(video_id):
    db = get_db()
    v = db.execute("SELECT * FROM videos WHERE id = ?", (video_id,)).fetchone()
    if v is None:
        abort(404)
    comments = db.execute(
        """SELECT c.*, u.username FROM comments c
           JOIN users u ON u.id = c.user_id
           WHERE c.video_id = ?
           ORDER BY c.created_at ASC""",
        (video_id,),
    ).fetchall()
    return render_template("video.html", video=v, comments=comments)


# ---------------------------------------------------------------------------
# Routes – auth
# ---------------------------------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        confirm = request.form["confirm"]

        db = get_db()
        error = None

        if not username or not email or not password:
            error = "Заполните все поля."
        elif password != confirm:
            error = "Пароли не совпадают."
        elif len(password) < 6:
            error = "Пароль должен быть не менее 6 символов."
        elif db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone():
            error = "Это имя пользователя уже занято."
        elif db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
            error = "Этот e-mail уже зарегистрирован."

        if error:
            flash(error, "error")
        else:
            db.execute(
                "INSERT INTO users (username, email, password, is_owner, created_at) VALUES (?,?,?,0,?)",
                (username, email, generate_password_hash(password), datetime.utcnow().isoformat()),
            )
            db.commit()
            flash("Регистрация прошла успешно. Войдите в аккаунт.", "success")
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("index"))
    if request.method == "POST":
        identifier = request.form["identifier"].strip()
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?",
            (identifier, identifier.lower()),
        ).fetchone()
        if user is None or not check_password_hash(user["password"], password):
            flash("Неверный логин или пароль.", "error")
        else:
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["is_owner"] = user["is_owner"]
            next_url = request.args.get("next")
            return redirect(next_url or url_for("index"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Routes – comments
# ---------------------------------------------------------------------------

@app.route("/video/<int:video_id>/comment", methods=["POST"])
@login_required
def add_comment(video_id):
    db = get_db()
    if db.execute("SELECT id FROM videos WHERE id = ?", (video_id,)).fetchone() is None:
        abort(404)
    body = request.form.get("body", "").strip()
    if not body:
        flash("Комментарий не может быть пустым.", "error")
        return redirect(url_for("video", video_id=video_id))
    db.execute(
        "INSERT INTO comments (video_id, user_id, body, created_at) VALUES (?,?,?,?)",
        (video_id, session["user_id"], body, datetime.utcnow().isoformat()),
    )
    db.commit()
    return redirect(url_for("video", video_id=video_id) + "#comments")


# ---------------------------------------------------------------------------
# Routes – owner (upload / delete)
# ---------------------------------------------------------------------------

@app.route("/upload", methods=["GET", "POST"])
@login_required
@owner_required
def upload():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        video_file = request.files.get("video")
        thumb_file = request.files.get("thumbnail")

        if not title:
            flash("Укажите название видео.", "error")
            return render_template("upload.html")
        if not video_file or not allowed_video(video_file.filename):
            flash("Прикрепите видеофайл (mp4, webm, mov, avi, mkv).", "error")
            return render_template("upload.html")

        video_path = save_file(video_file, "videos")
        thumb_path = None
        if thumb_file and thumb_file.filename and allowed_thumb(thumb_file.filename):
            thumb_path = save_file(thumb_file, "thumbs")

        db = get_db()
        db.execute(
            "INSERT INTO videos (title, description, filename, thumbnail, created_at) VALUES (?,?,?,?,?)",
            (title, description, video_path, thumb_path, datetime.utcnow().isoformat()),
        )
        db.commit()
        flash("Видео успешно загружено!", "success")
        return redirect(url_for("index"))

    return render_template("upload.html")


@app.route("/video/<int:video_id>/delete", methods=["POST"])
@login_required
@owner_required
def delete_video(video_id):
    db = get_db()
    v = db.execute("SELECT * FROM videos WHERE id = ?", (video_id,)).fetchone()
    if v is None:
        abort(404)
    for sub in ("filename", "thumbnail"):
        if v[sub]:
            path = os.path.join(app.config["UPLOAD_FOLDER"], v[sub])
            if os.path.exists(path):
                os.remove(path)
    db.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    db.commit()
    flash("Видео удалено.", "info")
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Bootstrap owner account on first run
# ---------------------------------------------------------------------------

def ensure_owner():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    existing = db.execute(
        "SELECT id FROM users WHERE username = ?", (OWNER_USERNAME,)
    ).fetchone()
    if not existing:
        owner_password = os.environ.get("OWNER_PASSWORD", "barinov2024")
        db.execute(
            "INSERT INTO users (username, email, password, is_owner, created_at) VALUES (?,?,?,1,?)",
            (
                OWNER_USERNAME,
                "sergey@barinov.ru",
                generate_password_hash(owner_password),
                datetime.utcnow().isoformat(),
            ),
        )
        db.commit()
        print(f"Owner account created: {OWNER_USERNAME} / {owner_password}")
    db.close()


if __name__ == "__main__":
    init_db()
    ensure_owner()
    app.run(debug=True, host="0.0.0.0", port=5000)
