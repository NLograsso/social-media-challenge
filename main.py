import tweepy

auth = tweepy.OAuthHandler('5EEbrv2FAqd0J6t92RTTfbAdc', 'QDxf4Z2FVlVxaO1lsi3uX0e69LbOoNjcjLgZ1pBBmZBYMhULfC')

# try:
#     redirect_url = auth.get_authorization_url()
# except tweepy.TweepError:
#     print ('Error! Failed to get request token.')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

user = api.get_user('realDonaldTrump')

print(user.screen_name)
print(user.followers_count)

# for tweet in user.tweets():
# 	print(tweet.text)