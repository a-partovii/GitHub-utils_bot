def print_in_columns(items_list, columns=3, width=35):
    """
    Prints a list of items in aligned columns.

    Args:
        items_list (list[str]): Items to display.
        columns (int, optional): Number of columns. Defaults to 3 (Default=3)
        width (int, optional): Width of each column. Defaults to 35 (Default=35)
    """
    if not items_list : 
        print("No items found.")

    for i, item in enumerate(items_list, start=1):
        text = f"{i}. {item}"
        print(f"{text:<{width}}", end="")

        if i % columns == 0:
            print()

    # Move to the next row.
    if len(items_list) % columns != 0:
        print()