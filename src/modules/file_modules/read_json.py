import json


def read_json(file_path: str):
    """
    Read and deserialize a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        The Python object deserialized from the JSON file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(f"[ERROR] File not found: {file_path}")

    except PermissionError:
        raise PermissionError(f"[ERROR] Permission denied: {file_path}")

    except json.JSONDecodeError:
        raise json.JSONDecodeError(
            f"[ERROR] Invalid JSON: {file_path}")