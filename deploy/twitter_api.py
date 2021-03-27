import os
from TwitterAPI import TwitterAPI


def tweeter(message: str):
    print(f"ZZZ os.environ={os.environ}")
    home_path = os.environ['HOME']
    twitter_api_key = os.environ['TWITTER_API_KEY']
    twitter_api_secret = os.environ['TWITTER_API_SECRET']
    twitter_access_token = os.environ['TWITTER_ACCESS_TOKEN']
    twitter_access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    print(f"twitter_api_key={twitter_api_key}\ntwitter_api_secret={twitter_api_secret}\n"
          f"twitter_access_token={twitter_access_token}\ntwitter_access_token_secret={twitter_access_token_secret}")
    print(f"ZZZ message = {message}")
    # Using Twitter's v2 API
    api = TwitterAPI(twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret)

    r = api.request('statuses/update', {'status': message})
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)
