from modules.major_modules import extract_usernames, extract_bulk_usernames_to_follow
from modules.utils import filter_list
from config.tokens import primary_token, token_manager
from modules.tui import print_in_columns, ask_output_type

def extract_your_followers():
        output_type = ask_output_type()
        my_username = next(iter(primary_token))
        
        my_followers = extract_usernames(
             target_username=my_username,
             source="followers",
             output_type= output_type[1]
        )

        if output_type[0] != 2:
            print_in_columns(my_followers)

# -----------------------------------------------------------------------------------------
extract_submenu = {
    "1": {"label": "Extract your followers usernames", "action": extract_your_followers},
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
