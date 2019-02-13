#!/usr/bin/python3
""" Prints the titles of the first 10 posts """
import json
import requests


def top_ten(subreddit):
    """Queries the Reddit API and returns titles of top ten hot posts
    Attributes:
        subreddit (string): name of the subreddit
    Return: titles of hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"user-agent": "top_ten_test"}
    posts = requests.get(url, headers=header, allow_redirects=False)\
        .json()["data"]["children"]

    try:
        for post in posts:
            print ("{}".format(post["data"]["title"]))
    except:
        print ("None")
