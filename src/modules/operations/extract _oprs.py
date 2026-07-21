def ask_output_type():
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

extract_submenu = {
    # "1": {"label": "Extract your followers usernames", "action": extract_your_followers},
    # "2": {"label": "Extract your following usernames", "action": extract_your_following},
    # "3": {"label": "Extract usernames you follow who don't follow you back", "action": extract_non_followers},
    # "4": {"label": "Extract a user's followers", "action": extract_from_followers},
    # "5": {"label": "Extract a user's following", "action": extract_from_following},
    # "6": {"label": "Extract usernames of users who starred your repositories", "action": extract_my_stargazers},
    # "7": {"label": "Extract usernames of users who starred a given user's repositories", "action": extract_user_stargazers},
    # "8": {"label": "Extract usernames of users who starred a given repository", "action": extract_repo_stargazers},
    # "9": {"label": "Extract bulk usernames to follow with a limit", "action": extract_bulk},
    # "0": {"label": "Back to main menu", "action": return_to_main},
}