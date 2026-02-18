import os

def delete_file(file_path):
    """
    Takes a file path and deletes the file.
    If the file does not exist, it prints an error message.

    Args:
        file_path (str): The path to the file to be deleted, including extension.
    """
    try:
        os.remove(file_path)
        return f"[SUCCESS] File deleted: {file_path}"
    
    except FileNotFoundError:
        return f"The file doesn't exist: {file_path}"
    
    except Exception as e:
        print(f"[ERROR] Deleting File: {e}")