import requests as req
from modules.delay import delay

# -------------------------------------------

def get_followers_list(target_username, headers, output_type="list"):
    page = 1
    
    followers_list = []
    while True:
        # per_page = 100, max items per request
        url = f"https://api.github.com/users/{target_username}/followers?per_page=100&page={page}"
        response = req.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error fetching followers — HTTP {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        for follower in data:
            followers_list.append(follower.get("login"))

        page += 1
        delay(2, 6) # Random delay per request (2–6 seconds)

    if output_type == "file": # "file" or "list" (default=List)
        try:
            with open(f"({target_username})followers.txt", "w") as file:
                for username in followers_list:
                    file.write(username + "\n")
        except :
            print("Writing in the file was not success, check this error and try again: \n")
    else:
        return followers_list
    print("Done! All follower usernames saved.")
