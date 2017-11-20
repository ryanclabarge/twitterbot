from twython import Twython
import settings

twitter = Twython(settings.APP_KEY,access_token=settings.ACCESS_TOKEN)

print(twitter.search(q='python'))
