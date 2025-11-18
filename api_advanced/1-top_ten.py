#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.top.ten:v1.0 (by /u/therealigor007)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, 
                                allow_redirects=False)
        
        # If we get a redirect, the subreddit doesn't exist
        if response.status_code == 302:
            print(None)
            return
        
        # If we don't get a successful response
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
                
    except Exception:
        print(None)
