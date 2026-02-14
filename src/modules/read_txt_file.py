from typing import List

def read_txt_file(filename:str, separator:str = "\n") -> List[str]:
    """
    Read and extract elements from a text file based on the separator type.

    Args:
        filename: Path to the file, including its file extension
        separator_type: Type of separator ("\n" newline, "," comma, ";" semicolen, "|" pipe)

    Returns:
        List of extracted elements
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        items_list = [
            item.strip()
            for item in content.split(separator)
            if item.strip()
            ]
        return items_list

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except PermissionError:
        raise PermissionError(f"Permission denied to read '{filename}'")
