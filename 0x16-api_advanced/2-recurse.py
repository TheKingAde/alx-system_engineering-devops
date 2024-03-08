#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    hot_list.extend([post['data']['title'] for post in data['children']])

    if 'after' in data and data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])
    else:
        return hot_list
