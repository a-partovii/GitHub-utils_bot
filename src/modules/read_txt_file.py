def read_txt_file(filename: str):
    """
    Read and extract elements from the txt files.
    Args:
        filename: Path to the text file containing usernames
    Returns:
        List of elements
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            item_list = [line.strip() for line in file if line.strip()]
            
        # print(f"Successfull, read {len(list)} usernames from {filename}")
        return item_list
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'")
        return []
    except Exception as error:
        print(f"Error reading file: {error}")
        return []