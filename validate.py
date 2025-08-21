
import json
import re
from collections import Counter

# --- Configuration ---
RAW_MD_PATH = "ivanovnic.md"
MARKED_MD_PATH = "ivanovnic_marked.md"
GRAPH_JSON_PATH = "graph.json"

# --- Helper Functions ---

def get_ids_from_markdown(content: str) -> list[str]:
    """Extracts all block IDs from the custom tags in the markdown file."""
    return re.findall(r"<([A-Z]+\d+(?:\.\d+)*)>", content)

def get_ids_from_graph(graph_data: dict) -> list[str]:
    """Extracts all node IDs from the graph JSON."""
    return [node['id'] for node in graph_data.get('nodes', [])]

def strip_tags_from_markdown(content: str) -> str:
    """Removes all block tags from the markdown content."""
    # This regex finds both start and end tags like <T1.2.3> and </T1.2.3>
    return re.sub(r"</?([A-Z]+\d+(?:\.\d+)*)>\n?", "", content)

# --- Validation Checks ---

def check_content_preservation():
    """
    Strips tags from the marked file and compares its content to the raw file.
    They should be identical, ensuring no content was lost or altered.
    """
    print("1. Checking Content Preservation...")
    try:
        with open(RAW_MD_PATH, 'r', encoding='utf-8') as f:
            raw_content = f.read()
        with open(MARKED_MD_PATH, 'r', encoding='utf-8') as f:
            marked_content = f.read()

        stripped_content = strip_tags_from_markdown(marked_content)

        if stripped_content.strip() == raw_content.strip():
            print("   \033[92mSUCCESS:\033[0m Content is perfectly preserved.")
            return True
        else:
            print("   \033[91mFAILURE:\033[0m Content differs between raw and marked files.")
            # Optional: Write to files to make diffing easier
            with open("temp_raw.txt", "w", encoding="utf-8") as f:
                f.write(raw_content)
            with open("temp_stripped.txt", "w", encoding="utf-8") as f:
                f.write(stripped_content)
            print("      -> Diff files created: temp_raw.txt, temp_stripped.txt")
            return False
    except FileNotFoundError as e:
        print(f"   \033[91mFAILURE:\033[0m File not found: {e.filename}")
        return False

def check_format_validity():
    """
    Checks if the JSON is valid and if markdown tags are properly matched.
    Also checks for duplicate IDs as a symptom of non-idempotency.
    """
    print("2. Checking Format Validity & Idempotency...")
    # JSON Validity
    try:
        with open(GRAPH_JSON_PATH, 'r', encoding='utf-8') as f:
            graph_data = json.load(f)
        print("   \033[92mSUCCESS:\033[0m graph.json is a valid JSON file.")
    except json.JSONDecodeError:
        print("   \033[91mFAILURE:\033[0m graph.json is not a valid JSON file.")
        return False
    except FileNotFoundError:
        print(f"   \033[91mFAILURE:\033[0m File not found: {GRAPH_JSON_PATH}")
        return False

    # Markdown Tag Matching
    with open(MARKED_MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tags = re.findall(r"<([A-Z]\d+\.\d+\.\d+)>", content)
    end_tags = re.findall(r"</([A-Z]\d+\.\d+\.\d+)>", content)

    if Counter(start_tags) == Counter(end_tags):
        print("   \033[92mSUCCESS:\033[0m All markdown tags are properly matched and closed.")
    else:
        print("   \033[91mFAILURE:\033[0m Mismatch in markdown start/end tags.")
        print(f"      -> Start tags found: {Counter(start_tags)}")
        print(f"      -> End tags found:   {Counter(end_tags)}")
        return False

    # Idempotency check for duplicates
    graph_ids = get_ids_from_graph(graph_data)
    if len(graph_ids) == len(set(graph_ids)):
        print("   \033[92mSUCCESS:\033[0m No duplicate node IDs found in graph.json.")
    else:
        print("   \033[91mFAILURE:\033[0m Duplicate node IDs found in graph.json.")
        print(f"      -> Duplicates: {[item for item, count in Counter(graph_ids).items() if count > 1]}")
        return False

    return True


def check_synchronization():
    """
    Checks if the set of IDs in the marked markdown and the graph JSON are identical.
    """
    print("3. Checking Synchronization...")
    try:
        with open(MARKED_MD_PATH, 'r', encoding='utf-8') as f:
            md_content = f.read()
        with open(GRAPH_JSON_PATH, 'r', encoding='utf-8') as f:
            graph_data = json.load(f)

        md_ids = set(re.findall(r"<([A-Z]\d+\.\d+\.\d+)>", md_content))
        graph_ids = set(get_ids_from_graph(graph_data))

        if md_ids == graph_ids:
            print("   \033[92mSUCCESS:\033[0m ID sets in markdown and JSON are identical.")
            return True
        else:
            print("   \033[91mFAILURE:\033[0m ID sets are out of sync.")
            print(f"      -> In Markdown but not in JSON: {md_ids - graph_ids}")
            print(f"      -> In JSON but not in Markdown: {graph_ids - md_ids}")
            return False
    except FileNotFoundError as e:
        print(f"   \033[91mFAILURE:\033[0m File not found: {e.filename}")
        return False

def check_accuracy():
    """
    Validates the ID format for all blocks/nodes and ensures all graph links are valid.
    """
    print("4. Checking Accuracy...")
    id_format_regex = re.compile(r"^[A-Z]+\d+(?:\.\d+)*$")
    all_checks_passed = True

    try:
        with open(GRAPH_JSON_PATH, 'r', encoding='utf-8') as f:
            graph_data = json.load(f)
        
        node_ids = set(get_ids_from_graph(graph_data))

        # Check Node ID format
        invalid_ids = [i for i in node_ids if not id_format_regex.match(i)]
        if not invalid_ids:
            print("   \033[92mSUCCESS:\033[0m All node IDs in graph have a valid format.")
        else:
            print(f"   \033[91mFAILURE:\033[0m Invalid node IDs found in graph: {invalid_ids}")
            all_checks_passed = False

        # Check Link Validity
        invalid_links = []
        for link in graph_data.get('links', []):
            source = link.get('source')
            target = link.get('target')
            if source not in node_ids or (target not in node_ids and link.get('type') != 'outside'):
                invalid_links.append(link)
        
        if not invalid_links:
            print("   \033[92mSUCCESS:\033[0m All links in graph point to existing nodes.")
        else:
            print(f"   \033[91mFAILURE:\033[0m Found invalid or dangling links: {invalid_links}")
            all_checks_passed = False

    except FileNotFoundError as e:
        print(f"   \033[91mFAILURE:\033[0m File not found: {e.filename}")
        return False
        
    return all_checks_passed


def main():
    """Runs all validation checks."""
    print("\n--- Running Validation Suite ---\n")
    results = [
        check_content_preservation(),
        check_format_validity(),
        check_synchronization(),
        check_accuracy(),
    ]
    print("\n--------------------------------\n")
    if all(results):
        print("\033[92mAll validation checks passed successfully!\033[0m")
    else:
        print(f"\033[91mValidation failed. {results.count(False)} check(s) failed.\033[0m")

if __name__ == "__main__":
    main()
