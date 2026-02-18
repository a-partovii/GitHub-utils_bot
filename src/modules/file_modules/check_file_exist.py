import os

def check_file_exist(file_path:str) -> bool:
    """
    Check if a file exists at the specified path.

    Args:
        file_path (str): The path to the file to check.
    """         
    if os.path.exists(file_path):
        return True
    return False
