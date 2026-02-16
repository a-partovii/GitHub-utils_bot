import os
from read_txt_file import read_txt_file
from write_in_file import write_in_file

def filter_file(file_path:str, filter_items):
    """
    Remove given item or a list of items from a text file.

    Args:
        file_path: path to file, including its file extension
        items: a single item or a list of items to remove
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    if isinstance(filter_items, list):
        remove_set = {str(i).strip() for i in filter_items}
    else:
        remove_set = {str(filter_items).strip()}

    # read file and make it a list
    raw_list = read_txt_file(file_path)

    # filter
    new_list = [i for i in raw_list if i not in remove_set]

    write_in_file(file_path, new_list, writing_mode="w")

def deduplicate_file_content(file_path:str):
    """
    Remove duplicated items from a text file.

    Args:
        file_path: path to the file, including its file extension
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    raw_list = read_txt_file(file_path)
    seen = set()
    new_list = []
    for i in raw_list:
        if i not in seen:
            seen.add(i)
            new_list.append(i)

    write_in_file(file_path, new_list, writing_mode="w")
