#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent-for-subreddit-subscriber-check"}
    
    try:
        # Make a request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful and if the subreddit exists
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            # If status is not 200, it could be an invalid subreddit
            return 0
    except Exception as e:
        # Any unexpected exceptions are handled here
        print(f"An error occurred: {e}")
        return 0
