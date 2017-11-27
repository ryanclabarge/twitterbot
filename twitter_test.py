import tweepy
import settings

auth = tweepy.OAuthHandler(settings.consumer_key,settings.consumer_secret)

auth.set_access_token(settings.access_token,settings.access_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline() #this takes the tweets and pulls out all the hashtags and user mentions
for tweet in public_tweets:
    hash = tweet.entities.get('hashtags')
    mention = tweet.entities.get('user_mentions')
    #print(tweet.text)
    for hashtag in hash:  #prints all hashtags
        print(hashtag.get('text'))
    for mentions in mention: #prints all users mentioned
        print(mentions.get('name'))

# user = api.get_user('arlabarge')
# for friend in user.friends():
#     print(friend.screen_name)

# my_current_status = api.user_timeline(count=1)
# for tweet in my_current_status:
#     print(tweet.text)

#api.send_direct_message(screen_name='arlabarge', text='Direct Message')

