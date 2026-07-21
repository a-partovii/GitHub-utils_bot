def ask_output_type():
    """
    Prompts user to select output mode.
    Default is 1 for invalid or empty input.

    Returns:
    list[int, str]: [mode_id, helper_string], the "helper_string" is used as the
    "output_type" argument of the 'extract_usernames()' function.
    """

    print("How would you like to have the result?")
    print("1. Display in the terminal (default)")
    print("2. Save to an output file")
    print("3. Display in the terminal and save a output file")
    print()

    try:
        user_input = int(input("Select an option: ")) or 1
    except ValueError:
            print("Invalid input! The default value will be replaced.")
            user_input = 1

    if user_input == 1 :
        return [1, "list"]
    
    elif user_input == 2:
       return [2, "file"]
    
    return [3, "file"]