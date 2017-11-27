import tweepy
import settings

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_secret)
api = tweepy.API(auth)


# Uncomment this for a stream
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
#        user = api.get_user(status.author.screen_name)
#        for friend in user.friends():
#            print(friend.screen_name)
        print(status.author.screen_name)
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return false


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['beer running'])



# public_tweets = api.user_timeline(count=1) #this takes the tweets and pulls out all the hashtags and user mentions
# for tweet in public_tweets:
#     hash = tweet.entities.get('hashtags')
#     mention = tweet.entities.get('user_mentions')
#     for hashtag in hash:  #prints all hashtags
#         print(hashtag.get('text'))
#     #for mentions in mention: #prints all users mentioned
#     #    print(mentions.get('name'))
#     print(tweet.author.screen_name)

# user = api.get_user('arlabarge')

# my_current_status = api.user_timeline(count=1)
# for tweet in my_current_status:
#     print(tweet.text)

# api.send_direct_message(screen_name='arlabarge', text='Direct Message')
