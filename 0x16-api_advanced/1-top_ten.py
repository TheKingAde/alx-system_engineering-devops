#!/usr/bin/python3
import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10', headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
