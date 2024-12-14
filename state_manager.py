import json

def save_state(state: dict, filename: str):
    """Saves the game state to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(state, file, indent=4, ensure_ascii=False)

def load_state(filename: str) -> dict:
    """Loads the game state from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file {filename} could not be parsed.")
        return {}