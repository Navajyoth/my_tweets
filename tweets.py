import oauth2 as oauth
import json

CONSUMER_KEY = "your consumer key"
CONSUMER_SECRET = "your consumer secret key"
ACCESS_KEY = "your access key"
ACCESS_SECRET = "your access secret key"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    print tweet['text']









