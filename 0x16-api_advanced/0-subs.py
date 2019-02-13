#!/usr/bin/python3
""" Returns the number of subs """
import json
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns number of subs
    Attributes:
        subreddit (string): name of the subreddit
    Return: The number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"user-agent": "sub_count_test"}

    try:
        return (requests.get(url, headers=header, allow_redirects=False)
                .json()["data"]["subscribers"])
    except:
        return 0
