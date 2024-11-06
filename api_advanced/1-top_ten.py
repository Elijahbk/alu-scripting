#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Function that queries the Reddit API."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title', None))
    else:
        print("None")
