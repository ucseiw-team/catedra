import tweepy


CONSUMER_KEY = 'GuaSCSTGMQmwG2NsYFWRa9zOY'
CONSUMER_SECRET = 'Fj3t3d7IdmD7eBBWoOyc4P5AfPfDjoEXqlKy8AlpUdBLalz3V3'

ACCESS_TOKEN = '44492903-uOksk9VTOgUUsWWcBC3pAGC8MtjDOSnVYs6PJPNvQ'
ACCESS_TOKEN_SECRET = 'HeCCmI5a5fB7qb4HX6RYyUG3kT9CZ4zWUjC4MKHCiXgyz'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets = api.user_timeline('fedeZurbriggen', count=10, page=1)
