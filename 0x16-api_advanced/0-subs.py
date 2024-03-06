import requests

def number_of_subscribers(subreddit):
    # Reddit API URL for fetching subreddit information
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    headers = {'User-Agent': 'CustomUserAgent'}
    
    # the GET request to the Reddit API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the number of subscribers from the response
        subscribers_count = data['data']['subscribers']
        
        return subscribers_count
    else:
        # Handle other error cases
        return 0
