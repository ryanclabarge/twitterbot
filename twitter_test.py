import tweepy
import settings

auth = tweepy.OAuthHandler(settings.consumer_key,settings.consumer_secret)

auth.set_access_token(settings.access_token,settings.access_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name='arlabarge',count=1)
for tweet in public_tweets:
    print(tweet.text)

user = api.get_user('arlabarge')
for friend in user.friends():
    print(friend.screen_name)

#api.send_direct_message(screen_name='arlabarge', text='Direct Message')

