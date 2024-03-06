#!/usr/bin/python3
"""  Python script that  queries the Reddit API
and returns the number of subscribers  """
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and returns the
    number of subscribers """
    # Reddit API URL for fetching subreddit information
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': 'CustomUserAgent'}

    # the GET request to the Reddit API
    response = requests.get(url, allow_redirects=False, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Check if the subreddit exists
        if 'data' in data and 'children' in data['data']:
            # Print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
    else:
        print("None")
