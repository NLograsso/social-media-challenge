import tweepy

consumer_key = '858dJ9NBYSMgu2u7Onu6LBcbG'
consumer_secret = '66SlUxKVsqs3jovP8WStPeQ3w24TbRHa7vpjDIYI03jvHobCKs'

access_token_key = '916395702380408832-M38tYdjxdH0MiaolfupWL3juxFvKKAd'
access_token_secret = 'ms1fFRT1Ro41KsVjOKs0d9dbrYYBmVxFyfD3Z1qZG5oey'

auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)


api = tweepy.API(auth1)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print 'Ran on_status'

def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

def on_data(self, data):
	print 'Ok, this is actually running'


myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['python'], async=True)

# handle = input("Input Twitter Handle: ")

# user = api.get_user(handle)

# #print("\nTwitter Handle: {}".format(user.screen_name))
# print("\nName: {}".format(user.name))
# print("Description: {}".format(user.description))
# print("Followers: {}".format(user.followers_count))
# print("Friends: {}".format(user.friends_count))

# # for tweet in user.tweets():
# # 	print(tweet.text)