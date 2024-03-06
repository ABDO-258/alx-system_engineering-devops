#!/usr/bin/python3
"""  Python script that  queries the Reddit API
and returns the number of subscribers  """
import requests

def recurse(subreddit, hot_list=[], after=None):
    # Reddit API URL for fetching hot posts in a subreddit
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(subreddit, after)

    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # GET request to the Reddit API
    response = requests.get(url, allow_redirects=False, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the subreddit exists
        if 'data' in data and 'children' in data['data']:
            # Append titles to the hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])
            
            # Check if there are more pages (pagination)
            after = data['data']['after']
            if after is not None:
                # Recursive call to fetch the next page
                recurse(subreddit, hot_list, after)
            else:
                # No more pages, return the hot_list
                return hot_list
    else:
        return None