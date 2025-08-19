<block id='B1'>
## Г.Е. Иванов

## ЛЕКЦИИ ПО

# МАТЕМАТИЧЕСКОМУ 

## АНАЛИЗУ

Часть 2
</block>
<block id='B2'>
## Оглавление

Предисловие ..... 4
Глава 13. ЭКСТРЕМУМЫ ФУНКЦИЙ НЕСКОЛЬКИХ ПЕРЕМЕННЫХ ..... 5
§ 1. Безусловный экстремум ..... 5
§ 2. Условный экстремум ..... 9
Глава 14. КРАТНЫЙ ИНТЕГРАЛ ..... 18
§ 1. Кратный интеграл Римана. Ограниченность интегри- руемой функции ..... 18
§ 2. Свойства кратного интеграла ..... 20
§ 3. Сведение кратного интеграла к повторному ..... 26
§ 4. Геометрический смысл модуля якобиана ..... 30
§ 5. Замена переменных в кратном интеграле ..... 39
§ 6. Геометрический смысл знака якобиана отображения ..... 45
§ 7. Формула Грина ..... 49
Глава 15. ПОВЕРХНОСТНЫЕ ИНТЕГРАЛЫ ..... 55
§ 1. Определения поверхностей ..... 55
§ 2. Поверхностный интеграл первого рода ..... 62
§ 3. Поверхностный интеграл второго рода ..... 66
§ 4. Оператор Гамильтона ..... 70
§ 5. Формула Остроградского-Гаусса ..... 73
§ 6. Формула Стокса ..... 80
§ 7. Условия независимости криволинейного интеграла от пути интегрирования ..... 84
§ 8. Дифференциальные формы и общая теорема Стокса ..... 89
Глава 16. РЯДЫ ФУРЬЕ ..... 94
§ 1. Определение ряда Фурье по ортогональной системе ..... 94
§ 2. Теорема Римана об осцилляции ..... 100
§ 3. Сходимость ряда Фурье в точке ..... 103
§ 4. Почленное дифференцирование и интегрирование ряда Фурье ..... 110
§ 5. Порядок убывания коэффициентов Фурье и остатка ряда Фурье ..... 112
§ 6. Суммирование ряда Фурье методом средних арифметических ..... 114
§ 7. Приближения непрерывных функций многочленами ..... 118
§ 8. Пространства $C[a, b], R L_{1}[a, b], R L_{2}[a, b]$ ..... 120
§ 9. Полные системы ..... 125
§ 10. Сходимость ряда Фурье в смысле евклидовой нормы ..... 130
§ 11. Неравенство Бесселя, равенство Парсеваля и равно- мерная сходимость ряда Фурье ..... 136
§ 12. Замкнутые системы ..... 138
Глава 17. ИНТЕГРАЛЫ, ЗАВИСЯЩИЕ OT ПАРАМЕТРА ..... 142
§ 1. Собственные интегралы, зависящие от параметра ..... 142
§ 2. Равномерная сходимость несобственных интегралов ..... 145
§ 3. Несобственные интегралы, зависящие от параметра ..... 149
§ 4. Эйлеровы интегралы ..... 154
§ 5. Интеграл Фурье ..... 155
§ 6. Преобразование Фурье ..... 161
Глава 18. ОБОБЩЕННЫЕ ФУНКЦИИ ..... 171
§ 1. Пространство $\mathcal{D}$ основных (пробных) функций ..... 171
§ 2. Пространство $\mathcal{D}^{\prime}$ обобщенных функций ..... 172
§ 3. Сходимость в пространстве $\mathcal{D}^{\prime}$ ..... 176
§ 4. Произведение обобщенной функции на бесконеч- но дифференцируемую функцию. Производная обобщенной функции ..... 177
§ 5. Пространства Шварца $S$ и $S^{\prime}$ ..... 180
§ 6. Преобразование Фурье обобщенных функций ..... 183
Предметный указатель ..... 189
</block>
<block id='B3'>
## Предисловие

Настоящее учебное пособие написано на основе лекций, читаемых автором студентам второго курса Московского физико-технического института (государственного университета).

Содержание материала соответствует программе кафедры высшей математики МФТИ (ГУ).

Автор выражает искреннюю признательность коллегам и студентам, высказавшим ценные замечания и предложения, а также обнаружившим опечатки в лекциях.
</block>
<block id='C13'>
# ЭКСТРЕМУМЫ ФУНКЦИЙ НЕСКОЛЬКИХ ПЕРЕМЕННЫХ 
</block>
<block id='C13.1'>
## § 1. Безусловный экстремум
</block>
<block id='D13.1.1'>
Определение. Пусть на множестве $X \subset \mathbb{R}^{n}$ задана функция $f: X \rightarrow \mathbb{R}$. Точка $x^{0} \in X$ называется точкой строгого локального минимума (максимума) функции $f$ на множестве $X$, если

$$
\exists \delta>0: \forall x \in \stackrel{o}{U}_{\delta}\left(x^{0}\right) \bigcap X \hookrightarrow f\left(x^{0}\right)<(>) f(x) .
$$

Если здесь строгое неравенство заменить нестрогим, то получится определение нестрогого локального минимума (максимума). Точки минимума и максимума называются точками экстремума.
</block>
<block id='D13.1.2'>
Определение. Пусть $x^{0}$ - точка локального экстремума функции $f$ на множестве $X$. Тогда если $x^{0} \in \operatorname{int} X$, то $x^{0}$ называется точкой безусловного локального экстремума функции $f$; если $x^{0} \in \partial X$, то $x^{0}$ называется точкой условного локального экстремума функции $f$.
</block>
<block id='L13.1.1'>
Лемма 1. $x^{0}$ - точка строгого безусловного локального минимума функции $f$ тогда и только тогда, когда

$$
\exists \delta>0: \forall x \in \stackrel{o}{U}_{\delta}\left(x^{0}\right) \hookrightarrow f\left(x^{0}\right)<f(x) .
$$

Доказательство. Пусть $x^{0}$ - точка строго безусловного локального минимума функции $f$. Тогда $\exists \delta_{1}>0: \forall x \in \stackrel{o}{U}_{\delta_{1}}\left(x^{0}\right) \cap X \hookrightarrow$ $\hookrightarrow f\left(x^{0}\right)<f(x)$. Поскольку $x^{0} \in \operatorname{int} X$, то $\exists \delta_{2}>0: U_{\delta_{2}}\left(x^{0}\right) \subset X$. Определим $\delta=\min \left\{\delta_{1}, \delta_{2}\right\}$. Тогда $\forall x \in U_{\delta}\left(x^{0}\right) \hookrightarrow f\left(x^{0}\right)<f(x)$. Обратное утверждение очевидно.
</block>
<block id='T13.1.1'>
Теорема 1. (Необходимое условие экстремума.) Пусть функция $f(x)$ определена в окрестности точки $x^{0} \in \mathbb{R}^{n}$ и дифференцируема

в точке $x^{0}$. Если $x^{0}$ - точка безусловного локального экстремума функции $f$, то $\operatorname{grad} f\left(x^{0}\right)=\overline{0}$.

Доказательство. Поскольку компоненты вектора grad $f\left(x^{0}\right)=$
$=\overline{0}$ равны частным производным $\frac{\partial f}{\partial x_{i}}\left(x^{0}\right)$, то достаточно доказать, что $\frac{\partial f}{\partial x_{i}}\left(x^{0}\right)=0 \quad \forall i \in\{1, \ldots, n\}$. Зафиксируем произвольное $i \in$
$\in\{1, \ldots, n\}$ и рассмотрим функцию одной переменной $\varphi\left(x_{i}\right)=$
$=f\left(x_{1}^{0}, \ldots, x_{i-1}^{0}, x_{i}, x_{i+1}^{0}, \ldots, x_{n}^{0}\right)$. Поскольку $x^{0}$ - точка локального экстремума функции $f$, то $x_{i}^{0}$ - точка локального экстремума функции $\varphi\left(x_{i}\right)$. В силу теоремы Ферма $\varphi^{\prime}\left(x_{i}^{0}\right)=0$. Следовательно, $\frac{\partial f}{\partial x_{i}}\left(x^{0}\right)=\varphi^{\prime}\left(x_{i}^{0}\right)=0$.
</block>
<block id='D13.1.3'>
Определение. Если $\operatorname{grad} f\left(x^{0}\right)=\overline{0}$, то точка $x^{0}$ называется cmaционарной точкой функции $f$.
</block>
<block id='R13.1.1'>
Из теоремы 1 следует, что точки экстремума функции являются ее стационарными точками. Обратное неверно. Например, для функции одной переменной $f(x)=x^{3}$ точка $x_{0}=0$ является стационарной точкой, но не является точкой экстремума.
</block>
<block id='TX13.1.1'>
Пусть функция $f(x)$ дважды непрерывно дифференцируема в окрестности точки $x^{0} \in \mathbb{R}^{n}$ (т. е. частные производные функции $f$ до второго порядка включительно непрерывны в окрестности точки $x^{0}$ ). Тогда справедлива следующая формула Тейлора (глава $6, \S 11$, теорема 2):

$$
f(x)-f\left(x^{0}\right)=d f\left(x^{0}\right)+\frac{1}{2} d^{2} f\left(x^{0}\right)+o\left(|\Delta x|^{2}\right) \quad \text { при } \quad \Delta x \rightarrow \overline{0} .
$
</block>
<block id='TX13.2.2'>
Если система из $m$ уравнений $g(x)=\overline{0}$ разрешима относительно $m$ переменных, т. е. вектор $x \in \mathbb{R}^{n}$ можно разбить на два вектора $y \in \mathbb{R}^{m}$ и $z \in \mathbb{R}^{n-m}: x=\binom{y}{z}$ таких, что

$
g(y, z)=\overline{0} \quad \Longleftrightarrow \quad y=\varphi(z),
$

тогда задача (1) отыскания условного экстремума сводится к задаче отыскания безусловного экстремума функции $f(\varphi(z), z)$.

Этот метод называется прямым методом, или методом разрешения ограничений.
</block>
<block id='E13.2.1'>
Пример 1. Найти локальные экстремумы функции $f(x, y, z)=$ $=-x^{3}-x^{2}+4 x y+2 x z-4 y^{2}+2 y z-z^{2}$ при условии $x+y-z=0$.

Решение. Из условия $x+y-z=0$ можно выразить $z=x+y$, поэтому исходная задача сводится к задаче отыскания безусловных локальных экстремумов функции $F(x, y)=f(x, y, x+y)=-x^{3}+$
$+6 x y-3 y^{2}$. Найдем стационарные точки функции $F$ :

$
\left\{\begin{array} { l } 
{ F _ { x } ^ { \prime } = 0 } \\
{ F _ { y } ^ { \prime } = 0 }
\end{array} \Leftrightarrow \left\{\begin{array} { l } 
{ - 3 x ^ { 2 } + 6 y = 0 } \\
{ 6 x - 6 y = 0 }
\end{array} \Leftrightarrow \left\{\begin{array}{l}
x=y,\\
x^{2}=2 x.
\end{array}\right.\right.\right.
$

Функция $F$ имеет две стационарные точки: $(0,0)$ и $(2,2)$.
Исследуем знакоопределенность второго дифференциала в стационарных точках.

Поскольку $F^{\prime \prime}(x, y)=\left(\begin{array}{cc}-6 x & 6 \\ 6 & -6\end{array}\right)$, то $F^{\prime \prime}(0,0)=\left(\begin{array}{cc}0 & 6 \\ 6 & -6\end{array}\right)$, $d^{2} F(0,0)=12 d x d y-6(d y)^{2}$.

При $\binom{d x}{d y}=\binom{0}{1}$ имеем $d^{2} F(0,0)=-6<0$, а при $\binom{d x}{d y}=\binom{1}{1}$ получаем $d^{2} F(0,0)=12-6=6>0$. Следовательно, квадратичная форма $d^{2} F(0,0)$ знаконеопределена, и в точке ( 0,0 ) нет локального экстремума.

Матрица $F^{\prime \prime}(2,2)=\left(\begin{array}{cc}-12 & 6 \\ 6 & -6\end{array}\right)$ отрицательно определена, так как матрица $-F^{\prime \prime}(2,2)=\left(\begin{array}{cc}12 & -6 \\ -6 & 6\end{array}\right)$ положительно определена, что проверяется по критерию Сильвестра: $\Delta_{1}=12>0, \Delta_{2}=12 \cdot 6-$
$-6^{2}>0$. Поэтому в точке $\left(x_{0}, y_{0}\right)=(2,2)$ функция $F$ достигает

локального минимума. Следовательно, в точке $\left(x_{0}, y_{0}, z_{0}\right)=(2,2,4)$ функция $f(x, y, z)$ достигает локального минимума, равного $-x_{0}^{3}+$
$+6 x_{0} y_{0}-3 y_{0}^{2}=4$.
</block>
<block id='TX13.2.3'>
Если в задаче на условный экстремум (1) не удается разрешить ограничения, явно выразив одни переменные как достаточно простые функции других переменных, то следует использовать метод множителей Лагранжа.
</block>
<block id='D13.2.1'>
Определение. Функи,ией Лагранжа для задачи (1) называется функция

$
L(x, \lambda)=f(x)+\lambda^{T} g(x)=f(x)+\lambda_{1} g_{1}(x)+\cdots+\lambda_{m} g_{m}(x),
$

где вектор $\lambda=\left(\begin{array}{c}\lambda_{1} \\\cdots \\\lambda_{m}\end{array}\right)$ называется вектором множителей Лаграчœа.
</block>
<block id='T13.2.1'>
Теорема 1. (Необходимые условия экстремума.) Пусть $x^{0}-$ точка локального экстремума в задаче (1). Пусть функция $f(x)$ и вектор-функция $g(x)$ непрерывно дифференцируемы в окрестности точки $x^{0}$. Пусть векторы $\operatorname{grad} g_{1}\left(x^{0}\right), \cdots, \operatorname{grad} g_{m}\left(x^{0}\right)$ линейно независимы. Тогда существует вектор множителей Лагранжа $\lambda^{0} \in$
$\in \mathbb{R}^{m}$ такой, что точка $\binom{x^{0}}{\lambda^{0}}$ является стационарной точкой функции Лагранжа.
</block>
<block id='D13.2.2'>
Определение. Пусть вектор-функция $g(x)$ дифференцируема в точке $x^{0}$. Тогда касательным подпространством к множеству допустимых точек называется множество векторов

$
E_{\mathbf{K A C}}=\left\{d x \in \mathbb{R}^{n}: d g_{i}\left(x^{0}\right)=0 \quad \forall i \in\{1, \ldots, m\}\right\} .
$

Иными словами, касательное подпространство образуют векторы $d x$, удовлетворяющие продифференцированным уравнениям ограничений, т. е. системе уравнений

$
\left\{\begin{array}{ccc}
\frac{\partial g_{1}}{\partial x_{1}}\left(x^{0}\right) d x_{1} & +\cdots+ & \frac{\partial g_{1}}{\partial x_{n}}\left(x^{0}\right) d x_{n}=0, \\
\cdots & \cdots & \cdots \\
\frac{\partial g_{m}}{\partial x_{1}}\left(x^{0}\right) d x_{1} & +\cdots+ & \frac{\partial g_{m}}{\partial x_{n}}\left(x^{0}\right) d x_{n}=0 .
\end{array}\right.
$
</block>
<block id='T13.2.2'>
Теорема 2. (Достаточные условия экстремума.) Пусть $\binom{x^{0}}{\lambda^{0}}$ - стационарная точка функции Лагранжа. Пусть функция $f(x)$ и вектор-функция $g(x)$ дважды непрерывно дифференцируемы в окрестности точки $x^{0}$. Пусть векторы $\operatorname{grad} g_{1}\left(x^{0}\right), \cdots, \operatorname{grad} g_{m}\left(x^{0}\right)$ линейно независимы. И пусть $k(d x)=(d x)^{T} L_{x x}^{\prime \prime}\left(x^{0}, \lambda^{0}\right) d x-$ второй дифференциал функции Лагранжа по переменным $x$. Тогда

1) если квадратичная форма $k(d x)$ положительно определена на $E_{\mathbf{K A C}}$, т. е. $k(d x)>0 \quad \forall d x \in E_{\mathbf{K A C}} \backslash\{\overline{0}\}$, то $x^{0}$ - точка строгого локального минимума в задаче (1);
2) если квадратичная форма $k(d x)$ отрицательно определена на $E_{\text {KAC }}$, т. е. $k(d x)<0 \quad \forall d x \in E_{\text {KAC }} \backslash\{\overline{0}\}$, то $x^{0}$ - точка строгого локального максимума в задаче (1);
3) если квадратичная форма $k(d x)$ знаконеопределена на $E_{\text {кас }}$, т. е. существуют векторы $\xi_{1}, \xi_{2} \in E_{\text {кас }}: k\left(\xi_{1}\right)>0, k\left(\xi_{2}\right)<0$, то $x^{0}$ не является точкой локального экстремума в задаче (1);
4) если условия предыдущих пунктов не выполнены, то точка $x^{0}$ может быть точкой локального экстремума в задаче (1), а может и не быть ею.
</block>
<block id='P13.2.1'>
Доказательства теорем 1 и 2 будут приведены после рассмотрения примера.
</block>
<block id='C14'>
## КРАТНЫЙ ИНТЕГРАЛ
</block>
<block id='C14.1'>
## § 1. Кратный интеграл Римана. Ограниченность интегрируемой функции
</block>
<block id='D14.1.1'>
Определение. Диаметром множества $E \subset \mathbb{R}^{n}$ называется супремум расстояний между двумя элементами этого множества:

$
\operatorname{diam}(E)=\sup _{x \in E, y \in E}|x-y|
$
</block>
<block id='D13.1.4'>
Через $f_{x}^{\prime}\left(x^{0}\right)$ обозначим строку частных производных первого порядка или, что то же самое, координатную строку вектора градиента:

$$
f_{x}^{\prime}\left(x_{0}\right)=\left(\begin{array}{lll}
\frac{\partial f}{\partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial f}{\partial x_{n}}\left(x^{0}\right)
\end{array}\right),
$$

а через $f_{x x}^{\prime\prime}\left(x^{0}\right)$ - матрицу частных производных второго порядка:

$$
f_{x x}^{\prime\prime}\left(x^{0}\right)=\left(\begin{array}{ccc}
\frac{\partial^{2} f}{\partial x_{1} \partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial^{2} f}{\partial x_{n} \partial x_{1}}\left(x^{0}\right) \\
\cdots & \cdots & \cdots \\
\frac{\partial^{2} f}{\partial x_{1} \partial x_{n}}\left(x^{0}\right) & \cdots & \frac{\partial^{2} f}{\partial x_{n} \partial x_{n}}\left(x^{0}\right)
\end{array}\right)
$$

Поскольку для дважды непрерывно дифференцируемой функции $f$ частные производные второго порядка не зависят от порядка дифференцирования, то $f_{x x}^{\prime\prime}\left(x^{0}\right)$ - симметрическая матрица.
</block>
<block id='TX13.1.2'>
Полагая $d x=\Delta x=x-x^{0}=\left(\begin{array}{c}x_{1}-x_{1}^{0} \\
\ldots \\
x_{n}-x_{n}^{0}\end{array}\right), \quad \Delta f=f(x)-f\left(x^{0}\right)$, получаем равенства

$$
\begin{gather*}
d f\left(x^{0}\right)=\sum_{i=1}^{n} \frac{\partial f}{\partial x_{i}}\left(x^{0}\right) d x_{i}=f_{x}^{\prime}\left(x^{0}\right) d x \\
d^{2} f\left(x^{0}\right)=\sum_{i=1}^{n} \sum_{j=1}^{n} \frac{\partial^{2} f}{\partial x_{i} \partial x_{j}}\left(x^{0}\right) d x_{i} d x_{j}=(d x)^{T} f_{x x}^{\prime\prime}\left(x^{0}\right) d x \tag{1}
\end{gather*}
$$

Из формулы (1) следует, что второй дифференциал функции $f$ является квадратичной формой относительно вектора $d x$.
</block>
<block id='D13.1.5'>
Напомним, что квадратичная форма $k(x)=x^{T} M x$ называется

1) положительно определенной, если $k(x)>0 \quad \forall x \neq \overline{0}$;
2) отрицательно определенной, если $k(x)<0 \quad \forall x \neq \overline{0}$;
3) знаконеопределенной, если $\exists x_{1}, x_{2} \in \mathbb{R}^{n}: k\left(x_{1}\right)>0, k\left(x_{2}\right)<0$.
</block>
<block id='R13.1.2'>
Легко видеть, что квадратичная форма $k(x)=x^{T} M x$ отрицательно определена, если квадратичная форма $-k(x)=x^{T}(-M) x$ положительно определена. Для проверки положительной и отрицательной определенности квадратичной формы удобно использовать критерий Сильвестра. Доказательство того, что квадратичная форма знаконеопределена, проводят по определению.
</block>
<block id='L13.1.2'>
Лемма 2. Если квадратичная форма $k(x)$ положительно определена, то

$
\exists \lambda>0: \forall x \in \mathbb{R}^{n} \hookrightarrow k(x) \geq \lambda|x|^{2} .
$

Доказательство. Поскольку функция $k(x)=x^{T} M x$ непрерывна, а единичная сфера $S=\left\{x \in \mathbb{R}^{n}:|x|=1\right\}$ ограничена и замкнута, т. е. является компактом, то существует $\min _{x \in S} k(x)=\lambda$. Из положительной определенности квадратичной формы $k(x)$ следует, что $\lambda>0$. Из определения минимума получаем, что $\forall \widetilde{x} \in S \hookrightarrow k(\widetilde{x}) \geq \lambda$.

Если $x=\overline{0}$, то $k(x)=0$, и неравенство $k(x) \geq \lambda|x|^{2}$ выполняется.
Если $x \neq \overline{0}$, то $\widetilde{x}=\frac{x}{|x|} \in S$, следовательно, $k(\widetilde{x}) \geq \lambda, \quad k(x)=$
$=x^{T} M x=|x|^{2} \widetilde{x}^{T} M \widetilde{x}=|x|^{2} k(\widetilde{x}) \geq \lambda|x|^{2}$.
</block>
<block id='T13.1.2'>
Теорема 2. (Достаточные условия экстремума.) Пусть функция $f(x)$ дважды непрерывно дифференцируема в окрестности точки $x^{0}$ и пусть $x^{0}$ - стационарная точка функции $f$. Тогда

1) если квадратичная форма $d^{2} f\left(x^{0}\right)$ положительно определена, то $x^{0}$ - точка строгого безусловного локального минимума функции $f$;
2) если квадратичная форма $d^{2} f\left(x^{0}\right)$ отрицательно определена, то $x^{0}$ - точка строгого безусловного локального максимума функции $f$;
3) если квадратичная форма $d^{2} f\left(x^{0}\right)$ знаконеопределена, то $x^{0}$ не является точкой безусловного локального экстремума функции $f$;
4) если квадратичная форма $d^{2} f\left(x^{0}\right)$ не является ни положительно, ни отрицательно определенной и не является знаконеопределенной, то $x^{0}$ может быть точкой локального экстремума, а может и не быть.

Доказательство. Поскольку $x^{0}$ - стационарная точка функции $f$, то $d f\left(x^{0}\right)=0$, следовательно,

$
\begin{equation*}
\Delta f=\frac{1}{2} d^{2} f\left(x^{0}\right)+o\left(|\Delta x|^{2}\right) \quad \text { при } \quad \Delta x \rightarrow \overline{0} . \tag{2}
\end{equation*}
$

1) Пусть квадратичная форма $d^{2} f\left(x^{0}\right)$ положительно определена. В силу леммы $2 \quad \exists \lambda>0: \forall \Delta x \in \mathbb{R}^{n} \hookrightarrow d^{2} f\left(x^{0}\right) \geq \lambda|\Delta x|^{2}$. Отсюда и из формулы Тейлора (2) следует, что $\Delta f \geq \frac{\lambda}{2}|\Delta x|^{2}+o\left(|\Delta x|^{2}\right)$ при $\Delta x \rightarrow \overline{0}$. По определению о-малого $\lim _{\Delta x \rightarrow \overline{0}} \frac{o\left(|\Delta x|^{2}\right)}{|\Delta x|^{2}}=0$, поэтому

$
\lim _{\Delta x \rightarrow \overline{0}} \frac{\frac{\lambda}{2}|\Delta x|^{2}+o\left(|\Delta x|^{2}\right)}{|\Delta x|^{2}}=\frac{\lambda}{2}>0 .
$

Следовательно,

$
\exists \delta>0: \forall \Delta x \in U_{\delta}(\overline{0}) \hookrightarrow \frac{\lambda}{2}|\Delta x|^{2}+o\left(|\Delta x|^{2}\right)>0,
$

поэтому $\forall x \in U_{\delta}\left(x^{0}\right) \hookrightarrow f(x)-f\left(x^{0}\right)=\Delta f \geq \frac{\lambda}{2}|\Delta x|^{2}+o\left(|\Delta x|^{2}\right)>0$, а значит, $x^{0}$ - точка строгого безусловного локального минимума.

Пункт (2) сводится к пункту (1) заменой функции $f(x)$ на $-f(x)$.
3) Пусть квадратичная форма $d^{2} f\left(x^{0}\right)=(d x)^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) d x$ знаконеопределена, т. е. $\exists \xi_{1}, \xi_{2} \in \mathbb{R}^{n}: \xi_{1}^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \xi_{1}>0, \xi_{2}^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \xi_{2}<0$. Применяя формулу (2) для $\Delta x=t \xi_{1}$, получим $f\left(x^{0}+t \xi_{1}\right)-f\left(x^{0}\right)=$
$=\Delta f=\frac{1}{2}(\Delta x)^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \Delta x+o\left(|\Delta x|^{2}\right)=\frac{1}{2}\left(\xi_{1}\right)^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \xi_{1} t^{2}+o\left(t^{2}\right)$

при $t \rightarrow 0$. Поскольку

$
\lim _{t \rightarrow 0} \frac{1}{t^{2}}\left(\frac{1}{2}\left(\xi_{1}\right)^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \xi_{1} t^{2}+o\left(t^{2}\right)\right)=\frac{1}{2}\left(\xi_{1}\right)^{T} f_{x x}^{\prime \prime}\left(x^{0}\right) \xi_{1}>0
$

то

$
\exists \delta_{1}>0: \forall t \in\left(0, \delta_{1}\right) \hookrightarrow \Delta f=f\left(x^{0}+t \xi_{1}\right)-f\left(x^{0}\right)>0 .
$

Аналогично,

$
\exists \delta_{2}>0: \forall t \in\left(0, \delta_{2}\right) \hookrightarrow \Delta f=f\left(x^{0}+t \xi_{2}\right)-f\left(x^{0}\right)<0 .
$

Поэтому $\forall \delta>0 \quad \exists t_{1}=\min \left\{\frac{\delta_{1}}{2}, \frac{\delta}{2|\xi_{1}|}\right\}, \exists t_{2}=\min \left\{\frac{\delta_{2}}{2}, \frac{\delta}{2|\xi_{2}|}\right\}$ такие, что $x^{1}=x^{0}+t_{1} \xi_{1} \in U_{\delta}\left(x^{0}\right), \quad x^{2}=x^{0}+t_{2} \xi_{2} \in U_{\delta}\left(x^{0}\right), \quad f\left(x^{1}\right)-$
$-f\left(x^{0}\right)>0, \quad f\left(x^{2}\right)-f\left(x^{0}\right)<0$. Следовательно, точка $x^{0}$ не является ни точкой локального минимума, ни точкой локального максимума функции $f$.
4) Пусть $f(x)$ - функция одной переменной $x \in \mathbb{R}$. Тогда в случае $f^{\prime \prime}\left(x_{0}\right)=0$ квадратичная форма $d^{2} f\left(x_{0}\right)=f^{\prime \prime}\left(x_{0}\right)(d x)^{2}$ не является положительно определенной, отрицательно определенной, а также не является знаконеопределенной.

Для функции $f(x)=x^{4}$ имеем $f^{\prime \prime}(0)=0$, а точка $x_{0}=0$ является точкой минимума.

Для функции $f(x)=x^{3}: f^{\prime \prime}(0)=0$, а точка $x_{0}=0$ не является точкой экстремума.
</block><block id='E13.1.1'>Задача 1. Пусть функция $f: \mathbb{R}^{2} \rightarrow \mathbb{R}$ дважды непрерывно дифференцируема и $\operatorname{det} f_{x x}^{\prime \prime}\left(x^{0}\right)<0$. Может ли функция $f$ достигать локальный безусловный экстремум в точке $x^{0}$ ?</block><block id='C13.2'>
## § 2. Условный экстремум
</block>
<block id='TX13.2.1'>
Пусть в окрестности точки $x^{0} \in \mathbb{R}^{n}$ заданы скалярная функция $f(x)$ и вектор-функция $g(x)=\left(\begin{array}{c}g_{1}(x) \\ \cdots \\ g_{m}(x)\end{array}\right)$. Рассмотрим задачу отыскания экстремума функции $f(x)$ на множестве $X \subset \mathbb{R}^{n}$, заданном системой уравнений $g(x)=\overline{0}$ :

Исследовать на экстремум $f(x)$ по $x \in \mathbb{R}^{n}: g(x)=\overline{0}$.

Далее будем всегда предполагать, что число ограничений $g_{i}(x)=$
$=0$ меньше числа переменных $x_{j}$ : $\quad m<n$.
</block>
<block id='TX13.2.2'>
Если система из $m$ уравнений $g(x)=\overline{0}$ разрешима относительно $m$ переменных, т. е. вектор $x \in \mathbb{R}^{n}$ можно разбить на два вектора $y \in \mathbb{R}^{m}$ и $z \in \mathbb{R}^{n-m}: x=\binom{y}{z}$ таких, что

$
g(y, z)=\overline{0} \quad \Longleftrightarrow \quad y=\varphi(z),
$

тогда задача (1) отыскания условного экстремума сводится к задаче отыскания безусловного экстремума функции $f(\varphi(z), z)$.

</block><block id='E13.2.1'>Пример 1. Найти локальные экстремумы функции $f(x, y, z)=$ $=-x^{3}-x^{2}+4 x y+2 x z-4 y^{2}+2 y z-z^{2}$ при условии $x+y-z=0$.Решение. Из условия $x+y-z=0$ можно выразить $z=x+y$, поэтому исходная задача сводится к задаче отыскания безусловных локальных экстремумов функции $F(x, y)=f(x, y, x+y)=-x^{3}+$ $+6 x y-3 y^{2}$. Найдем стационарные точки функции $F$ :$ \left\{\begin{array} { l } { F _ { x } ^ { \prime } = 0 } \\ { F _ { y } ^ { \prime } = 0 } \end{array} \right. \Leftrightarrow \left\{\begin{array} { l } { - 3 x ^ { 2 } + 6 y = 0 } \\ { 6 x - 6 y = 0 } \end{array} \right. \Leftrightarrow \left\{\begin{array}{l}x=y, \\ x^{2}=2 x .\end{array}\right.$Функция $F$ имеет две стационарные точки: $(0,0)$ и $(2,2)$.Исследуем знакоопределенность второго дифференциала в стационарных точках.Поскольку $F^{\prime \prime}(x, y)=\left(\begin{array}{cc}-6 x & 6 \\ 6 & -6\end{array}\right)$, то $F^{\prime \prime}(0,0)=\left(\begin{array}{cc}0 & 6 \\ 6 & -6\end{array}\right)$, $d^{2} F(0,0)=12 d x d y-6(d y)^{2}$.При $\binom{d x}{d y}=\binom{0}{1}$ имеем $d^{2} F(0,0)=-6<0$, а при $\binom{d x}{d y}=\binom{1}{1}$ получаем $d^{2} F(0,0)=12-6=6>0$. Следовательно, квадратичная форма $d^{2} F(0,0)$ знаконеопределена, и в точке ( 0,0 ) нет локального экстремума.Матрица $F^{\prime \prime}(2,2)=\left(\begin{array}{cc}-12 & 6 \\ 6 & -6\end{array}\right)$ отрицательно определена, так как матрица $-F^{\prime \prime}(2,2)=\left(\begin{array}{cc}12 & -6 \\ -6 & 6\end{array}\right)$ положительно определена, что проверяется по критерию Сильвестра: $\Delta_{1}=12>0, \Delta_{2}=12 \cdot 6-$ $-6^{2}>0$. Поэтому в точке $\left(x_{0}, y_{0}\right)=(2,2)$ функция $F$ достигаетлокального минимума. Следовательно, в точке $\left(x_{0}, y_{0}, z_{0}\right)=(2,2,4)$ функция $f(x, y, z)$ достигает локального минимума, равного $-x_{0}^{3}+$ $+6 x_{0} y_{0}-3 y_{0}^{2}=4$.</block>
Свойство 5. (Интегрируемость модуля.) Если функция $f(x)$ интегрируема на множестве $E \subset \mathbb{R}^{n}$, то функция $|f(x)|$ также интегрируема на множестве $E$.
</block>
<block id='P14.2.6'>
Свойство 6. (Интегрируемость по подмножеству.) Если функция $f(x)$ интегрируема на множестве $E$, то $f$ интегрируема на любом измеримом подмножестве множества $E$.
</block>
то $f$ интегрируема на любом измеримом подмножестве множества $E$.
</block>
<block id='P14.2.7'>
Доказательство свойств 1-6 аналогично доказательству соответствующих свойств интеграла Римана по отрезку.
</block>
<block id='T14.2.1'>
Теорема 1. (Свойство аддитивности кратного интеграла относительно множеств интегрирования.) Пусть функция $f(x)$ ограничена и интегрируема на множествах $X \subset \mathbb{R}^{n}$ и $Y \subset \mathbb{R}^{n}$, не имеющих общих внутренних точек. Тогда $f(x)$ интегрируема на множестве $X \bigcup Y$, причем

$
\begin{gather*}
\int \cdots \int_{X \cup Y} f(x) d x_{1} \cdots d x_{n}= \\
=\int \cdots \int f(x) d x_{1} \cdots d x_{n}+\int \cdots \int f(x) d x_{1} \cdots d x_{n} \tag{1}
\end{gather*}
$

Доказательство. Так как функция $f$ ограничена на множестве $X \bigcup Y$, то $\exists C \in \mathbb{R}: \forall x \in X \bigcup Y \hookrightarrow|f(x)| \leq C$.

Пусть задано произвольное разбиение $\mathrm{T}=\left\{E_{i}\right\}_{i=1}^{I}$ множества $X \bigcup Y$. Определим $X_{i}=X \bigcap E_{i}, Y_{i}=Y \bigcap E_{i} \quad \forall i \in\{1, \ldots, I\}$. Из непустых множеств $X_{i}$ составим разбиение $\mathrm{T}_{X}$ множества $X$, а из непустых множеств $Y_{i}$ - разбиение $T_{Y}$ множества $Y$. Рассмотрим множество индексов

$
\mathfrak{I}=\left\{i \in\{1, \ldots, I\}: E_{i} \not \subset X \text { и } E_{i} \bigcap X \neq \emptyset\right\} .
$

Тогда

$
\begin{equation*}
\left|s(f ; \mathrm{T})-s\left(f ; \mathrm{T}_{X}\right)-s\left(f ; \mathrm{T}_{Y}\right)\right| \leq 2 C \sum_{i \in \mathfrak{I}} \mu\left(E_{i}\right) \tag{2}
\end{equation*}
$

Поскольку при $i \in \mathfrak{I}$ существуют точки $x, y \in E_{i}$ такие, что $x \in$ $\in X, y \notin X$, то на отрезке с концами в точках $x$ и $y$ найдется точка $z \in \partial X$. Следовательно, $E_{i} \subset U_{\delta_{i}}(\partial X)$, где $\delta_{i}=2 \operatorname{diam} E_{i} \leq 2 \ell(T)$. Поэтому $\bigcup_{i \in \mathfrak{I}} E_{i} \subset U_{2 \ell(\mathrm{~T})}(\partial X)$. Так как $\mu(\partial X)=0$, то в силу леммы 2 $\S 1$ главы 7 имеем $\mu^{*}\left(U_{2 \ell(\mathrm{~T})}(\partial X)\right) \rightarrow 0$ при $\ell(\mathrm{T}) \rightarrow 0$. Следовательно,

$
\sum_{i \in \mathfrak{I}} \mu\left(E_{i}\right)=\mu\left(\bigcup_{i \in \mathfrak{I}} E_{i}\right) \leq \mu^{*}\left(U_{2 \ell(\mathrm{~T})}(\partial X)\right) \rightarrow 0 \quad \text { при } \quad \ell(\mathrm{T}) \rightarrow 0 .
$

Отсюда из неравенства (2) получаем

$
\begin{equation*}
\lim _{\ell(\mathrm{T}) \rightarrow 0}\left(s(f ; \mathrm{T})-s\left(f ; \mathrm{T}_{X}\right)-s\left(f ; \mathrm{T}_{Y}\right)\right)=0 \tag{3}
\end{equation*}
$

Обозначим

$
J_{X}=\int \cdots \int f(x) d x_{1} \cdots d x_{n}, \quad J_{Y}=\int \cdots \int f(x) d x_{1} \cdots d x_{n}
$

Так как $\ell\left(\mathrm{T}_{X}\right) \leq \ell(\mathrm{T}), \ell\left(\mathrm{T}_{Y}\right) \leq \ell(\mathrm{T})$ и в силу интегрируемости функции $f$ на множествах $X$ и $Y$ справедливы равенства $\lim _{\ell\left(\mathrm{T}_{X}\right) \rightarrow 0} s\left(f ; \mathrm{T}_{X}\right)=J_{X}, \lim _{\ell\left(\mathrm{T}_{Y}\right) \rightarrow 0} s\left(f ; \mathrm{T}_{Y}\right)=J_{Y}$, то из соотношения (3) получаем $\lim _{\ell(\mathrm{T}) \rightarrow 0} s(f ; \mathrm{T})=J_{X}+J_{Y}$. Аналогично, для верхней суммы Дарбу $\lim _{\ell(\mathrm{T}) \rightarrow 0} S(f ; \mathrm{T})=J_{X}+J_{Y}$. Поэтому существует

$
\int_{X \cup Y} \cdots \int_{Y} f(x) d x_{1} \cdots d x_{n}=J_{X}+J_{Y}
$
</block>
<block id='R14.2.1'>Замечание. Для неограниченной функции $f$ из интегрируемости $f$ на множествах $X$ и $Y$ не следует интегрируемость $f$ на $X \bigcup Y$. Пусть, например, $X=(0,1) \times(0,1), Y=(0,1) \times\{0\}, f(x, y)=$ $=\left\{\begin{array}{ll}0, & y \in(0,1), \\ 1 / x, & y=0 .\end{array}\right.$ Поскольку суммы Римана функции $f$ по любому разбиению множества $X$ и $Y$ равны нулю, то 2 -кратные интегралы функции $f$ по множествам $X$ и $Y$ существуют и равны нулю. Поскольку для множества $X \bigcup Y=(0,1) \times[0,1)$ имеет место условие $\overline{\operatorname{int}(X \bigcup Y)}=\overline{X \bigcup Y}=[0,1] \times[0,1]$ и функция $f$ неограничена намножестве $X \bigcup Y$, то в силу теоремы 1 \S 1 функция $f$ неинтегрируема на $X \bigcup Y$.</block><block id='T14.2.2'>
Теорема 2. (Достаточное условие интегрируемости.) Если функция $f$ непрерывна на измеримом компакте $E \subset \mathbb{R}^{n}$, то $f$ интегрируема на $E$.

Доказательство. В силу теоремы Кантора из непрерывности функции $f(x)$ на компакте $E$ следует ее равномерная непрерывность на этом компакте, т. е. модуль непрерывности функции $f$ :

$
\omega(\delta)=\sup _{x^{\prime}, x^{\prime \prime} \in E,\left|x^{\prime}-x^{\prime \prime}\right|<\delta}\left|f\left(x^{\prime}\right)-f\left(x^{\prime \prime}\right)\right| \rightarrow 0 \quad \text { при } \quad \delta \rightarrow 0 .
$

Поскольку для любого разбиения $\mathrm{T}=\left\{E_{i}\right\}_{i=1}^{I}$ множества $E$ при $x^{\prime}, x^{\prime \prime} \in E_{i}$ выполняется неравенство $\left|x^{\prime}-x^{\prime \prime}\right| \leq$ $\leq \operatorname{diam}\left(E_{i}\right) \leq \ell(\mathrm{T})<2 \ell(T)$, то $\omega_{i}(f) \leq \omega(2 \ell(T))$. Следовательно,

$
\begin{gathered}
S(f ; \mathrm{T})-s(f ; \mathrm{T})=\sum_{i=1}^{I} \omega_{i}(f) \mu\left(E_{i}\right) \leq \omega(2 \ell(T)) \sum_{i=1}^{I} \mu\left(E_{i}\right)=
=\omega(2 \ell(T)) \mu(E) \rightarrow 0 \quad \text { при } \quad \ell(\mathrm{T}) \rightarrow 0
\end{gathered}
$

и в силу критерия интегрируемости функция $f$ интегрируема на $E$.
</block>
<block id='C14.3'>
## § 3. Сведение кратного интеграла к повторному
</block>
<block id='T14.3.1'>
Теорема 1. Пусть задано измеримое множество $E \subset \mathbb{R}^{n}$, отрезок $[a, b]$ и функция $g\left(x_{1}, \ldots, x_{n}, y\right)$, интегрируемая на цилиндре $\Omega=$ $=E \times[a, b] \subset \mathbb{R}^{n+1}$. Пусть для любой точки $x=\left(x_{1}, \ldots, x_{n}\right) \in E$ существует интеграл $\int_{a}^{b} g(x, y) d y$. Тогда функция $h(x)=\int_{a}^{b} g(x, y) d y$ интегрируема на множестве $E$ и справедлива формула

$
\begin{aligned}
& \int \cdots \int g\left(x_{1}, \ldots, x_{n}, y\right) d x_{1} \cdots d x_{n} d y= \\
= & \int \cdots \int d x_{1} \cdots d x_{n} \int_{a}^{b} g\left(x_{1}, \ldots, x_{n}, y\right) d y .
\end{aligned}
$

</block>
<block id='P14.3.1'>
## Доказательство.

Зафиксируем произвольное число $\delta>0$. Пусть $T_{\delta}^{E}=\left\{E_{i}\right\}_{i=1}^{I}-$ произвольное разбиение множества $E$ мелкости $\ell\left(T_{\delta}^{E}\right) \leq \delta$. Пусть $\xi_{T_{\delta}^{E}}=$
$=\left\{\xi_{i}\right\}_{i=1}^{I}-$ произвольная выборка, соответствующая разбиению $T_{\delta}^{E}$, т. е. $\xi_{i} \in E_{i}$ для любого $i \in\{1, \ldots, I\}$. Так как $h\left(\xi_{i}\right)=\int_{a}^{b} g\left(\xi_{i}, y\right) d y$, то по определению интеграла Римана существует $\quad\left\{y_{i}^{k}\right\}_{k=0}^{K_{i}} \quad-$ разбиение отрезка $[a, b]$ такое, что для любого
![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-027.jpg?height=788&width=686&top_left_y=220&top_left_x=650) $i \in\{1, \ldots, I\}$

$
\begin{equation*}
\max _{k \in\left\{1, \ldots, K_{i}\right\}}\left|y_{i}^{k}-y_{i}^{k-1}\right| \leq \delta \tag{1}
\end{equation*}
$

и

$
\left|h\left(\xi_{i}\right)-\sum_{k=1}^{K_{i}} g\left(\xi_{i}, y_{i}^{k}\right)\left(y_{i}^{k}-y_{i}^{k-1}\right)\right| \leq \delta .
$

Умножая последнее неравенство на $\mu\left(E_{i}\right)$ и суммируя по $i \in$ $\in\{1, \ldots, I\}$, получаем

$
\begin{align*}
\mid \sum_{i=1}^{I} \mu\left(E_{i}\right) h\left(\xi_{i}\right)- & \sum_{i=1}^{I} \sum_{k=1}^{K_{i}} \mu\left(E_{i}\right) g\left(\xi_{i}, y_{i}^{k}\right)\left(y_{i}^{k}-y_{i}^{k-1}\right) \mid \leq  \tag{2}\\
& \leq \sum_{i=1}^{I} \mu\left(E_{i}\right) \delta=\mu(E) \delta
\end{align*}
$

Обозначим
$\Omega_{i}^{k}=E_{i} \times\left[y_{i}^{k-1}, y_{i}^{k}\right], \quad T_{\delta}^{\Omega}=\left\{\Omega_{i}^{k}\right\}_{\substack{i=1, \ldots, I \\ k=1, \ldots, K_{i}}}, \quad \xi_{T_{\delta}^{\Omega}}=\left\{\left(\xi_{i}, y_{i}^{k}\right)\right\}_{\substack{i=1, \ldots, I \\ k=1, \ldots, K_{i}}}$.

Из теоремы 4 § 1 главы 7 (теоремы об измеримости цилиндра) следует, что $\mu\left(\Omega_{i}^{k}\right)=\mu\left(E_{i}\right)\left(y_{i}^{k}-y_{i}^{k-1}\right)$. Поэтому неравенство (2) можно записать через суммы Римана:

$
\begin{equation*}
\left|\sigma\left(h, T_{\delta}^{E}, \xi_{T_{\delta}^{E}}\right)-\sigma\left(g, T_{\delta}^{\Omega}, \xi_{T_{\delta}^{\Omega}}\right)\right| \leq \mu(E) \delta . \tag{3}
\end{equation*}
$

В силу теоремы Пифагора, используя неравенства (1) и $\ell\left(T_{\delta}^{E}\right) \leq \delta$, получаем неравенства

$
\operatorname{diam} \Omega_{i}^{k} \leq \sqrt{\left(\operatorname{diam} E_{i}\right)^{2}+\left(y_{i}^{k}-y_{i}^{k-1}\right)^{2}} \leq \sqrt{\left(\ell\left(T_{\delta}^{E}\right)\right)^{2}+\delta^{2}} \leq \delta \sqrt{2}
$

Поэтому

$
\begin{equation*}
\ell\left(T_{\delta}^{\Omega}\right) \leq \delta \sqrt{2} \rightarrow 0 \quad \text { при } \quad \delta \rightarrow 0 . \tag{4}
\end{equation*}
$

Обозначим

$
J=\int \cdots \int g\left(x_{1}, \ldots, x_{n}, y\right) d x_{1} \cdots d x_{n} d y
$

По определению интеграла и в силу соотношения (4) имеем $\sigma\left(g, T_{\delta}^{\Omega}, \xi_{T_{\delta}^{\Omega}}\right) \rightarrow J$ при $\delta \rightarrow 0$. Следовательно, используя неравенство (3), получаем

$
\sigma\left(h, T_{\delta}^{E}, \xi_{T_{\delta}^{E}}\right) \xrightarrow{\delta \rightarrow 0} J,
$

то есть существует

$
\int \cdots \int h(x) d x_{1} \cdots d x_{n}=J
$
</block>
<block id='R14.3.1'>
Замечание. Из теоремы 1 следует, что если функция $g(x, y)$ интегрируема на прямоугольнике $[a, b] \times[c, d]$ и существуют повторные интегралы $\int_{a}^{b} d x \int_{c}^{d} g(x, y) d y$ и $\int_{c}^{d} d y \int_{a}^{b} g(x, y) d x$, то они равны кратному и, следовательно, равны между собой. Если же кратный интеграл не существует, то указанные повторные интегралы могут существовать, но быть различными. Например, для функции $g(x, y)=\frac{x^{2}-y^{2}}{\left(x^{2}+y^{2}\right)^{2}}$

имеет место $\int_{0}^{1} d y \int_{0}^{1} g(x, y) d x=-\pi / 4$, но $\int_{0}^{1} d x \int_{0}^{1} g(x, y) d y=\pi / 4$. Действительно, интегрируя по частям, получаем $\int_{0}^{1} \frac{d x}{x^{2}+y^{2}}=\left.\frac{x}{x^{2}+y^{2}}\right|_{0} ^{1}+$ $+2 \int_{0}^{1} \frac{x^{2}}{\left(x^{2}+y^{2}\right)^{2}} d x$, следовательно, $\int_{0}^{1} \frac{x^{2}-y^{2}}{\left(x^{2}+y^{2}\right)^{2}} d x=-\left.\frac{x}{x^{2}+y^{2}}\right|_{x=0} ^{x=1}=-\frac{1}{1+y^{2}}$, поэтому $\int_{0}^{1} d y \int_{0}^{1} g(x, y) d x=-\int_{0}^{1} \frac{d y}{1+y^{2}}=-\pi / 4$. Второй повторный интеграл вычисляется аналогично.
</block>
<block id='T14.3.2'>
Теорема 2. Пусть

1) множество $G$ элементарно относительно оси $x_{n+1}$, т. е.

$
\begin{aligned}
& G=\left\{\left(x_{1}, \ldots, x_{n+1}\right):\left(x_{1}, \ldots, x_{n}\right) \in E\right.\n& \left.\varphi\left(x_{1}, \ldots, x_{n}\right)<x_{n+1}<\psi\left(x_{1}, \ldots, x_{n}\right)\right\}
\end{aligned}
$

где функции $\varphi$ и $\psi$ непрерывны на замыкании измеримого множества $E$ и $\varphi(x)<\psi(x) \quad \forall x \in E$;
2) функция $f\left(x_{1}, \ldots, x_{n+1}\right)$ ограничена и интегрируема на множестве $G$;
3) для любой точки $\left(x_{1}, \ldots, x_{n}\right) \in E$ существует интеграл

$
h\left(x_{1}, \ldots, x_{n}\right)=\int_{\varphi\left(x_{1}, \ldots, x_{n}\right)}^{\psi\left(x_{1}, \ldots, x_{n}\right)} f\left(x_{1}, \ldots, x_{n+1}\right) d x_{n+1}
$

Тогда функция $h$ интегрируема на множестве $E$ и справедлива формула

$
\begin{gather*}
\int \cdots \int f\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}= \\
=\int \cdots \int d x_{1} \cdots d x_{n} \int_{\varphi\left(x_{1}, \ldots, x_{n}\right)}^{\psi\left(x_{1}, \ldots, x_{n}\right)} f\left(x_{1}, \ldots, x_{n+1}\right) d x_{n+1} \tag{5}
\end{gather*}
$

Доказательство. Определим числа $a=\min _{x \in \bar{E}} \varphi(x), b=\max _{x \in \bar{E}} \psi(x)$ и множество $\Omega=E \times[a, b]$. На множестве $\Omega$ определим функцию

$
g\left(x_{1}, \ldots, x_{n+1}\right)= \begin{cases}f\left(x_{1}, \ldots, x_{n+1}\right), & \left(x_{1}, \ldots, x_{n+1}\right) \in G \\ 0, & \left(x_{1}, \ldots, x_{n+1}\right) \notin G .\end{cases}
$

Поскольку функция $g$ ограничена и интегрируема на множествах $G$ и $\Omega \backslash G$, то по свойству аддитивности интеграла относительно множеств интегрирования функция $g$ интегрируема на множестве $\Omega$ и

$
\begin{align*}
& \int \cdots \int g\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}= \\
= & \int_{G} \cdots \int_{G} g\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}+ \\
+ & \int_{\Omega \backslash G} \cdots \int_{G} g\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}=  \tag{6}\\
= & \int_{G} \cdots \int_{G} f\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}
\end{align*}
$

В силу теоремы 1 функция $h\left(x_{1}, \ldots, x_{n}\right)=\int_{a}^{b} g\left(x_{1}, \ldots, x_{n+1}\right) d x_{n+1}$ интегрируема на $E$ и справедлива формула

$
\begin{gathered}
\int \cdots \int g\left(x_{1}, \ldots, x_{n+1}\right) d x_{1} \cdots d x_{n+1}= \\
=\int \cdots \int d x_{1} \cdots d x_{n} \int_{a}^{b} g\left(x_{1}, \ldots, x_{n+1}\right) d x_{n+1}= \\
=\int \cdots \int d x_{1} \cdots d x_{n} \int_{\varphi\left(x_{1}, \ldots, x_{n}\right)}^{\psi\left(x_{1}, \ldots, x_{n}\right)} f\left(x_{1}, \ldots, x_{n+1}\right) d x_{n+1}
\end{gathered}
$

откуда и из (6) получаем (5).
</block>
<block id='C14.4'>
## § 4. Геометрический смысл модуля якобиана
</block>
<block id='D14.4.1'>
Определение. Пусть функция $f(x)$ определена и непрерывна на множестве $G \subset \mathbb{R}^{n}$. Будем говорить, что функция $f(x)$ непрерывно продолжима на замыкание множества $G$, если существует функция $\widetilde{f}(x)$, непрерывная на $\bar{G}$ и совпадающая с $f(x)$ на $G$.
</block>
<block id='D14.4.2'>
Определение. Будем говорить, что функция $f(x)$ является $k$ раз непрерывно дифферениируемой на замыкании открытого множества $G \subset \mathbb{R}^{n}$, если

1) $f(x)$ непрерывна на $\bar{G}$;
2) все частные производные функции $f$ до порядка $k$ включительно существуют в $G$ и непрерывно продолжимы на $\bar{G}$.

Вектор-функция называется $k$ раз непрерывно дифференцируемой на замыкании открытого множества, если все ее компоненты обладают этим свойством.
</block>
<block id='TX14.4.1'>
Пусть $\mathbb{R}_{u v}^{2}$ - двумерное арифметическое пространство точек $\vec{u}=\binom{u}{v}$, а $\mathbb{R}_{x y}^{2}$ - двумерное арифметическое пространство точек $\vec{x}=\binom{x}{y}$. Пусть заданы открытые множества $G \subset \mathbb{R}_{u v}^{2}$ и $G^{*} \subset \mathbb{R}_{x y}^{2}$. Рассмотрим отображение (вектор-функцию) $F: G \rightarrow G^{*}$, значения которого $F(\vec{u})=\binom{x(u, v)}{y(u, v)}$.

Будем предполагать, что отображение $F$ :

$
\begin{equation*}
\mathbb{R}_{u v}^{2} \quad \supset \quad \underset{\substack{ \text { откр. } \\ \text { измер. }}}{G} \quad \stackrel{F}{\rightleftarrows} \quad \underset{\substack{G^{*} \\ \text { иткр. } \\ \text { измер.}}}{G^{*} \text { ( }} \tag{1}
\end{equation*}
$

обладает следующими свойствами:
$1^{o}$. $\quad F$ взаимно однозначно отображает $G$ в $G^{*}$;
$2^{o}$. отображение $F$ непрерывно дифференцируемо на $\bar{G}$;
$3^{o}$. $J_{F}(\vec{u}) \neq 0$ для любой точки $\vec{u} \in G$.
Здесь $J_{F}(\vec{u})$ - якобиан отображения $F$ в точке $\vec{u}=\binom{u}{v}$ :

$
J_{F}(\vec{u})=\operatorname{det} \mathcal{D} F(\vec{u})=\operatorname{det}\left(\begin{array}{ll}
x_{u}^{\prime}(u, v) & x_{v}^{\prime}(u, v) \\
y_{u}^{\prime}(u, v) & y_{v}^{\prime}(u, v)
\end{array}\right)=\frac{\partial(x, y)}{\partial(u, v)} .
$
</block>
<block id='L14.4.1'>
Лемма 1. Для любого множества $E \subset G$ образ границы $E$ при отображении $F$ совпадает с границей образа $E$ :

$
F(\partial E)=\partial F(E) .
$

Доказательство. Зафиксируем произвольную точку $\vec{u}_{0} \in \partial E$. Так как $\vec{u}_{0} \in \bar{E}$, то существует последовательность $\left\{\vec{u}_{k}\right\} \subset E$ такая, что $\lim _{k \rightarrow \infty} \vec{u}_{k}=\vec{u}_{0}$. В силу непрерывности отображения $F$ на множестве $\bar{G}$ имеем

$
\begin{equation*}
\lim _{k \rightarrow \infty} F\left(\vec{u}_{k}\right)=F\left(\vec{u}_{0}\right) \tag{2}
\end{equation*}
$

Поскольку $F\left(\vec{u}_{k}\right) \in F(E)$ для любого $k \in \mathbb{N}$, то из соотношения (2) следует включение

$
\begin{equation*}
F\left(\vec{u}_{0}\right) \in \overline{F(E)} . \tag{3}
\end{equation*}
$

Покажем, что

$
\begin{equation*}
F\left(\vec{u}_{0}\right) \in \partial F(E) . \tag{4}
\end{equation*}
$

Рассмотрим сначала случай $\vec{u}_{0} \in G$. Так как множество $G$ открыто, то $\vec{u}_{0} \in \operatorname{int} G$. Тогда в силу включения $\vec{u}_{0} \in \partial E$ найдется последовательность $\left\{\vec{w}_{k}\right\} \subset G \backslash E$ такая, что $\lim _{k \rightarrow \infty} \vec{w}_{k}=\vec{u}_{0}$. Поскольку отображение $F: G \rightarrow F(G)$ взаимно однозначно, то $F\left(\vec{w}_{k}\right) \notin F(E)$ для любого $k \in \mathbb{N}$, а в силу непрерывности $F$ справедливо равенство $\lim _{k \rightarrow \infty} F\left(\vec{w}_{k}\right)=F\left(\vec{u}_{0}\right)$. Поэтому $F\left(\vec{u}_{0}\right) \notin \operatorname{int} F(E)$ и в силу включения (3) получаем включение (4) в случае $\vec{u}_{0} \in G$.

Пусть теперь $\vec{u}_{0} \notin G$. Если $F\left(\vec{u}_{0}\right) \notin F(E)$, то, используя включение (3), опять приходим к включению (4). Предположим, что $F\left(\vec{u}_{0}\right) \in$ $\in F(E)$, т. е. существует вектор $\vec{v}_{0} \in E \subset G$ такой, что $F\left(\vec{u}_{0}\right)=F\left(\vec{v}_{0}\right)$. Поскольку $\vec{u}_{0} \notin G$, а $\vec{v}_{0} \in G$, то $\vec{v}_{0} \neq \vec{u}_{0}$. Из соотношения (2) следует, что $\lim _{k \rightarrow \infty} F\left(\vec{u}_{k}\right)=F\left(\vec{v}_{0}\right)$. В силу теоремы об обратном отображении найдется последовательность $\left\{\vec{v}_{k}\right\} \subset G$ такая, что $\lim _{k \rightarrow \infty} \vec{v}_{k}=\vec{v}_{0}$ и $F\left(\vec{v}_{k}\right)=F\left(\vec{u}_{k}\right)$ при достаточно больших $k$. Тогда при достаточно больших $k$ имеем $\vec{v}_{k} \neq \vec{u}_{k}, \vec{u}_{k} \in G, \vec{v}_{k} \in G, F\left(\vec{v}_{k}\right)=F\left(\vec{u}_{k}\right)$. Это противоречит условию $1^{o}$ ). Итак, включение (4) доказано. Следовательно,

$
\begin{equation*}
F(\partial E) \subset \partial F(E) . \tag{5}
\end{equation*}
$

Докажем обратное включение. Зафиксируем точку $\vec{x}_{0} \in \partial F(E)$. Тогда найдется последовательность $\left\{\vec{x}_{k}\right\} \subset F(E)$ такая, что
$\lim _{k \rightarrow \infty} \vec{x}_{k}=\vec{x}_{0}$. Поскольку $\left\{\vec{x}_{k}\right\} \subset F(E)$, то для любого индекса $k \in$ $\in \mathbb{N}$ найдется вектор $\vec{u}_{k} \in E$ такой, что $F\left(\vec{u}_{k}\right)=\vec{x}_{k}$. Так как множество $G$ измеримо, то оно ограничено. Следовательно, его подмножество $E$ также ограничено. Поэтому существует подпоследовательность $\left\{\vec{u}_{k_{j}}\right\}$, сходящаяся к некоторому вектору $\vec{u}_{0} \in \bar{E}$. В силу непрерывности отображения $F$ на множестве $\bar{G}$ справедливо равенство $F\left(\vec{u}_{0}\right)=\vec{x}_{0}$. Если $\vec{u}_{0} \in \operatorname{int} E$, то в силу теоремы об обратном отображении имеем $\vec{x}_{0}=F\left(\vec{u}_{0}\right) \in \operatorname{int} F(E)$, что противоречит включению $\vec{x}_{0} \in \partial F(E)$. Поэтому $\vec{u}_{0} \in \partial E$. Следовательно, $\vec{x}_{0} \in F(\partial E)$. Таким образом, включение, обратное к (5), также доказано.
</block>
<block id='TX14.4.2'>Наряду с нелинейным отображением $F$ рассмотрим линейное отображение $F^{\operatorname{lin}}$ :

$
F^{\operatorname{lin}}(\vec{u})=A\binom{u}{v}+\binom{c_{1}}{c_{2}}=\binom{a_{11} u+a_{12} v+c_{1}}{a_{21} u+a_{22} v+c_{2}}, \quad \text { где } \quad \vec{u}=\binom{u}{v}
$

задаваемое матрицей $A=\left(\begin{array}{ll}a_{11} & a_{12} \\ a_{21} & a_{22}\end{array}\right)$ и столбцом $\binom{c_{1}}{c_{2}}$. Далее мы будем использовать следующие два свойства линейных отображений.
</block>
<block id='P14.4.1'>
Из свойства нормы матрицы (глава $12, \S 2$, лемма 1) следует
Первое свойство линейных отображений. При линейном отображении отношение расстояния между образами двух точек к расстоянию между прообразами не превосходит нормы матрицы линейного отображения:

$
\frac{\left|F^{\operatorname{lin}}\left(\vec{u}_{1}\right)-F^{\operatorname{lin}}\left(\vec{u}_{2}\right)\right|}{\left|\vec{u}_{1}-\vec{u}_{2}\right|} \leq\|A\| \quad \forall \vec{u}_{1} \in \mathbb{R}^{2} \quad \forall \vec{u}_{2} \in \mathbb{R}^{2}: \vec{u}_{1} \neq \vec{u}_{2} .
$

Второе свойство линейных отображений. Если $\operatorname{det} A \neq 0$, то линейное отображение с матрицей $A$ переводит параллелограмм в параллелограмм, причем отношение площади образа к площади прообраза равно модулю $\operatorname{det} A$.
</block>
<block id='P14.4.2'>
Действительно, рассмотрим параллелограмм $P$, построенный на векторах $\vec{b}_{1}=\binom{b_{11}}{b_{21}}$ и $\vec{b}_{2}=\binom{b_{12}}{b_{22}}$. При отображении $F^{\operatorname{lin}}$ он перейдет в параллелограмм $P^{*}$, построенный на векторах $\vec{b}_{1}^{*}=A \vec{b}_{1}$ и $\vec{b}_{2}^{*}=$ $=A \vec{b}_{2}$. Площадь параллелограмма $P$ равна длине векторного произведения векторов $\left(\begin{array}{c}b_{11} \\ b_{21} \\ 0\end{array}\right)$ и $\left(\begin{array}{c}b_{12} \\ b_{22} \\ 0\end{array}\right): \mu(P)=\left|b_{11} b_{22}-b_{12} b_{21}\right|=|\operatorname{det} B|$, где $B=\left(\begin{array}{ll}b_{11} & b_{12} \\ b_{21} & b_{22}\end{array}\right)$. Аналогично, $\mu\left(P^{*}\right)=|\operatorname{det} B^{*}|$, где столбцы матрицы $B^{*}$ равны $\vec{b}_{1}^{*}=A \vec{b}_{1}$ и $\vec{b}_{2}^{*}=A \vec{b}_{2}$, а значит, $B^{*}=A B$. Следовательно,

$\frac{\mu\left(P^{*}\right)}{\mu(P)}=\frac{|\operatorname{det}(A B)|}{|\operatorname{det} B|}=|\operatorname{det} A| .$
</block>
<block id='TX14.4.3'>
Через $F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})$ будем обозначать линейное приближение отображения $F(\vec{u})$ в окрестности точки $\vec{u}_{0}=\binom{u_{0}}{v_{0}} \in G$ :

$
\begin{gather*}
F_{\vec{u}_{0}}^{\ln }(\vec{u})=F\left(\vec{u}_{0}\right)+\mathcal{D} F\left(\vec{u}_{0}\right)\left(\vec{u}-\vec{u}_{0}\right)= \\
=\binom{x\left(u_{0}, v_{0}\right)+x_{u}^{\prime}\left(u_{0}, v_{0}\right)\left(u-u_{0}\right)+x_{v}^{\prime}\left(u_{0}, v_{0}\right)\left(v-v_{0}\right)}{y\left(u_{0}, v_{0}\right)+y_{u}^{\prime}\left(u_{0}, v_{0}\right)\left(u-u_{0}\right)+y_{v}^{\prime}\left(u_{0}, v_{0}\right)\left(v-v_{0}\right)} . \tag{6}
\end{gather*}
$

Через $\left[\vec{u}, \vec{u}_{0}\right]$ обозначим отрезок в $\mathbb{R}_{u v}^{2}$ с концами в точках $\vec{u}=$ $=\binom{u}{v}$ и $\vec{u}_{0}=\binom{u_{0}}{v_{0}}$. Длина этого отрезка равна $\left|\vec{u}-\vec{u}_{0}\right|=$ $=\sqrt{\left(u-u_{0}\right)^{2}+\left(v-v_{0}\right)^{2}}$.
</block>
<block id='L14.4.2'>
## Лемма 2.

$
\sup _{\substack{\left\{\vec{u}, \vec{u}_{0}\right] \subset G \\ 0<\left|\vec{u}-\vec{u}_{0}\right| \leq \delta}} \frac{\left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|}{\left|\vec{u}-\vec{u}_{0}\right|} \longrightarrow 0 \quad \text { при } \quad \delta \rightarrow+0 .
$

Доказательство. Зафиксируем произвольную точку $\vec{u}_{0} \in G$ и применим теорему о среднем (глава 12 , § 2, теорема 1) к векторфункции

$
\begin{equation*}
g(\vec{u})=F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u}) . \tag{7}
\end{equation*}
$

Получим, что

$
\begin{equation*}
|g(\vec{u})|=\left|g(\vec{u})-g\left(\vec{u}_{0}\right)\right| \leq \sup _{\theta \in(0,1)}\left\|\mathcal{D} g\left(\vec{u}_{\theta}\right)\right\|\left|\vec{u}-\vec{u}_{0}\right|, \tag{8}
\end{equation*}
$

где $\vec{u}_{\theta}=\vec{u}_{0}+\theta\left(\vec{u}-\vec{u}_{0}\right)$.
Заметим, что

$
\begin{equation*}
\mathcal{D} g\left(\vec{u}_{\theta}\right)=\mathcal{D} F\left(\vec{u}_{\theta}\right)-\mathcal{D} F_{\vec{u}_{0}}^{\operatorname{lin}}\left(\vec{u}_{\theta}\right)=\mathcal{D} F\left(\vec{u}_{\theta}\right)-\mathcal{D} F\left(\vec{u}_{0}\right) . \tag{9}
\end{equation*}
$

Поскольку $\left|\vec{u}_{\theta}-\vec{u}_{0}\right| \leq\left|\vec{u}-\vec{u}_{0}\right|$, то, как следует из формул (7), (8), (9),

$
\begin{equation*}
\frac{\left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|}{\left|\vec{u}-\vec{u}_{0}\right|} \leq \sup _{\substack{\vec{u}_{0} \in G, \vec{u}^{\prime} \in G \\ 0<\left|\vec{u}^{\prime}-\vec{u}_{0}\right| \leq \delta}}\left\|\mathcal{D} F\left(\vec{u}^{\prime}\right)-\mathcal{D} F\left(\vec{u}_{0}\right)\right\| . \tag{10}
\end{equation*}
$

В силу непрерывной дифференцируемости отображения $F$ на $\bar{G}$ продолженные на $\bar{G}$ частные производные этого отображения непрерывны на компакте $\bar{G}$. Отсюда по теореме Кантора следует равномерная непрерывность продолженных частных производных отображения $F$ на $\bar{G}$, а значит, равномерная непрерывность этих частных производных на $G$. Поэтому матрица Якоби $\mathcal{D} F$ равномерно непрерывна на $G$, т. е. при $\delta \rightarrow+0$

$
\sup _{\substack{\vec{u}_{0} \in G, \vec{u}^{\prime} \in G \\ 0<\left|\vec{u}^{\prime}-\vec{u}_{0}\right| \leq \delta}}\left\|\mathcal{D} F\left(\vec{u}^{\prime}\right)-\mathcal{D} F\left(\vec{u}_{0}\right)\right\| \longrightarrow 0 .
$

Отсюда и из неравенства (10) получаем требуемое утверждение.
</block>
<block id='T14.4.1'>
Теорема 1. (Геометрический смысл модуля якобиана отображения.) Пусть задано отображение $F$ (см. (1)) со свойствами $1^{o}-3^{o}$.

При различных числах $h>0$ и векторах $\vec{u}_{0}=\binom{u_{0}}{v_{0}} \in G$ будем рассматривать квадраты

$
Q_{h}=Q_{h}\left(\vec{u}_{0}\right)=\left[u_{0}-h, u_{0}+h\right] \times\left[v_{0}-h, v_{0}+h\right] \subset G .
$

Тогда образы квадратов $Q_{h}$ при отображении $F$ являются измеримыми множествами и при $h \rightarrow+0$ отношение мер $\frac{\mu\left(F\left(Q_{h}\right)\right)}{\mu\left(Q_{h}\right)}$ стремится к модулю якобиана $\left|J_{F}\left(\vec{u}_{0}\right)\right|$ равномерно по всем точкам $\vec{u}_{0}$ таким, что квадраты $Q_{h}=Q_{h}\left(\vec{u}_{0}\right)$ содержатся в $G$ :

$
\sup _{\vec{u}_{0}: Q_{h}=Q_{h}\left(\vec{u}_{0}\right) \subset G}\left|\frac{\mu\left(F\left(Q_{h}\right)\right)}{\mu\left(Q_{h}\right)}-\left|J_{F}\left(\vec{u}_{0}\right)\right|\right| \longrightarrow 0 \quad \text { при } \quad h \rightarrow+0 .
$

Доказательство. Из теоремы о производной сложной функции следует, что образ непрерывно дифференцируемой кривой при непрерывно дифференцируемом отображении является непрерывно дифференцируемой кривой. Поэтому образ стороны квадрата $Q_{h}$ является непрерывно дифференцируемой кривой, а образ границы $Q_{h}$ - кусочно-гладкой, а значит, спрямляемой кривой. Отсюда и из теоремы 3 \S 1 главы 7 следует, что $\mu\left(F\left(\partial Q_{h}\right)\right)=0$, что вместе с леммой 1 текущего параграфа дает равенство $\mu\left(\partial F\left(Q_{h}\right)\right)=0$. Следовательно, в силу критерия измеримости множество $F\left(Q_{h}\right)$ измеримо.

В силу второго свойства линейных отображений образ квадрата $Q_{h}$ при отображении $F_{\vec{u}_{0}}^{\operatorname{lin}}$ является параллелограммом $S_{h}=$
$=F_{\vec{u}_{0}}^{\ln }\left(Q_{h}\right)$, причем

$
\begin{equation*}
\frac{\mu\left(S_{h}\right)}{\mu\left(Q_{h}\right)}=\left|\operatorname{det} \mathcal{D} F\left(\vec{u}_{0}\right)\right|=\left|J_{F}\left(\vec{u}_{0}\right)\right| . \tag{11}
\end{equation*}
$

Обозначим

$
\begin{gather*}
\sigma(h)=\sup _{\vec{u}_{0}: Q_{h}\left(\vec{u}_{0}\right) \subset G} \sup _{\vec{u} \in Q_{h}\left(\vec{u}_{0}\right)}\left|F(\vec{u})-F_{\vec{u}_{0}}^{\ln }(\vec{u})\right|, \tag{12}\\
\beta(\delta)=\sup _{\substack{\left[\vec{u}, \vec{u}_{0}\right] \subset G \\
0<\left|\vec{u}-\vec{u}_{0}\right| \leq \delta}} \frac{\left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|}{\left|\vec{u}-\vec{u}_{0}\right|} .
\end{gather*}
$

Согласно лемме 2

$
\begin{equation*}
\beta(\delta) \longrightarrow 0 \quad \text { при } \quad \delta \rightarrow+0 . \tag{13}
\end{equation*}
$

Покажем, что

$
\begin{equation*}
\sigma(h) \leq \sqrt{2} h \cdot \beta(h \sqrt{2}) \quad \forall h>0 . \tag{14}
\end{equation*}
$

Для этого зафиксируем произвольные число $h>0$ и вектор $\vec{u}_{0}$ такие, что $Q_{h}\left(\vec{u}_{0}\right) \subset G$, а также вектор $\vec{u} \in Q_{h}\left(\vec{u}_{0}\right)$ и покажем, что

$
\begin{equation*}
\left|F(\vec{u})-F_{\vec{u}_{0}}^{\ln }(\vec{u})\right| \leq \sqrt{2} h \cdot \beta(h \sqrt{2}) . \tag{15}
\end{equation*}
$

Действительно, если $\vec{u}=\vec{u}_{0}$, то в левой части неравенства (15) стоит ноль и, следовательно, это неравенство выполнено. Пусть $\vec{u} \neq \vec{u}_{0}$. Поскольку $\vec{u} \in Q_{h}$, то $\left|\vec{u}-\vec{u}_{0}\right| \leq h \sqrt{2}$. Следовательно,

$
\begin{aligned}
& \left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|=\frac{\left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|}{\left|\vec{u}-\vec{u}_{0}\right|} \cdot\left|\vec{u}-\vec{u}_{0}\right| \leq \\
& \quad \leq \sqrt{2} h \cdot \frac{\left|F(\vec{u})-F_{\vec{u}_{0}}^{\operatorname{lin}}(\vec{u})\right|}{\left|\vec{u}-\vec{u}_{0}\right|} \leq \sqrt{2} h \cdot \beta(h \sqrt{2}) .
\end{aligned}
$

Таким образом, неравенство (15) доказано. Переходя в неравенстве $(15)$ к супремуму по всем $\vec{u}_{0}$ таким, что $Q_{h}\left(\vec{u}_{0}\right) \subset G$, и по всем $\vec{u} \in$
$\in Q_{h}\left(\vec{u}_{0}\right)$, получаем неравенство (14). Из неравенства (14) и соотношения (13) следует соотношение

$
\begin{equation*}
\frac{\sigma(h)}{h} \rightarrow 0 \quad \text { при } \quad h \rightarrow+0 . \tag{16}
\end{equation*}
$

Пусть $p_{h}$ - периметр параллелограмма $S_{h}$. Из формулы (12) следует, что «криволинейный параллелограмм» $F\left(Q_{h}\right)$ содержится в замыкании $\sigma(h)$ - окрестности параллелограмма $S_{h}=F_{\vec{u}_{0}}^{\ln }\left(Q_{h}\right): \quad F\left(Q_{h}\right) \subset$
$\subset \overline{U_{\sigma(h)}\left(S_{h}\right)}$. Поэтому $\mu\left(F\left(Q_{h}\right)\right) \leq \mu\left(U_{\sigma(h)}\left(S_{h}\right)\right)$. Заметим, что площадь окрестности $U_{\sigma(h)}\left(S_{h}\right)$ отличается от площади параллелограмма $S_{h}$ не более чем на $\sigma(h) p_{h}+\pi \sigma^{2}(h)$ :

$
\mu\left(U_{\sigma(h)}\left(S_{h}\right)\right)-\mu\left(S_{h}\right) \leq \sigma(h) p_{h}+\pi \sigma^{2}(h) .
$

Следовательно,

$
\begin{equation*}
\mu\left(F\left(Q_{h}\right)\right)-\mu\left(S_{h}\right) \leq \sigma(h) p_{h}+\pi \sigma^{2}(h) . \tag{17}
\end{equation*}
$

![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-038.jpg?height=456&width=1085&top_left_y=212&top_left_x=249)

Докажем неравенство

$
\begin{equation*}
\mu\left(S_{h}\right)-\mu\left(F\left(Q_{h}\right)\right) \leq \sigma(h) p_{h} \tag{18}
\end{equation*}
$

Если минимальная из высот параллелограмма $S_{h}$ не превосходит $2 \sigma(h)$, то $\mu\left(S_{h}\right) \leq \sigma(h) p_{h}$, и неравенство (18) выполнено. Поэтому будем предполагать, что $2 \sigma(h)$ меньше высот параллелограмма $S_{h}$. Тогда существует параллелограмм $\widetilde{S}_{h}$, содержащийся в параллелограмме $S_{h}$ и такой, что стороны параллелограмма $\widetilde{S}_{h}$ параллельны соответствующим сторонам параллелограмма $S_{h}$ и находятся от них на расстоянии $\sigma(h)$.

При линейном отображении $F_{\vec{u}_{0}}^{\ln }$ точка $\vec{u}_{0}$, находящаяся в центре квадрата $Q_{h}$, перейдет в центр параллелограмма $S_{h}$, который обозначим через $\vec{x}_{0}: \vec{x}_{0}=F_{\vec{u}_{0}}^{\operatorname{lin}}\left(\vec{u}_{0}\right)$. Из определения параллелограмма $\widetilde{S}_{h}$ следует, что точка $\vec{x}_{0}$ является его центром, а значит, $\vec{x}_{0} \in \operatorname{int} \widetilde{S}_{h}$. Из формулы (6) следует, что $F_{\vec{u}_{0}}^{\ln }\left(\vec{u}_{0}\right)=F\left(\vec{u}_{0}\right)$. Поэтому $\vec{x}_{0}=F\left(\vec{u}_{0}\right)$.

Покажем, что

$
\begin{equation*}
\widetilde{S}_{h} \subset F\left(Q_{h}\right) \tag{19}
\end{equation*}
$

Предположим противное: существует точка $\vec{x}_{*} \in \widetilde{S}_{h} \backslash F\left(Q_{h}\right)$. Тогда на отрезке $\left[\vec{x}_{0}, \vec{x}_{*}\right]$ найдется точка $\vec{x}_{1} \in \partial F\left(Q_{h}\right)$. В силу леммы 1 имеем $\partial F\left(Q_{h}\right)=F\left(\partial Q_{h}\right)$. Поэтому существует точка $\vec{u}_{1} \in \partial Q_{h}$ такая, что $\vec{x}_{1}=F\left(\vec{u}_{1}\right)$. При этом $\vec{x}_{1} \in \overline{F\left(Q_{h}\right)}=F\left(Q_{h}\right)$ (множество $F\left(Q_{h}\right)$ замкнуто как образ компакта при непрерывном отображении) и, следовательно, $\vec{x}_{1} \neq \vec{x}_{*}$.

Из формулы (12) получаем неравенство $\left|F\left(\vec{u}_{1}\right)-F_{\vec{u}_{0}}^{\ln }\left(\vec{u}_{1}\right)\right| \leq \sigma(h)$. Поскольку $F_{\vec{u}_{0}}^{\operatorname{lin}}\left(\vec{u}_{1}\right) \in \partial S_{h}$, то расстояние от точки $\vec{x}_{1}=F\left(\vec{u}_{1}\right)$ до границы параллелограмма $S_{h}$ не превосходит $\sigma(h)$. С другой стороны,

из соотношений $\vec{x}_{0} \in \operatorname{int} \widetilde{S}_{h}, \vec{x}_{*} \in \widetilde{S}_{h}, \vec{x}_{1} \in\left[\vec{x}_{0}, \vec{x}_{*}\right], \vec{x}_{1} \neq \vec{x}_{*}$ следует, что $\vec{x}_{1} \in \operatorname{int} \widetilde{S}_{h}$, а значит, расстояние от точки $\vec{x}_{1}$ до границы параллелограмма $S_{h}$ строго больше $\sigma(h)$. Полученное противоречие доказывает включение (19). Из включения (19) и неравенства $\mu\left(S_{h}\right)-$
$-\mu\left(\widetilde{S}_{h}\right) \leq \sigma(h) p_{h}$ следует неравенство (18), которое вместе с неравенством (17) дает оценку

$
\begin{equation*}
\left|\mu\left(F\left(Q_{h}\right)\right)-\mu\left(S_{h}\right)\right| \leq \sigma(h) p_{h}+\pi \sigma^{2}(h) . \tag{20}
\end{equation*}
$

Поскольку периметр квадрата $Q_{h}$ равен $8 h$, то в силу первого свойства линейных отображений $p_{h} \leq 8 h\left|\left|\mathcal{D} F\left(\vec{u}_{0}\right)\right|\right|$. Так как отображение $F$ непрерывно дифференцируемо на компакте $\bar{G}$, то по теореме Вейерштрасса продолженные частные производные отображения $F$ ограничены на $\vec{G}$. Следовательно, матрица Якоби $\mathcal{D} F(\vec{u})$ ограничена на $G$, т. е. $\sup _{\vec{u}_{0} \in G}\left|\left|\mathcal{D} F\left(\vec{u}_{0}\right)\right|\right|=M \in \mathbb{R}$. Следовательно, $p_{h} \leq 8 M h$. Отсюда и из формул (16), (20) следует, что при $h \rightarrow+0$

$
\sup _{\vec{u}_{0}: Q_{h}\left(\vec{u}_{0}\right) \subset G}\left|\mu\left(F\left(Q_{h}\right)\right)-\mu\left(S_{h}\right)\right| / h^{2} \rightarrow 0 .
$

Замечая, что $\mu\left(Q_{h}\right)=4 h^{2}$, получаем при $h \rightarrow+0$

$
\sup _{\vec{u}_{0}: Q_{h}\left(\vec{u}_{0}\right) \subset G}\left|\frac{\mu\left(F\left(Q_{h}\right)\right)}{\mu\left(Q_{h}\right)}-\frac{\mu\left(S_{h}\right)}{\mu\left(Q_{h}\right)}\right| \longrightarrow 0 .
$

Отсюда и из равенства (11) следует доказываемое утверждение.
</block>
<block id='C14.5'>
## § 5. Замена переменных в кратном интеграле
</block>
<block id='L14.5.1'>
Лемма 1. Пусть $P$ - замкнутый квадрат, лежащий в $G$, стороны квадрата $P$ параллельны координатным осям. Пусть на множестве $F(P)$ задана непрерывная функция $f(x, y)$. Тогда

$
\iint_{F(P)} f(x, y) d x d y=\iint_{P} f(x(u, v), y(u, v))\left|\frac{\partial(x, y)}{\partial(u, v)}\right| d u d v
$
</block>
<block id='P14.5.1'>
Доказательство. Пусть $a_{0}$ - длина стороны квадрата $P$. Разобъем стороны квадрата $P$ на $k$ равных частей и получим разбиение
$\mathrm{T}=\left\{P_{i}^{k}\right\}_{i=1}^{k^{2}}$ квадрата $P$ на квадраты

$
P_{i}^{k}=\left[u_{i}^{k}-\frac{a_{0}}{2 k}, u_{i}^{k}+\frac{a_{0}}{2 k}\right] \times\left[v_{i}^{k}-\frac{a_{0}}{2 k}, v_{i}^{k}+\frac{a_{0}}{2 k}\right] .
$

Обозначим $\vec{u}_{i}^{k}=\binom{u_{i}^{k}}{v_{i}^{k}}$. Из теоремы $1 \S 4$ следует, что

$
\begin{equation*}
\max _{i \in\left\{1, \ldots, k^{2}\right\}}\left|\frac{\mu\left(F\left(P_{i}^{k}\right)\right)}{\mu\left(P_{i}^{k}\right)}-\left|J_{F}\left(\vec{u}_{i}^{k}\right)\right|\right| \longrightarrow 0 \quad \text { при } \quad k \rightarrow \infty . \tag{1}
\end{equation*}
$

В силу леммы $1 \S 4$ множества $F\left(P_{i}^{k}\right)$ и $F\left(P_{j}^{k}\right)$ при $i \neq j$ могут пересекаться лишь по границе. Рассмотрим разбиение $\widetilde{\mathrm{T}}=\left\{F\left(P_{i}^{k}\right)\right\}_{i=1}^{k^{2}}$ множества $F(P)$. Для разбиений Т и $\widetilde{\mathrm{T}}$ определим выборки $\xi_{\mathrm{T}}=$
$=\left\{\vec{u}_{i}^{k}\right\}_{i=1}^{k^{2}}$ и $\xi_{\widetilde{T}}=\left\{F\left(\vec{u}_{i}^{k}\right)\right\}_{i=1}^{k^{2}}$.

Заметим, что $\ell(\mathrm{T})=a_{0} \sqrt{2} / k$. Следовательно, $\ell(\mathrm{T}) \rightarrow 0$ при $k \rightarrow$ \rightarrow \infty$. Поскольку функция

$
g(u, v)=f(x(u, v), y(u, v))\left|\frac{\partial(x, y)}{\partial(u, v)}\right|
$

непрерывна на измеримом компакте $P$, то она интегрируема на этом компакте. Следовательно,

$
\begin{equation*}
\sigma\left(g ; \mathrm{T} ; \xi_{\mathrm{T}}\right) \longrightarrow \iint_{P} g(u, v) d u d v \quad \text { при } \quad k \rightarrow \infty \tag{2}
\end{equation*}
$

Из равномерной непрерывности отображения $F$ на компакте $P$ следует, что $\ell(\widetilde{\mathrm{T}}) \rightarrow 0$ при $k \rightarrow \infty$. Отсюда и из интегрируемости функции $f(x, y)$, непрерывной на измеримом компакте $F(P)$, получаем

$
\begin{equation*}
\sigma\left(f ; \widetilde{\mathrm{T}} ; \xi_{\widetilde{\mathrm{T}}}\right) \longrightarrow \iint_{F(P)} f(x, y) d x d y \quad \text { при } \quad k \rightarrow \infty \tag{3}
\end{equation*}
$

Обозначим $M=\max _{(x, y) \in F(P)}|f(x, y)|$. Тогда

$
\begin{aligned}
& \quad\left|\sigma\left(f ; \widetilde{\mathrm{T}} ; \xi_{\widetilde{\mathrm{T}}}\right)-\sigma\left(g ; \mathrm{T} ; \xi_{\mathrm{T}}\right)\right|= \\
& =\left|\sum_{i=1}^{k^{2}} f\left(F\left(\vec{u}_{i}^{k}\right)\right) \mu\left(F\left(P_{i}^{k}\right)\right)-\sum_{i=1}^{k^{2}} g\left(\vec{u}_{i}^{k}\right) \mu\left(P_{i}^{k}\right)\right|= \\
& =\left|\sum_{i=1}^{k^{2}} f\left(F\left(\vec{u}_{i}^{k}\right)\right)\left(\mu\left(F\left(P_{i}^{k}\right)\right)-\left|J_{F}\left(\vec{u}_{i}^{k}\right)\right| \mu\left(P_{i}^{k}\right)\right)\right| \leq \\
& \quad \leq M k^{2} \max _{i \in\left\{1, \ldots, k^{2}\right\}}\left|\mu\left(F\left(P_{i}^{k}\right)\right)-\left|J_{F}\left(\vec{u}_{i}^{k}\right)\right| \mu\left(P_{i}^{k}\right)\right| .
\end{aligned}
$

Замечая, что $\mu\left(P_{i}^{k}\right)=\left(a_{0} / k\right)^{2}$, получаем

$
\begin{gather*}
\left|\sigma\left(f ; \widetilde{\mathrm{T}} ; \xi_{\widetilde{\mathrm{T}}}\right)-\sigma\left(g ; \mathrm{T} ; \xi_{\mathrm{T}}\right)\right| \leq \\
\leq M a_{0}^{2} \max _{i \in\left\{1, \ldots, k^{2}\right\}}\left|\frac{\mu\left(F\left(P_{i}^{k}\right)\right)}{\mu\left(P_{i}^{k}\right)}-\left|J_{F}\left(\vec{u}_{i}^{k}\right)\right| \cdot\right. \tag{4}
\end{gather*}
$

Из формул (1), (4) получаем, что

$
\left|\sigma\left(f ; \widetilde{\mathrm{T}} ; \xi_{\widetilde{\mathrm{T}}}\right)-\sigma\left(g ; \mathrm{T} ; \xi_{\mathrm{T}}\right)\right| \longrightarrow 0 \quad \text { при } \quad k \rightarrow \infty,
$

откуда и из формул (2), (3) следует требуемое равенство.
</block>
<block id='T14.5.1'>
Теорема 1. (О замене переменных в кратном интеграле.) Пусть заданы отображение $F$

$
\mathbb{R}_{u v}^{2} \quad \supset \quad \underset{\substack{\text { откр. } \\ \text { измер. }}}{G} \quad \stackrel{F}{\rightleftarrows} \underset{\substack{G^{*} \\ \text { измер. }}}{G^{*} \text { кр. }} \subset \mathbb{R}_{x y}^{2}
$

со свойствами $1^{o}-3^{o}$ и функция $f(x, y)$, непрерывная в замыкании множества $G^{*}$. Тогда

$
\begin{equation*}
\iint_{G^{*}} f(x, y) d x d y=\iint_{G} f(x(u, v), y(u, v))\left|\frac{\partial(x, y)}{\partial(u, v)}\right| d u d v \tag{5}
\end{equation*}
$

Доказательство. Поскольку функции $f(x, y)$ и $g(u, v)=$ $=f(x(u, v), y(u, v))\left|\frac{\partial(x, y)}{\partial(u, v)}\right|$ непрерывны на измеримых компактах $\overline{G^{*}}$ и $\bar{G}$, то эти функции интегрируемы на них. Следовательно, функции $f$ и $g$ интегрируемы на измеримых подмножествах $G^{*} \subset \overline{G^{*}}, G \subset \bar{G}$. Поэтому интегралы в формуле (5) существуют.

Поскольку множество $G$ измеримо, то оно ограничено. Следовательно, существует замкнутый квадрат $Q^{0}: G \subset Q^{0}$. Разобъем стороны квадрата $Q^{0}$ на $k$ равных частей и получим разбиение $\left\{Q_{i}^{k}\right\}_{i=1}^{k^{2}}$ квадрата $Q^{0}$ на квадраты $Q_{i}^{k}$, не имеющие общих внутренних точек. Через $A_{k}$ обозначим клеточное множество, состоящее из тех квадратов $Q_{i}^{k}$, которые содержатся во множестве $G$ :

$
A_{k}=\bigcup_{i: Q_{i}^{k} \subset G} Q_{i}^{k}
$

Пусть $a_{0}$ - длина стороны квадрата $Q^{0}$. Тогда $\operatorname{diam}\left(Q_{i}^{k}\right)=$ $=a_{0} \sqrt{2} / k$. Заметим, что если точка $\vec{u}$ лежит во множестве $G \backslash A_{k}$, то $\vec{u} \in Q_{i}^{k}, Q_{i}^{k} \not \subset G$. Поэтому, как следует из леммы $3 \S 1$ главы 7 , $Q_{i}^{k} \bigcap \partial G \neq \emptyset$, а значит, $\vec{u} \in U_{\varepsilon_{k}}(\partial G)$, где $\varepsilon_{k}=\operatorname{diam}\left(Q_{i}^{k}\right)=a_{0} \sqrt{2} / k \rightarrow$ $\rightarrow 0$ при $k \rightarrow \infty$. Следовательно, $G \backslash A_{k} \subset U_{\varepsilon_{k}}(\partial G)$.

В силу измеримости множества $G$ справедливо равенство $\mu(\partial G)=0$. Поэтому, как следует из леммы 2 \S 1 главы 7, $\mu\left(U_{\varepsilon_{k}}(\partial G)\right) \rightarrow 0$ при $k \rightarrow \infty$. Следовательно,

$
\begin{equation*}
\mu\left(G \backslash A_{k}\right) \longrightarrow 0 \quad \text { при } \quad k \rightarrow \infty . \tag{6}
\end{equation*}
$

Так как отображение $F$ непрерывно на компакте $\bar{G}$, то оно равномерно непрерывно на $\bar{G}$. Отсюда и из условия $\lim _{k \rightarrow \infty} \varepsilon_{k}=0$ получаем, что для числовой последовательности

$
\sigma_{k}=\sup _{\substack{\vec{u}_{1} \in \bar{G}, \vec{u}_{2} \in \bar{G}: \\|\vec{u}_{1}-\vec{u}_{2}|<\varepsilon_{k}}}\|F\left(\vec{u}_{1}\right)-F\left(\vec{u}_{2}\right)\|
$

выполняется условие $\lim _{k \rightarrow \infty} \sigma_{k}=0$.
Поскольку $G \backslash A_{k} \subset U_{\varepsilon_{k}}(\partial G)$, то $F\left(G \backslash A_{k}\right) \subset U_{\sigma_{k}}(F(\partial G))$. В силу леммы $1 \S 4$ имеем $F(\partial G)=\partial F(G)=\partial G^{*}$. Отсюда и из критерия измеримости следует равенство $\mu(F(\partial G))=0$, что вместе с леммой $2 \S 1$ главы 7 дает соотношение $\mu\left(U_{\sigma_{k}}(F(\partial G)) \rightarrow 0\right.$ при $k \rightarrow \infty$. Следовательно, $\mu\left(F\left(G \backslash A_{k}\right)\right) \rightarrow 0$ при $k \rightarrow \infty$. Так как отображение $F$ взаимно однозначно, то $F\left(G \backslash A_{k}\right)=F(G) \backslash F\left(A_{k}\right)=G^{*} \backslash F\left(A_{k}\right)$. Поэтому

$
\begin{equation*}
\mu\left(G^{*} \backslash F\left(A_{k}\right)\right) \longrightarrow 0 \quad \text { при } \quad k \rightarrow \infty . \tag{7}
\end{equation*}
$

![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-043.jpg?height=468&width=1101&top_left_y=212&top_left_x=243)

В силу непрерывности функции $f$ на компакте $\overline{G^{*}}=\overline{F(G)}$ существует число $M=\max _{(x, y) \in \overline{G^{*}}}|f(x, y)|$. Отсюда и из (7) следует, что при $k \rightarrow \infty$

$
\left|\int_{G^{*} \backslash F\left(A_{k}\right)} f(x, y) d x d y\right| \leq M \mu\left(G^{*} \backslash F\left(A_{k}\right)\right) \longrightarrow 0
$

Используя аддитивность интеграла по множеству, получаем

$
\iint_{G^{*}} f(x, y) d x d y=\iint_{F\left(A_{k}\right)} f(x, y) d x d y+\int_{G^{*} \backslash F\left(A_{k}\right)} f(x, y) d x d y
$

поэтому

$
\begin{equation*}
\iint_{F\left(A_{k}\right)} f(x, y) d x d y \longrightarrow \iint_{G^{*}} f(x, y) d x d y \quad \text { при } \quad k \rightarrow \infty \tag{8}
\end{equation*}
$

Аналогично из непрерывности функции $g$ на компакте $\bar{G}$ и условия (6) следует, что

$
\begin{equation*}
\iint_{A_{k}} g(u, v) d u d v \longrightarrow \iint_{G} g(u, v) d u d v \quad \text { при } \quad k \rightarrow \infty \tag{9}
\end{equation*}
$

В силу леммы 1 и аддитивности интеграла получаем равенство

$
\begin{equation*}
\iint_{A_{k}} g(u, v) d u d v=\iint_{F\left(A_{k}\right)} f(x, y) d x d y \tag{10}
\end{equation*}
$

Из формул (8) - (10) следует требуемое равенство (5).
</block>
<block id='E14.5.1'>
Пример. Пусть в открытом круге $\Omega=\left\{(x, y) \in \mathbb{R}^{2}: x^{2}+\right.$ $\left.+y^{2}<r_{0}^{2}\right\}$ задана непрерывная функция $f(x, y)$, которая может быть непрерывно продолжена в замыкание круга $\Omega$. Для вычисления интеграла $\iint_{\Omega} f(x, y) d x d y$ часто удобно ввести полярные координаты:

$
r \geq 0, \quad \varphi \in[0,2 \pi], \quad x=r \cos \varphi, \quad y=r \sin \varphi .
$

Отображение $F(r, \varphi)=\binom{r \cos \varphi}{r \sin \varphi}$ непрерывно дифференцируемо, и его якобиан

$
J_{F}(r, \varphi)=\operatorname{det}\left(\begin{array}{ll}
x_{r}^{\prime} & x_{\varphi}^{\prime} \\
y_{r}^{\prime} & y_{\varphi}^{\prime}
\end{array}\right)=\operatorname{det}\left(\begin{array}{cc}
\cos \varphi & -r \sin \varphi \\
\sin \varphi & r \cos \varphi
\end{array}\right)=r .
$

Отображение $F: \mathbb{R}_{r \varphi}^{2} \rightarrow \mathbb{R}_{x y}^{2}$ не является взаимно однозначным, так как, например, точки ( $r, 0$ ) и ( $r, 2 \pi$ ) переходят в одну и ту же точку. Кроме того, $J_{F}(r, \varphi)=0$ при $r=0$. Чтобы удовлетворить требованиям взаимной однозначности и неравенства нулю якобиана, рассмотрим открытое измеримое множество

$
G=\left\{(r, \varphi): r \in\left(0, r_{0}\right), \varphi \in(0,2 \pi)\right\}
$

которое при отображении $F$ переходит во множество

$
G^{*}=\left\{(x, y):\left(0<x^{2}+y^{2}<r_{0}^{2}\right) \text { и }(y \neq 0 \text { при } x>0)\right\} .
$

В силу теоремы о замене переменных в кратном интеграле и теоремы о сведении кратного интеграла к повторному справедливы равенства

$
\begin{gathered}
\iint_{G^{*}} f(x, y) d x d y=\iint_{G} f(r \cos \varphi, r \sin \varphi) r d r d \varphi=\\
=\int_{0}^{r_{0}} r d r \int_{0}^{2 \pi} f(r \cos \varphi, r \sin \varphi) d \varphi
\end{gathered}
$

Поскольку круг $\Omega$ отличается от множества $G^{*}$ на множество меры нуль, а интеграл по множеству меры нуль равен нулю, то

$
\iint_{\Omega} f(x, y) d x d y=\iint_{G^{*}} f(x, y) d x d y
$

Таким образом, вычисление интеграла по кругу $\Omega$ сводится к вычислению повторного интеграла:

$
\iint_{x^{2}+y^{2}<r_{0}^{2}} f(x, y) d x d y=\int_{0}^{r_{0}} r d r \int_{0}^{2 \pi} f(r \cos \varphi, r \sin \varphi) d \varphi
$
</block>
<block id='T14.5.2'>
Теорема 2. Рассматривается пространство $\mathbb{R}_{x}^{n}$ точек $x=$ $=\left(x_{1}, \ldots, x_{n}\right)$ и пространство $\mathbb{R}_{u}^{n}$ точек $u=\left(u_{1}, \ldots, u_{n}\right)$. Пусть на замыкании открытого измеримого множества $G \subset \mathbb{R}_{u}^{n}$ задана векторфункция $F(u)=\left(\begin{array}{c}x_{1}\left(u_{1}, \ldots, u_{n}\right) \\ \ldots \\ x_{n}\left(u_{1}, \ldots, u_{n}\right)\end{array}\right)$, переводящая множество $G$ в открытое измеримое множество $G^{*} \subset \mathbb{R}_{x}^{n}$ и обладающая свойствами:
$1^{o}$. $F$ взаимно однозначно отображает $G$ в $G^{*}$;
$2^{o}$. отображение $F$ непрерывно дифференцируемо на $\bar{G}$;
$3^{o} . \quad J_{F}(u)=\operatorname{det}\left(\begin{array}{ccc}\frac{\partial x_{1}}{\partial u_{1}}(u) & \cdots & \frac{\partial x_{1}}{\partial u_{n}}(u) \\ \cdots & \cdots & \cdots \\ \frac{\partial x_{n}}{\partial u_{1}}(u) & \cdots & \frac{\partial x_{n}}{\partial u_{n}}(u)\end{array}\right) \neq 0$ для любых $u \in G$.
Пусть функция $f: \overline{G^{*}} \rightarrow \mathbb{R}$ непрерывна. Тогда

$
\int \cdots \int f(x) d x_{1} \cdots d x_{n}=\int \cdots \int f(F(u))\left|J_{F}(u)\right| d u_{1} \cdots d u_{n}
$
</block>
<block id='C14.6'>
## § 6. Геометрический смысл знака якобиана отображения
</block>
<block id='D14.6.1'>
Напомним, что кривая $\Gamma \subset \mathbb{R}^{n}$ называется гладкой, если возможна ее натуральная параметризация $\Gamma=\{\vec{\varrho}(s): s \in[0,|\Gamma|]\}$ и векторфункция $\vec{\varrho}(s)$ непрерывно дифференцируема на отрезке $[0,|\Gamma|]$. При этом $\left|\vec{\varrho}^{\prime}(s)\right|=1 \quad \forall s \in[0,|\Gamma|]$.

В главе 5 было показано, что если вектор-функция $\vec{r}(t)$ непрерывно дифференцируема и не имеет особых точек, т. е. $\vec{r}^{\prime}(t) \neq \overline{0} \quad \forall t \in$ $\in[a, b]$, то кривая $\Gamma=\{\vec{r}(t): t \in[a, b]\}$ - гладкая.
</block>
<block id='D14.6.2'>
Определение. Пусть заданы два неколлинеарных вектора на плоскости: $\vec{x}=\binom{x_{1}}{x_{2}}$ и $\vec{y}=\binom{y_{1}}{y_{2}}$. Будем говорить, что пара векторов $\vec{x}, \vec{y}$ - правая, если кратчайший поворот от направления вектора $\vec{x}$ к направлению вектора $\vec{y}$ производится против часовой стрелки; иначе пара $\vec{x}, \vec{y}$ называется левой. Из аналитической геометрии известно, что в правой системе координат в случае $\operatorname{det}\left(\begin{array}{ll}x_{1} & y_{1} \\ x_{2} & y_{2}\end{array}\right)>0$ пара векторов $\vec{x}, \vec{y}$ - правая, а в случае $\operatorname{det}\left(\begin{array}{ll}x_{1} & y_{1} \\ x_{2} & y_{2}\end{array}\right)<0$ - левая.
</block>
<block id='D14.6.3'>Определение. Пусть плоские кривые $\Gamma_{1}$ и $\Gamma_{2}$ пересекаются в точке $\vec{r}_{0}$. Пусть $\vec{\tau}_{1}, \vec{\tau}_{2}$ - векторы касательных к кривым $\Gamma_{1}, \Gamma_{2}$ в точке $\vec{r}_{0}$, направленные в соответствии с ориентацией кривых $\Gamma_{1}$, $\Gamma_{2}$. Будем говорить, что кривые $\Gamma_{1}, \Gamma_{2}$ составляют правую (левую) napy в точке $\vec{r}_{0}$, если векторы $\vec{\tau}_{1}, \vec{\tau}_{2}$ составляют правую (левую) пару.</block>
<block id='L14.6.1'>
Лемма 1. Пусть кривые $\Gamma_{1}$ и $\Gamma_{2}$ лежат в области $\Omega \subset \mathbb{R}_{u v}^{2}$ и составляют правую пару в точке $\binom{u_{0}}{v_{0}}$. Пусть в области $\Omega$ задана непрерывно дифференцируемая вектор-функция $F(u, v)=\binom{x(u, v)}{y(u, v)}$ с неравным нулю якобианом. Пусть $F\left(\Gamma_{1}\right), F\left(\Gamma_{2}\right)$ - образы кривых $\Gamma_{1}, \Gamma_{2}$ при отображении $F$, ориентированные в соответствии с ориентацией кривых $\Gamma_{1}, \Gamma_{2}$.

Тогда в случае $J_{F}\left(u_{0}, v_{0}\right)>0$ кривые $F\left(\Gamma_{1}\right), F\left(\Gamma_{2}\right)$ составляют правую пару в точке $\binom{x_{0}}{y_{0}}=\binom{x\left(u_{0}, v_{0}\right)}{y\left(u_{0}, v_{0}\right)}$, а в случае $J_{F}\left(u_{0}, v_{0}\right)<0$ - левую пару.
![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-046.jpg?height=272&width=322&top_left_y=1582&top_left_x=319)

$
\begin{gathered}
F \\
J_{F}\left(u_{0}, v_{0}\right)>0
\end{gathered}
$

![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-046.jpg?height=278&width=320&top_left_y=1577&top_left_x=944)

Доказательство. Поскольку кривые $\Gamma_{1}, \Gamma_{2}$ имеют касательную в точке $\vec{r}_{0}=\binom{u_{0}}{v_{0}}$, то эти кривые могут быть заданы векторфункциями $\vec{r}_{i}(t)=\binom{u_{i}(t)}{v_{i}(t)}$, дифференцируемыми в точке $t_{0}$, где $\vec{r}_{1}\left(t_{0}\right)=\vec{r}_{2}\left(t_{0}\right)=\vec{r}_{0}$, причем $\vec{r}_{i}^{\prime}\left(t_{0}\right) \neq \overline{0}, i=1,2$. Так как кривые $\Gamma_{1}$, $\Gamma_{2}$ составляют в точке $\vec{r}_{0}$ правую пару, то пара векторов $\vec{r}_{1}^{\prime}\left(t_{0}\right), \vec{r}_{2}^{\prime}\left(t_{0}\right)$ - правая, т. е.

$
\operatorname{det}\left(\begin{array}{ll}
u_{1}^{\prime}\left(t_{0}\right) & v_{1}^{\prime}\left(t_{0}\right)  \tag{1}\\
u_{2}^{\prime}\left(t_{0}\right) & v_{2}^{\prime}\left(t_{0}\right)
\end{array}\right)>0 .
$

Кривые $F\left(\Gamma_{i}\right)$ могут быть заданы вектор-функциями $\vec{R}_{i}(t)=$ $=\binom{x_{i}(t)}{y_{i}(t)}=F\left(\vec{r}_{i}(t)\right), i=1,2$.

В силу теоремы о дифференцировании сложной вектор-функции $\vec{R}_{i}^{\prime}\left(t_{0}\right)=\mathcal{D} F\left(\vec{r}_{0}\right) \vec{r}_{i}^{\prime}\left(t_{0}\right)$, следовательно,

$
\left(\begin{array}{ll}
x_{1}^{\prime}\left(t_{0}\right) & x_{2}^{\prime}\left(t_{0}\right) \\
y_{1}^{\prime}\left(t_{0}\right) & y_{2}^{\prime}\left(t_{0}\right)
\end{array}\right)=\mathcal{D} F\left(\vec{r}_{0}\right)\left(\begin{array}{ll}
u_{1}^{\prime}\left(t_{0}\right) & u_{2}^{\prime}\left(t_{0}\right) \\
v_{1}^{\prime}\left(t_{0}\right) & v_{2}^{\prime}\left(t_{0}\right)
\end{array}\right)
$

поэтому

$
\operatorname{det}\left(\begin{array}{cc}
x_{1}^{\prime}\left(t_{0}\right) & x_{2}^{\prime}\left(t_{0}\right)  \tag{2}\\
y_{1}^{\prime}\left(t_{0}\right) & y_{2}^{\prime}\left(t_{0}\right)
\end{array}\right)=J_{F}\left(u_{0}, v_{0}\right) \operatorname{det}\left(\begin{array}{cc}
u_{1}^{\prime}\left(t_{0}\right) & u_{2}^{\prime}\left(t_{0}\right) \\
v_{1}^{\prime}\left(t_{0}\right) & v_{2}^{\prime}\left(t_{0}\right)
\end{array}\right) .
$

Из формул (1), (2) следует, что при $J_{F}\left(u_{0}, v_{0}\right)>0$ пара векторов $\vec{R}_{1}^{\prime}\left(t_{0}\right), \vec{R}_{2}^{\prime}\left(t_{0}\right)$ - правая, т. е. кривые $F\left(\Gamma_{1}\right), F\left(\Gamma_{2}\right)$ составляют правую пару в точке $\binom{x_{0}}{y_{0}}=F\left(\vec{r}_{0}\right)$, а при $J_{F}\left(u_{0}, v_{0}\right)<0$ - левую пару в этой точке.
</block>
<block id='D14.6.4'>
Определение. Пусть простая замкнутая кусочно-гладкая кривая $\Gamma=\{\vec{r}(t): t \in[a, b]\}$ лежит на границе области $G \subset \mathbb{R}^{2}$. Пусть $\vec{r}_{0}=\vec{r}\left(t_{0}\right)$ - точка гладкости кривой $\Gamma$, т. е. существует $\vec{r}^{\prime}\left(t_{0}\right) \neq \overline{0}$. Будем говорить, что вектор $\vec{n}\left(t_{0}\right) \in \mathbb{R}^{2}$ является вектором внутренней нормали к границе области $G$ в точке $\vec{r}_{0}$, если

1) $\vec{n}\left(t_{0}\right) \perp \vec{r}^{\prime}\left(t_{0}\right)$ и
2) $\exists \delta_{0}>0: \forall \delta \in\left(0, \delta_{0}\right) \hookrightarrow \vec{r}_{0}+\delta \vec{n}\left(t_{0}\right) \in G$.
</block>
<block id='D14.6.5'>
Определение. Будем говорить, что простая замкнутая кусочногладкая кривая $\Gamma=\{\vec{r}(t): t \in[a, b]\}$, лежащая на границе области
$G \subset \mathbb{R}^{2}$, ориентирована положительно относительно области $G$, и писать $\Gamma^{+}$, если в каждой точке $\vec{r}\left(t_{0}\right)$ гладкости кривой $\Gamma$ пара, составленная из вектора касательной $\vec{r}^{\prime}\left(t_{0}\right)$ и вектора внутренней нормали $\vec{n}\left(t_{0}\right)$ является правой. Ориентацию кривой $\Gamma$, противоположную положительной, будем называть отрицательной ориентацией и писать в этом случае $\Gamma^{-}$.

Менее аккуратно можно сказать, что кривая $\Gamma$ ориентирована положительно (отрицательно) относительно области $G$, если при обходе кривой Г в направлении ее ориентации область $G$ остается слева (справа).
</block>
<block id='T14.6.1'>
Теорема 1. (Геометрический смысл знака якобиана отображения.) Пусть простая замкнутая кусочно-гладкая кривая $\Gamma^{+}$лежит на границе области $G \subset \mathbb{R}^{2}$ и ориентирована положительно относительно области $G$. Пусть в области $\Omega$, содержащей кривую $\Gamma^{+}$, определена непрерывно дифференцируемая вектор-функция $F(u, v)=$ $=\binom{x(u, v)}{y(u, v)}$, задающая взаимно однозначное отображение $F: G \rightarrow$ $\rightarrow F(G)$ с неравным нулю якобианом. Пусть кривая $F\left(\Gamma^{+}\right)$- образ кривой $\Gamma^{+}$при отображении $F$, ориентирована в соответствии с ориентацией кривой $\Gamma^{+}$.

Тогда в случае $J_{F}(u, v)>0 \quad \forall(u, v) \in \Omega$ кривая $F\left(\Gamma^{+}\right)$ориентирована положительно относительно области $F(G)$, а в случае $J_{F}(u, v)<$
$<0 \quad \forall(u, v) \in \Omega$ - отрицательно. Других случаев не бывает.

Доказательство. Пусть $\Gamma^{+}=\left\{\vec{r}_{1}(t): t \in[a, b]\right\}$. Зафиксируем произвольную точку $\vec{r}_{0}=\vec{r}_{1}\left(t_{0}\right)$ на кривой $\Gamma^{+}$. Пусть $\vec{n}_{0}$ - вектор внутренней нормали к границе области $G$ в точке $\vec{r}_{0}$. Тогда $\exists \delta_{0}>$
$>0: \forall \delta \in\left(0, \delta_{0}\right) \hookrightarrow \vec{r}_{0}+\delta \vec{n}\left(t_{0}\right) \in G$. Из положительной ориентации кривой $\Gamma^{+}$следует, что кривые $\Gamma^{+}, \Gamma_{0}=\left\{\vec{r}_{2}(t)=\vec{r}_{0}+\left(t-t_{0}\right) \vec{n}_{0}: t \in$
$\in\left[t_{0}, t_{0}+\delta_{0}\right]\right\}$ образуют правую пару в точке $\vec{r}_{0}$.

Пусть якобиан отображения $F$ положителен. В силу леммы 1 кривые $F\left(\Gamma^{+}\right)=\left\{\vec{R}_{1}(t)=F\left(\vec{r}_{1}(t)\right) \quad : \quad t \in[a, b]\right\}$ и $F\left(\Gamma_{0}\right)=\left\{\vec{R}_{2}(t)=$
$=F\left(\vec{r}_{2}(t)\right): t \in\left[t_{0}, t_{0}+\delta_{0}\right]\right\}$ образуют правую пару в точке $\vec{R}_{0}=$
$=F\left(\vec{r}_{0}\right)$, т. е. пара векторов $\vec{R}_{1}^{\prime}\left(t_{0}\right), \vec{R}_{2}^{\prime}\left(t_{0}\right)$ - правая. Поскольку $\forall \delta \in$
$\in\left(0, \delta_{0}\right) \hookrightarrow \vec{R}_{2}\left(t_{0}+\delta\right) \in F(G)$, то вектор касательной $\vec{R}_{2}^{\prime}\left(t_{0}\right)$ направлен в сторону области $F(G)$. Отсюда следует, что вектор касательной $\vec{R}_{1}^{\prime}\left(t_{0}\right)$ и вектор внутренней нормали к границе области $F(G)$ в точке $\vec{R}_{0}=F\left(\vec{r}_{0}\right)$ составляют правую пару. Поскольку выбором точки $\vec{r}_{0}$

на кривой $\Gamma^{+}$можно получить любую точку $\vec{R}_{0}=F\left(\vec{r}_{0}\right)$ на кривой $F\left(\Gamma^{+}\right)$, то кривая $F\left(\Gamma^{+}\right)$ориентирована положительно относительно области $F(G)$. Аналогично в случае отрицательного якобиана, кривая $F\left(\Gamma^{+}\right)$ориентирована отрицательно относительно области $F(G)$.

Покажем, что других случаев не бывает. Если якобиан $J_{F}(u, v)$ принимает в области $\Omega$ значения различных знаков, то по теореме о промежуточном значении для функции многих переменных, непрерывной на связном множестве, якобиан $J_{F}(u, v)$ должен обращаться в нуль в некоторой точке области $\Omega$, что противоречит условиям теоремы.
</block>
<block id='C14.7'>
## § 7. Формула Грина
</block>
<block id='D14.7.1'>
Напомним определение криволинейного интеграла второго рода, введенного в §7 главы 7. Пусть кривая $\Gamma=\left\{\vec{r}(t) \in \mathbb{R}^{n}: t \in\right.$ $[a, b]$\}\}
задана непрерывной вектор-функцией $\vec{r}(t)$, имеющей кусочнонепрерывную производную, а вектор-функция $\vec{f}(\vec{r}) \in \mathbb{R}^{n}$ непрерывна на множестве Г. Криволинейный интеграл второго рода функции $\vec{f}(\vec{r})$ по кривой Г определяется формулой

$
\begin{equation*}
\int_{\Gamma}(\vec{f}(\vec{r}), d \vec{r})=\int_{a}^{b}\left(\vec{f}(\vec{r}(t)), \vec{r}^{\prime}(t)\right) d t \tag{1}
\end{equation*}
$

Выражение, записанное в левой части этой формулы является обозначением криволинейного интеграла второго рода, а в правой части данной формулы записан интеграл Римана скалярной функции $\varphi(t)=$
$=\left(\vec{f}(\vec{r}(t)), \vec{r}^{\prime}(t)\right)$ по отрезку $[a, b]$. Здесь через $\left(\vec{f}(\vec{r}(t)), \vec{r}^{\prime}(t)\right)$ обозначено скалярное произведение векторов $\vec{f}(\vec{r}(t))$ и $\vec{r}^{\prime}(t)$.
</block>
<block id='R14.7.1'>
Как было доказано ранее, криволинейный интеграл второго рода не зависит от параметризации, а при изменении ориентации кривой меняет знак. Отметим, что из свойства аддитивности интеграла Римана по отрезку и формулы (1) следует свойство аддитивности криволинейного интеграла по кривой:
если кривая $\Gamma$ составлена из кривых $\Gamma_{1}, \ldots, \Gamma_{k}$, ориентированных в соответствии с ориентацией кривой $\Gamma$, то

$
\int_{\Gamma}(\vec{f}(\vec{r}), d \vec{r})=\sum_{i=1}^{k} \int_{\Gamma_{i}}(\vec{f}(\vec{r}), d \vec{r})
$
</block>
<block id='TX14.7.1'>
Для криволинейного интеграла по плоской кривой $\Gamma=$
$=\left\{\binom{x(t)}{y(t)}: t \in[a, b]\right\}$ от вектор-функции $\vec{f}(x, y)=\binom{P(x, y)}{Q(x, y)}$ формула (1) принимает вид

$
\begin{gathered}
\int_{\Gamma} P(x, y) d x+Q(x, y) d y= \\
=\int_{a}^{b}\left(P(x(t), y(t)) x^{\prime}(t)+Q(x(t), y(t)) y^{\prime}(t)\right) d t
\end{gathered}
$
</block>
<block id='TX14.7.2'>
В частности, если кривая Г является графиком функции $y(x)$, непрерывно дифференцируемой на отрезке $[a, b]$, то

$
\begin{equation*}
\int_{\Gamma} P(x, y) d x=\int_{a}^{b} P(x, y(x)) d x \tag{2}
\end{equation*}
$

Заметим, что для существования интеграла $\int_{a}^{b} P(x, y(x)) d x$ достаточно требовать непрерывность функции $y(x)$ на $[a, b]$ и непрерывность функции $P(x, y)$ на множестве $\Gamma=\{(x, y(x)): \quad x \in[a, b]\}$. Поэтому в случае, когда кривая $\Gamma$ является графиком непрерывной (а не обязательно непрерывно дифференцируемой) функции, криволинейный интеграл $\int_{\Gamma} P(x, y) d x$ будем понимать в смысле формулы (2). Как показано выше, в случае непрерывной дифференцируемости функции $y(x)$ это определение совпадает с общим определением криволинейного интеграла второго рода.

Аналогично, если кривая $\Gamma=\{(x(y), y): y \in[c, d]\}$ является графиком функции $x(y)$, непрерывной на отрезке $[c, d]$, а функция $Q(x, y)$ непрерывна на множестве $\Gamma$, то определим

$
\int_{\Gamma} Q(x, y) d y=\int_{c}^{d} Q(x(y), y) d y
$
</block>
<block id='D14.7.2'>
Определение. Будем говорить, что область $G \subset \mathbb{R}^{2}$ элементарна, если она элементарна относительно каждой из координатных осей, т. е. существуют функции $\varphi(x)$, $\psi(x)$, непрерывные на $[a, b]$, и функции $\alpha(y), \beta(y)$, непрерывные на $[c, d]$, такие, что

$
\begin{array}{ll}
\varphi(x)<\psi(x) & \forall x \in(a, b) \\
\alpha(y)<\beta(y) & \forall y \in(c, d)
\end{array}
$

![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-051.jpg?height=453&width=445&top_left_y=248&top_left_x=890)

и

$
\begin{aligned}
G & =\{(x, y): x \in(a, b), \varphi(x)<y<\psi(x)\} = \\
& =\{(x, y): y \in(c, d), \alpha(y)<x<\beta(y)\}
\end{aligned}
$
</block>
<block id='T14.7.1'>
Теорема 1. Пусть область $G \subset \mathbb{R}^{2}$ элементарна и ее границей является кусочно-гладкая кривая $\partial G^{+}$, ориентированная положительно относительно области $G$. Пусть в замыкании области $G$ заданы непрерывно дифференцируемые функции $P(x, y)$ и $Q(x, y)$. Тогда справедлива формула Грина:

$
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
$

Доказательство. Докажем сначала формулу

$
\begin{equation*}
\int_{\partial G^{+}} P(x, y) d x=-\iint_{G} \frac{\partial P}{\partial y}(x, y) d x d y \tag{3}
\end{equation*}
$

Разобъем кривую $\partial G^{+}$на кривые

$
\begin{aligned}
& \Gamma_{1}=\{(x, \varphi(x)): x \in[a, b]\}, \\
& \Gamma_{2}=\{(b, y): y \in[\varphi(b), \psi(b)]\}, \\
& \Gamma_{3}=\{(x, \psi(x)): x \in[a, b]\}, \\
& \Gamma_{4}=\{(a, y): y \in[\varphi(a), \psi(a)]\} .
\end{aligned}
$

![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-051.jpg?height=423&width=534&top_left_y=1452&top_left_x=809)

Поскольку координата $x$ на отрезках $\Gamma_{2}$ и $\Gamma_{4}$ не меняется, то криволинейные интегралы $\int P(x, y) d x$ по этим кривым равны нулю. Кривая $\Gamma_{1}$ имеет ориентацию, соответствующую ориентации кривой $\partial G^{+}$, а кривая $\Gamma_{3}$ - противоположную ориентацию. Следовательно, в силу аддитивности криволинейного интеграла

$
\begin{gathered}
\quad \int_{\partial G^{+}} P(x, y) d x=\int_{\Gamma_{1}} P(x, y) d x-\int_{\Gamma_{3}} P(x, y) d x= \\
=\int_{a}^{b} P(x, \varphi(x)) d x-\int_{a}^{b} P(x, \psi(x)) d x=-\int_{a}^{b}(P(x, \psi(x))-P(x, \varphi(x))) d x
\end{gathered}
$

Из формулы Ньютона-Лейбница следует, что

$
P(x, \psi(x))-P(x, \varphi(x))=\int_{\varphi(x)}^{\psi(x)} \frac{\partial P}{\partial y}(x, y) d y
$

Отсюда и из теоремы о сведении кратного интеграла к повторному получаем

$
\int_{\partial G^{+}} P(x, y) d x=-\int_{a}^{b} d x \int_{\varphi(x)}^{\psi(x)} \frac{\partial P}{\partial y}(x, y) d y=-\iint_{G} \frac{\partial P}{\partial y}(x, y) d x d y
$

Формула

$
\begin{equation*}
\int_{\partial G^{+}} Q(x, y) d y=\iint_{G} \frac{\partial Q}{\partial x}(x, y) d x d y \tag{4}
\end{equation*}
$

доказывается аналогично. Складывая формулы (3) и (4), получаем формулу Грина.
</block>
<block id='T14.7.2'>
Теорема 2. Пусть

1) область $G \subset \mathbb{R}^{2}$ может быть представлена как объединение конечного числа непересекающихся элементарных областей $G_{i}(i=$
$=1, \ldots, I)$ с кусочно-гладкими границами и кривых $\gamma_{j}(j=1, \ldots, J)$, лежащих на внутренних (по отношению к области $G$ ) границах областей $G_{i}$;
2) граница $\partial G^{+}$области $G$ состоит из конечного числа простых замкнутых кусочно-гладких кривых $\Gamma_{k}^{+}(k=1, \ldots, K)$, ориентированных положительно относительно области $G$;
3) пусть функции $P(x, y), Q(x, y)$ непрерывно дифференцируемы на замыкании области $G$.

Тогда справедлива формула Грина:

$
\begin{equation*}
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y \tag{5}
\end{equation*}
$

где

$
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\sum_{k=1}^{K} \int_{\Gamma_{k}^{+}} P(x, y) d x+Q(x, y) d y
$

Доказательство. Применяя теорему 1 к элементарным областям $G_{i}$, из которых состоит область $G$, получаем

$
\int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G_{i}}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
$

Поскольку кусочно-гладкие кривые $\gamma_{j}$, лежащие на внутренних границах областей $G_{i}$, имеют меру нуль, то кратный интеграл по внутренним границам областей $G_{i}$ равен нулю. Следовательно, в силу аддитивности кратного интеграла

$
\begin{align*}
& \sum_{i=1}^{I} \int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=  \tag{6}\\
= & \iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
\end{align*}
$

Заметим, что если кривая $\gamma_{j}$ лежит на границе соседних областей $G_{i}$ и $G_{\ell}$, то положительная ориентация этой кривой относительно области $G_{i}$ противоположна положительной ориентации этой же кривой относительно области $G_{\ell}$.
![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-054.jpg?height=483&width=477&top_left_y=221&top_left_x=244)

Следовательно, интегралы по кривой $\gamma_{j}$ войдут в слагаемые $\underset{\partial G_{i}^{+}}{\int} P(x, y) d x+Q(x, y) d y$ и $\int P(x, y) d x+Q(x, y) d y$ с раз$\partial G_{\ell}^{+}$
ными знаками и при суммировании взаимно уничтожатся. В результате в левой части формулы $(6)$ останутся только интегралы по кривым, лежащим на границе области $G$, что дает формулу (5).
</block>
<block id='T14.7.2'>
Теорема 2. Пусть

1) область $G \subset \mathbb{R}^{2}$ может быть представлена как объединение конечного числа непересекающихся элементарных областей $G_{i}(i=$
$=1, \ldots, I)$ с кусочно-гладкими границами и кривых $\gamma_{j}(j=1, \ldots, J)$, лежащих на внутренних (по отношению к области $G$ ) границах областей $G_{i}$;
2) граница $\partial G^{+}$области $G$ состоит из конечного числа простых замкнутых кусочно-гладких кривых $\Gamma_{k}^{+}(k=1, \ldots, K)$, ориентированных положительно относительно области $G$;
3) пусть функции $P(x, y), Q(x, y)$ непрерывно дифференцируемы на замыкании области $G$.

Тогда справедлива формула Грина:

$
\begin{equation*}
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y \tag{5}
\end{equation*}
$

где

$
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\sum_{k=1}^{K} \int_{\Gamma_{k}^{+}} P(x, y) d x+Q(x, y) d y
$

Доказательство. Применяя теорему 1 к элементарным областям $G_{i}$, из которых состоит область $G$, получаем

$
\int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G_{i}}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
$

Поскольку кусочно-гладкие кривые $\gamma_{j}$, лежащие на внутренних границах областей $G_{i}$, имеют меру нуль, то кратный интеграл по внутренним границам областей $G_{i}$ равен нулю. Следовательно, в силу аддитивности кратного интеграла

$
\begin{align*}
& \sum_{i=1}^{I} \int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=  \tag{6}\\
= & \iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
\end{align*}
$

Заметим, что если кривая $\gamma_{j}$ лежит на границе соседних областей $G_{i}$ и $G_{\ell}$, то положительная ориентация этой кривой относительно области $G_{i}$ противоположна положительной ориентации этой же кривой относительно области $G_{\ell}$.
![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-054.jpg?height=483&width=477&top_left_y=221&top_left_x=244)

Следовательно, интегралы по кривой $\gamma_{j}$ войдут в слагаемые $\underset{\partial G_{i}^{+}}{\int} P(x, y) d x+Q(x, y) d y$ и $\int P(x, y) d x+Q(x, y) d y$ с раз$\partial G_{\ell}^{+}$
ными знаками и при суммировании взаимно уничтожатся. В результате в левой части формулы $(6)$ останутся только интегралы по кривым, лежащим на границе области $G$, что дает формулу (5).
</block>
<block id='T14.7.2'>
Теорема 2. Пусть

1) область $G \subset \mathbb{R}^{2}$ может быть представлена как объединение конечного числа непересекающихся элементарных областей $G_{i}(i=$
$=1, \ldots, I)$ с кусочно-гладкими границами и кривых $\gamma_{j}(j=1, \ldots, J)$, лежащих на внутренних (по отношению к области $G$ ) границах областей $G_{i}$;
2) граница $\partial G^{+}$области $G$ состоит из конечного числа простых замкнутых кусочно-гладких кривых $\Gamma_{k}^{+}(k=1, \ldots, K)$, ориентированных положительно относительно области $G$;
3) пусть функции $P(x, y), Q(x, y)$ непрерывно дифференцируемы на замыкании области $G$.

Тогда справедлива формула Грина:

$
\begin{equation*}
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y \tag{5}
\end{equation*}
$

где

$
\int_{\partial G^{+}} P(x, y) d x+Q(x, y) d y=\sum_{k=1}^{K} \int_{\Gamma_{k}^{+}} P(x, y) d x+Q(x, y) d y
$

Доказательство. Применяя теорему 1 к элементарным областям $G_{i}$, из которых состоит область $G$, получаем

$
\int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=\iint_{G_{i}}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
$

Поскольку кусочно-гладкие кривые $\gamma_{j}$, лежащие на внутренних границах областей $G_{i}$, имеют меру нуль, то кратный интеграл по внутренним границам областей $G_{i}$ равен нулю. Следовательно, в силу аддитивности кратного интеграла

$
\begin{align*}
& \sum_{i=1}^{I} \int_{\partial G_{i}^{+}} P(x, y) d x+Q(x, y) d y=  \tag{6}\\
= & \iint_{G}\left(\frac{\partial Q}{\partial x}(x, y)-\frac{\partial P}{\partial y}(x, y)\right) d x d y
\end{align*}
$

Заметим, что если кривая $\gamma_{j}$ лежит на границе соседних областей $G_{i}$ и $G_{\ell}$, то положительная ориентация этой кривой относительно области $G_{i}$ противоположна положительной ориентации этой же кривой относительно области $G_{\ell}$.
![](https://cdn.mathpix.com/cropped/2025_07_20_130114880eb2e38b8671g-054.jpg?height=483&width=477&top_left_y=221&top_left_x=244)

Следовательно, интегралы по кривой $\gamma_{j}$ войдут в слагаемые $\underset{\partial G_{i}^{+}}{\int} P(x, y) d x+Q(x, y) d y$ и $\int P(x, y) d x+Q(x, y) d y$ с раз$\partial G_{\ell}^{+}$
ными знаками и при суммировании взаимно уничтожатся. В результате в левой части формулы $(6)$ останутся только интегралы по кривым, лежащим на границе области $G$, что дает формулу (5).
</block>
<block id='R13.2.1'>
Замечание. Применение метода множителей Лагранжа не требует разрешения ограничений. Однако доказательство теорем 1 и 2 основано на том, что в силу теоремы о неявной функции ограничения $g(x)=\overline{0}$ можно разрешить в некоторой окрестности точки $x^{0}$.
</block>
<block id='D13.2.3'>
Определение. Будем говорить, что в точке $x^{0}$ выполнены $y$ словия локальной разрешимости ограничений $g(x)=\overline{0}$, если

1) $g\left(x^{0}\right)=\overline{0}$;
2) вектор-функция $g(x)$ непрерывно дифференцируема в окрестности точки $x^{0}$;
3) векторы $\operatorname{grad} g_{1}\left(x^{0}\right), \cdots, \operatorname{grad} g_{m}\left(x^{0}\right)$ линейно независимы.\n</block>\n<block id='T13.2.3'>\nТретье из условий локальной разрешимости ограничений означает, что строки матрицы Якоби\n\n$ \n\mathcal{D} g\left(x^{0}\right)=\left(\begin{array}{ccc}\n\frac{\partial g_{1}}{\partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{1}}{\partial x_{n}}\left(x^{0}\right) \\ \n\cdots & \cdots & \cdots \\ \n\frac{\partial g_{m}}{\partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{m}}{\partial x_{n}}\left(x^{0}\right)\n\end{array}\right)\n$ \n\nлинейно независимы, т. е. $\operatorname{rang} \mathcal{D} g\left(x^{0}\right)=m$. Следовательно, существуют $m$ линейно независимых столбцов матрицы $\mathcal{D} g\left(x^{0}\right)$. Без ограничения общности будем считать, что первые $m$ столбцов матрицы $\mathcal{D} g\left(x^{0}\right)$ линейно независимы (если это не так, то можно перенумеровать переменные $x_{i}$ так, что это условие выполняется). Разобъем вектор $x=\left(\begin{array}{c}x_{1} \\ \ldots \\ x_{n}\end{array}\right)$ на два вектора: $y=\left(\begin{array}{c}x_{1} \\ \ldots \\ x_{m}\end{array}\right)$ и $z=\left(\begin{array}{c}x_{m+1} \\ \ldots \\ x_{n}\end{array}\right)$. Тогда\n\n$ \n\begin{gathered}\nx=\binom{y}{z}, \quad x^{0}=\binom{y^{0}}{z^{0}} \\ \nf(x)=f(y, z), \quad g(x)=g(y, z), \quad L(x, \lambda)=L(y, z, \lambda)\n\end{gathered}\n$ \n\nБудем обозначать\n\n$ \n\begin{aligned}\nf_{y}^{\prime}\left(y^{0}, z^{0}\right) & =\left(\frac{\partial f}{\partial x_{1}}\left(x^{0}\right) \cdots \frac{\partial f}{\partial x_{m}}\left(x^{0}\right)\right) \\ \nf_{z}^{\prime}\left(y^{0}, z^{0}\right) & =\left(\frac{\partial f}{\partial x_{m+1}}\left(x^{0}\right) \cdots \frac{\partial f}{\partial x_{n}}\left(x^{0}\right)\right) \\ \ng_{y}^{\prime}\left(y^{0}, z^{0}\right) & =\left(\begin{array}{ccc}\n\frac{\partial g_{1}}{\partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{1}}{\partial x_{m}}\left(x^{0}\right) \\ \n\cdots & \cdots & \cdots \\ \n\frac{\partial g_{m}}{\partial x_{1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{m}}{\partial x_{m}}\left(x^{0}\right)\n\end{array}\right) \\ \ng_{z}^{\prime}\left(y^{0}, z^{0}\right) & =\left(\begin{array}{ccc}\n\frac{\partial g_{1}}{\partial x_{m+1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{1}}{\partial x_{n}}\left(x^{0}\right) \\ \n\cdots & \cdots & \cdots \\ \n\frac{\partial g_{m}}{\partial x_{m+1}}\left(x^{0}\right) & \cdots & \frac{\partial g_{m}}{\partial x_{n}}\left(x^{0}\right)\n\end{array}\right)\n\end{aligned}\n$ \n\nПоскольку первые $m$ столбцов матрицы $\mathcal{D} g\left(x^{0}\right)$ линейно независимы, а они являются столбцами квадратной матрицы $g_{y}^{\prime}\left(y^{0}, z^{0}\right)$, то $\operatorname{det} g_{y}^{\prime}\left(y^{0}, z^{0}\right) \neq 0$.\n\nИз теоремы о неявной функции (глава $12, \S 4$, теорема 1) получаем следующую лемму.\n\nЛемма 1. Пусть в точке $x^{0}$ выполняются условия локальной разрешимости ограничений. Тогда существуют числа $\beta>0, \gamma>$ $>0$ и функция $\varphi(z)$, непрерывно дифференцируемая в $U_{\beta}\left(z^{0}\right)$, такие, что при $z \in U_{\beta}\left(z^{0}\right), y \in U_{\gamma}\left(y^{0}\right)$ системы $g(y, z)=\overline{0}$ и $y=\varphi(z)$ эквивалентны.\n\nПри этом точка $x^{0}=\binom{y^{0}}{z^{0}}$ является локальным минимумом (максимумом) в задаче (1) тогда и только тогда, когда $z^{0}$ является точкой безусловного локального минимума (максимума) функции $F(z)=f(\varphi(z), z)$.\n\nДоказательство теоремы 1. Из условий теоремы 1 следует, что в точке $x^{0}$ выполняются условия локальной разрешимости ограничений. В силу леммы 1 существует непрерывно дифференцируемая функция $\varphi(z)$ такая, что в окрестности точки $x^{0}=\binom{y^{0}}{z^{0}}$\n\n$ \ng(y, z)=\overline{0} \quad \Longleftrightarrow \quad y=\varphi(z) .\n$ \n\nТребуется доказать, что существует вектор $\lambda^{0} \in \mathbb{R}^{n}$ такой, что точка $\left(\begin{array}{l}y^{0} \\ z^{0} \\ \lambda^{0}\end{array}\right)$ является стационарной точкой функции Лагранжа $L(x, \lambda)=$ $=f(x)+\lambda^{T} g(x)$, т. е.\n\n$ \n\left\{\begin{array}{l}\nL_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0} \\ \nL_{z}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0} \\ \nL_{\lambda}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}\n\end{array}\right.\n$ \n\nПоскольку точка $x^{0}=\binom{y^{0}}{z^{0}}$ удовлетворяет ограничениям $g(x)=$ $=\overline{0}$, то $L_{\lambda}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\left(g\left(x^{0}\right)\right)^{T}=\overline{0}$. Следовательно, уравнение $L_{\lambda}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$ выполнено автоматически.\n\nОпределим вектор $\lambda^{0}$ из уравнения $L_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$ : $L_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=f_{y}^{\prime}\left(y^{0}, z^{0}\right)+\left(\lambda^{0}\right)^{T} g_{y}^{\prime}\left(y^{0}, z^{0}\right)=\overline{0}$. Поскольку $\operatorname{det} g_{y}^{\prime}\left(y^{0}, z^{0}\right) \neq 0$, то существует матрица $\left(g_{y}^{\prime}\left(y^{0}, z^{0}\right)\right)^{-1}$, и вектор $\lambda^{0}$ можно определить по формуле\n\n$ \n\left(\lambda^{0}\right)^{T}=-f_{y}^{\prime}\left(y^{0}, z^{0}\right)\left(g_{y}^{\prime}\left(y^{0}, z^{0}\right)\right)^{-1}\n$ \n\nОсталось показать, что выполняется равенство $L_{z}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$.\nПо условию теоремы 1 точка $x^{0}$ доставляет локальный экстремум в задаче (1). Отсюда и из леммы 1 следует, что $z^{0}$ - точка локального безусловного экстремума функции $F(z)=f(\varphi(z), z)$. Поскольку $y=\varphi(z)$ - это решение уравнения $g(y, z)=\overline{0}$, то $g(\varphi(z), z)=\overline{0}$,\n\nследовательно,\n\n$ \nF(z)=f(\varphi(z), z)+\left(\lambda^{0}\right)^{T} g(\varphi(z), z)=L\left(\varphi(z), z, \lambda^{0}\right) .\n$ \n\nИз теоремы 1 \S 1 следует, что $z^{0}$ - стационарная точка функции $F(z)$, т. е. $F_{z}^{\prime}\left(z^{0}\right)=\overline{0}$, а значит,\n\n$ \nL_{y}^{\prime}\left(\varphi\left(z^{0}\right), z^{0}, \lambda^{0}\right) \varphi_{z}^{\prime}\left(z^{0}\right)+L_{z}^{\prime}\left(\varphi\left(z^{0}\right), z^{0}, \lambda^{0}\right)=\overline{0}\n$ \n\nОтсюда и из условий $y^{0}=\varphi\left(z^{0}\right), L_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$ следует, что $L_{z}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$.\n\nДоказательство теоремы 2. Из условий теоремы 2 следует выполнение условий локальной разрешимости ограничений в точке $x^{0}$. В силу леммы 1 точка $x^{0}$ доставляет локальный минимум (максимум) в задаче (1) тогда и только тогда, когда точка $z^{0}$ доставляет безусловный локальный минимум (максимум) функции $F(z)=$ $=f(\varphi(z), z)$. Поскольку $g(\varphi(z), z)=\overline{0}$, то\n\n$ \n\begin{equation*}\nF(z)=f(\varphi(z), z)+\left(\lambda^{0}\right)^{T} g(\varphi(z), z)=L\left(\varphi(z), z, \lambda^{0}\right) . \tag{4}\n\end{equation*}\n$ \n\nСледовательно,\n\n$ \n\begin{aligned}\nF_{z}^{\prime}\left(z^{0}\right) & =L_{y}^{\prime}\left(\varphi\left(z^{0}\right), z^{0}, \lambda^{0}\right) \varphi_{z}^{\prime}\left(z^{0}\right)+L_{z}^{\prime}\left(\varphi\left(z^{0}\right), z^{0}, \lambda^{0}\right)= \\ \n& =L_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right) \varphi_{z}^{\prime}\left(z^{0}\right)+L_{z}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)\n\end{aligned}\n$ \n\nПоскольку $\left(\begin{array}{l}y^{0} \\ z^{0} \\ \lambda^{0}\end{array}\right)$ - стационарная точка функции Лагранжа, то $L_{y}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}, L_{z}^{\prime}\left(y^{0}, z^{0}, \lambda^{0}\right)=\overline{0}$, следовательно, $F_{z}^{\prime}\left(z^{0}\right)=\overline{0}$, т. е. $z^{0}$ - стационарная точка функции $F(z)$.\n\nСогласно теореме 2 \S 1 , наличие в точке $z^{0}$ экстремума функции $F(z)$, а значит, и наличие в точке $x^{0}$ экстремума в задаче (1), зависит от знакоопределенности квадратичной формы $d^{2} F\left(z^{0}\right)$.\n\nВ силу инвариантности формы первого дифференциала получаem\n\n$ \nd F(z)=L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y+L_{z}^{\prime}\left(y, z, \lambda^{0}\right) d z\n$ \n\nгде $y=\varphi(z), d z$ - приращение вектора независимых переменных $z$, а $d y=d \varphi(z)$. Найдем $d^{2} F\left(z^{0}\right)$ :\n\n$ \n\begin{gathered}\nd\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)=L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d^{2} y+\\ \n+\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)_{y}^{\prime} d y+\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)_{z}^{\prime} d z\n\end{gathered}\n$ \n\nПоскольку $L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y=\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)^{T}=(d y)^{T}\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right)\right)^{T}$, то $\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)_{y}^{\prime} \quad=\quad(d y)^{T} L_{y y}^{\prime \prime}\left(y, z, \lambda^{0}\right)$. Аналогично, $\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)_{z}^{\prime}=(d y)^{T} L_{y z}^{\prime \prime}\left(y, z, \lambda^{0}\right)$. Поэтому\n\n$ \n\begin{gathered}\nd\left(L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d y\right)=L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d^{2} y+\\ \n+(d y)^{T} L_{y y}^{\prime \prime}\left(y, z, \lambda^{0}\right) d y+(d y)^{T} L_{y z}^{\prime \prime}\left(y, z, \lambda^{0}\right) d z\n\end{gathered}\n$ \n\nАналогично, учитывая, что $d^{2} z=0$, получаем\n\n$ \nd\left(L_{z}^{\prime}\left(y, z, \lambda^{0}\right) d z\right)=(d z)^{T} L_{z z}^{\prime \prime}\left(y, z, \lambda^{0}\right) d z+(d z)^{T} L_{z y}^{\prime \prime}\left(y, z, \lambda^{0}\right) d y .\n$ \n\nСледовательно,\n\n$ \n\begin{gathered}\nd^{2} F(z)=L_{y}^{\prime}\left(y, z, \lambda^{0}\right) d^{2} y+(d y)^{T} L_{y y}^{\prime \prime}\left(y, z, \lambda^{0}\right) d y+\\ \n+2(d y)^{T} L_{y z}^{\prime \prime}\left(y, z, \lambda^{0}\right) d z+(d z)^{T} L_{z z}^{\prime \prime}\left(y, z, \lambda^{0}\right) d z=\\ \n=L_{y}^{\prime}\left(x, \lambda^{0}\right) d^{2} y+(d x)^{T} L_{x x}^{\prime \prime}\left(x, \lambda^{0}\right) d x\n\end{gathered}\n$ \n\nПоскольку $\left(\begin{array}{l}y^{0} \\ z^{0} \\ \lambda^{0}\end{array}\right)$ - стационарная точка функции Лагранжа, то $L_{y}^{\prime}\left(x^{0}, \lambda^{0}\right)=\overline{0}$, поэтому\n\n$ \nd^{2} F\left(z^{0}\right)=(d x)^{T} L_{x x}^{\prime \prime}\left(x^{0}, \lambda^{0}\right) d x=k(d x) .\n$ \n\nИз эквивалентности систем $g(y, z)=\overline{0}$ и $y=\varphi(z)$ следует эквивалентность систем $d g(x)=\overline{0}$ и $d y=d \varphi(z)$. Поскольку $d z \in \mathbb{R}^{n-m}$ - произвольный вектор, $d y=d \varphi\left(z^{0}\right)$, то $d x=\binom{d y}{d z}$ - произвольный вектор, удовлетворяющий системе $d g\left(x^{0}\right)=\overline{0}$, т. е. $d x$ - произвольный вектор из $E_{\text {кас }}$. Следовательно, знакоопределенность квадратичной формы $d^{2} F\left(z^{0}\right)=(d z)^{T} F_{z z}^{\prime \prime}\left(z^{0}\right) d z$ такая же, как и знакоопределенность квадратичной формы $k(d x)$ на подпространстве $E_{\text {кас }}$. Применение теоремы 2 \S 1 завершает доказательство теоремы 2 .\n</block>\n<block id='D13.2.3'>
Определение. Будем говорить, что в точке $x^{0}$ выполнены $y$ словия локальной разрешимости ограничений $g(x)=\overline{0}$, если

1) $g\left(x^{0}\right)=\overline{0}$;
2) вектор-функция $g(x)$ непрерывно дифференцируема в окрестности точки $x^{0}$;
3) векторы $\operatorname{grad} g_{1}\left(x^{0}\right), \cdots, \operatorname{grad} g_{m}\left(x^{0}\right)$ линейно независимы.
</block>
<block id='C14'>
## КРАТНЫЙ ИНТЕГРАЛ
</block>
<block id='R14.7.2'>
Замечание. Формула Грина справедлива и для области, которую нельзя представить как объединение конечного числа элементарных областей и частей их границ, т. е. вместо условия (1) теоремы 2 достаточно требовать измеримость области $G$. Доказательство соответствующей теоремы довольно трудоемко, и мы его приводить не будем. Тем более что в практических задачах области, не удовлетворяющие условию (1) теоремы 2, обычно не встречаются.
</block>
<block id='C14.7.1'>
Следствие. (Вычисление площади с помощью криволинейного интеграла.) Пусть область $G \subset \mathbb{R}^{2}$ ограничена, а ее граница $\partial G^{+}$состоит из конечного числа простых замкнутых кусочно-гладких кривых $\Gamma_{k}^{+}(k=1, \ldots, K)$, ориентированных положительно относительно области $G$. Тогда площадь (мера Жордана) области $G$ равна следующим криволинейным интегралам:

$
\mu(G)=\int_{\partial G^{+}} x d y=-\int_{\partial G^{+}} y d x=\frac{1}{2} \int_{\partial G^{+}} x d y-y d x
$
</block>
<block id='C15'>
## ПОВЕРХНОСТНЫЕ ИНТЕГРАЛЫ
</block>
<block id='C15.1'>
## § 1. Определения поверхностей
</block>
<block id='D15.1.1'>
Определение. Пусть вектор-функция $\vec{r}(u, v)=\left(\begin{array}{l}x(u, v) \\ y(u, v) \\ z(u, v)\end{array}\right)$ непрерывна в замыкании измеримой области $G \subset \mathbb{R}_{u v}^{2}$. Тогда множество

$
S=\vec{r}(\bar{G})=\{\vec{r}(u, v):(u, v) \in \bar{G}\} \subset \mathbb{R}_{x y z}^{3}
$

называется поверхностью (заданной параметрически). Векторфункция $\vec{r}(u, v)$ называется параметризацией поверхности $S$.
</block>
<block id='D15.1.2'>
Определение. Пусть поверхность $S$ параметризована непрерывно дифференцируемой вектор-функцией $\vec{r}: \bar{G} \rightarrow S$ (определение непрерывной дифференцируемости функции в замыкании области было дано в §5 главы 14). Точка $\left(u_{0}, v_{0}\right) \in \bar{G}$ называется особой точкой параметризации $\vec{r}$, если векторы $\vec{r}^{\prime}{ }_{u}\left(u_{0}, v_{0}\right)=\left(\begin{array}{l}x_{u}^{\prime}\left(u_{0}, v_{0}\right) \\ y_{u}^{\prime}\left(u_{0}, v_{0}\right) \\ z_{u}^{\prime}\left(u_{0}, v_{0}\right)\end{array}\right)$ и $\vec{r}_{v}^{\prime}\left(u_{0}, v_{0}\right)=\left(\begin{array}{l}x_{v}^{\prime}\left(u_{0}, v_{0}\right) \\ y_{v}^{\prime}\left(u_{0}, v_{0}\right) \\ z_{v}^{\prime}\left(u_{0}, v_{0}\right)\end{array}\right)$ коллинеарны, т. е.

$
\left[\vec{r}_{u}^{\prime}\left(u_{0}, v_{0}\right) \times \vec{r}_{v}^{\prime}\left(u_{0}, v_{0}\right)\right]=\overline{0} .
$
</block>
<block id='D15.1.3'>
Определение. Поверхность $S$ называется простой гладкой, если существует такая ее параметризация $S=\vec{r}(\bar{G})$, что
(1) $G$ - измеримая область в $\mathbb{R}_{u v}^{2}$;
(2) отображение $\vec{r}: \bar{G} \rightarrow S$ взаимно однозначно;
(3) параметризация $\vec{r}$ непрерывно дифференцируема и не имеет особых точек в $\bar{G}$.
</block>
<block id='D15.1.4'>
Определение. Образ границы области $G$ называется краем простой гладкой поверхности $S=\vec{r}(\bar{G})$ и обозначается через $\partial S: \quad \partial S=$
$=\vec{r}(\partial G)$.
</block>
<block id='D15.1.5'>
Определение. Поверхность $S$ называется кусочно-гладкой, если ее можно представить как объединение конечного числа кусков $S_{i}$, $i \in\{1, \ldots, I\}$, таких, что
(1) каждый кусок $S_{i}$ является простой гладкой поверхностью;
(2) два различных куска $S_{i}$ и $S_{j}$ могут пересекаться лишь по краям: $S_{i} \cap S_{j}=\partial S_{i} \cap \partial S_{j}$;
(3) если пересечение двух различных кусков $S_{i}$ и $S_{j}$ представляет собой бесконечное множество точек, то эти куски называются соседними;
(4) пересечение двух соседних кусков состоит из конечного числа кусочно-гладких кривых и, быть может, конечного числа точек;
<block id='D15.1.5'>
(5) для любых двух различных кусков $S_{i}$ и $S_{j}$ существует конечный набор кусков $S_{k_{1}}, S_{k_{2}}, \ldots, S_{k_{m}}$ такой, что $k_{1}=i, k_{m}=j$ и для любого $\ell \in\{1, \ldots, m-1\}$ куски $S_{k_{\ell}}$ и $S_{k_{\ell+1}}$ являются соседними;
(6) пересечение трех различных кусков $S_{i}, S_{j}$ и $S_{k}$ состоит не более чем из конечного числа точек.
</block>
<block id='D15.1.6'>
Определение. Касательной плоскостью к гладкой поверхности $S=\vec{r}(\bar{G})$ в точке $\vec{r}_{0}=\vec{r}\left(u_{0}, v_{0}\right) \in S$ называется плоскость, проходящая через точку $\vec{r}_{0}$ и параллельная векторам $\vec{r}_{u}^{\prime}\left(u_{0}, v_{0}\right), \vec{r}_{v}^{\prime}\left(u_{0}, v_{0}\right)$.
</block>
<block id='D15.1.7'>
Единичный вектор
$\vec{n}\left(\vec{r}_{0}\right)= \pm\left.\frac{\left[\vec{r}_{u}^{\prime} \times \vec{r}_{v}^{\prime}\right]}{\left|\left[\vec{r}_{u}^{\prime} \times \vec{r}_{v}^{\prime}\right]\right|}\right|_{\left(u_{0}, v_{0}\right)}$,
ортогональный касательной плоскости к поверхности $S$ в точке $\vec{r}_{0}$, называется единичным вектором нормали к поверхности $S$ в точке $\vec{r}_{0}$.
</block>
<block id='D15.1.8'>
Определение. Поверхность $S$ называется гладкой, если для любой точки $\vec{r}_{0} \in S$ существует число $\delta>0$ такое, что $\overline{U_{\delta}\left(\vec{r}_{0}\right)} \cap S$ является простой гладкой поверхностью.
</block>
<block id='D15.1.9'>
Определение. Гладкая поверхность $S$ называется ориентируемой, если существует непрерывное поле единичных нормалей к поверхности $S$, т. е. существует непрерывная на множестве $S$ векторфункция $\vec{n}(\vec{r})$, значением которой в каждой точке $\vec{r} \in S$ является вектор единичной нормали к поверхности $S$ в точке $\vec{r}$.
</block>
<block id='R15.1.1'>
Легко видеть, что для ориентируемой поверхности $S$ существуют две взаимно противоположные ориентации. Если какая-либо ориентация поверхности $S$ задана, то поверхность $S$ называется ориентированной.
</block>
<block id='R15.1.2'>
Заметим, что любая простая гладкая поверхность $S=\vec{r}(\bar{G})$ ориентируема, так как каждая из вектор-функций

$
\begin{gathered}
\vec{n}_{+}(\vec{r})=\frac{\left[\vec{r}_{u}^{\prime}(u, v) \times \vec{r}_{v}^{\prime}(u, v)\right]}{\left|\left[\vec{r}_{u}^{\prime}(u, v) \times \vec{r}_{v}^{\prime}(u, v)\right]\right|} \quad \text { и }
\vec{n}_{-}(\vec{r})=-\frac{\left[\vec{r}_{u}^{\prime}(u, v) \times \vec{r}_{v}^{\prime}(u, v)\right]}{\left|\left[\vec{r}_{u}^{\prime}(u, v) \times \vec{r}_{v}^{\prime}(u, v)\right]\right|}, \quad \text { где } \quad \vec{r}=\vec{r}(u, v),
\end{gathered}
$

является непрерывным полем единичных нормалей к поверхности $S$.
</block>
</block>

<end></end>

