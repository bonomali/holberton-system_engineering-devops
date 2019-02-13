#!/usr/bin/python3
""" Returns a list with all the titles of hot articles """
import requests


def recurse(subreddit, hot_list=[], next=""):
    """Queries the Reddit API and returns titles of hot articles
    Attributes:
        subreddit (string): name of the subreddit
        hot_list (list): list of hot posts
    Return: titles of hot posts
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100"\
            .format(subreddit)
        header = {"user-agent": "recurse_test"}
        posts = requests.get(url, headers=header, allow_redirects=False,
                             params={"after": next}).json()["data"]["children"]
        nextpage = requests.get(url, headers=header, allow_redirects=False,
                                params={"after": next}).json()["data"]["after"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        if nextpage is not None:
            recurse(subreddit, hot_list, nextpage)
        return hot_list
    except:
        return (None)
