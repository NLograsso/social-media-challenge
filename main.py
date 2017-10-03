import tweepy

auth = tweepy.OAuthHandler('5EEbrv2FAqd0J6t92RTTfbAdc', 'QDxf4Z2FVlVxaO1lsi3uX0e69LbOoNjcjLgZ1pBBmZBYMhULfC')

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print 'Error! Failed to get request token.'

# Example w/o callback (desktop)
# verifier = raw_input('Verifier:')

# print(auth.access_token)
# print(auth.access_token_secret)

auth.set_access_token('24435877-x2wDohtnf7LsQjZ0ZsU18roCDNgivE6rzr9GeRn8G', 'cpzzjk73RkfThQXeHHgAyvmg4MHqRb1nSuEJzNSRPeaWe')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text