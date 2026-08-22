import json

def read_json(file_path: str):
    """
    Read and deserialize a JSON file.

    Args:
        file_path (str): Path to the target JSON file.

    Returns:
        The Python object loaded from the JSON file.

    Raises:
        FileNotFoundError: If the JSON file does not exist.
        PermissionError: If the file cannot be read.
        json.JSONDecodeError: If the file contains invalid JSON.
        OSError: If another file system error occurs.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"[ERROR] Couldn't find: {file_path}"
        )

    except PermissionError:
        raise PermissionError(
            f"[ERROR] No permission to read file: {file_path}"
        )

    except json.JSONDecodeError as error:
        raise json.JSONDecodeError(
            f"Invalid JSON in file: {file_path}",
            error.doc,
            error.pos
        )

    except OSError as error:
        raise OSError(f"[ERROR] Writing JSON failed:  {error}")