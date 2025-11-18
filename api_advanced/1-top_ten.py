#!/usr/bin/python3
"""Function that queries the Reddit API"""

import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:subreddit:v1.0 (by /u/therealigor007)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 302:
            print(None)
            return

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
