import os
from TwitterAPI import TwitterAPI


def tweeter(message: str):
    # Necessary keys to have been set for tweeting to work:
    required_keys = ['TWITTER_API_KEY', 'TWITTER_API_SECRET', 'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET']
    for required_key in required_keys:
        try:
            os.environ[required_key]
        except KeyError:
            print(f"Please set the environment variable {required_key}")

    twitter_api_key = os.environ['TWITTER_API_KEY']
    twitter_api_secret = os.environ['TWITTER_API_SECRET']
    twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
    twitter_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    # Using Twitter's v1.1 API to post a tweet
    api = TwitterAPI(twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret)
    r = api.request('statuses/update', {'status': message})
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)
