"""
Put your GitHub Personal Access Tokens in the dictionaries below.
The key is just a name to identify each token, and the value is the token itself.

You can add multiple secondary tokens to spread API requests between them.
This helps reduce rate limiting and lowers the risk of getting blocked.

The primary token is used for modifying actions (such as starring or following).
The secondary tokens are only used for doing background tasks.

Using secondary tokens is optional, but recommended.
"""
import random

# The main GitHub personal access token for modifying tasks
primary_token = {
    "name": "ghp_####################################" 
}
# The secondary GitHub personal access tokens to help proccess
secondary_tokens = {
    "name1": "ghp_####################################",
    "name2": "token2",
    "name3": "token3"
}

def headeres(token):
    """
    Generate GitHub API headers using the provided token."""
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

# Tracking last used token to avoid repeats
last_token = None
def random_token(tokens_dict=secondary_tokens):
    """
    Select a random token from the dictionary, 
    ensuring it's not the same as the last one.
    """
    global last_token
    tokens_list = list(tokens_dict.values())

    if len(tokens_list) == 1:
        return tokens_list[0]
    
    while True:
        token = random.choice(tokens_list)
        if token != last_token:
            last_token = token
            return token