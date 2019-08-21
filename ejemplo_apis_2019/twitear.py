"""
Ejemplo de consumo de api usando una lib específica para esa api, y que requiere OAuth.
"""
import tweepy


# autenticación de oauth de la app
CONSUMER_KEY = 'GuaSCSTGMQmwG2NsYFWRa9zOY'
CONSUMER_SECRET = 'Fj3t3d7IdmD7eBBWoOyc4P5AfPfDjoEXqlKy8AlpUdBLalz3V3'
# autenticación de oauth del usuario (
ACCESS_TOKEN = '44492903-uOksk9VTOgUUsWWcBC3pAGC8MtjDOSnVYs6PJPNvQ'
ACCESS_TOKEN_SECRET = 'HeCCmI5a5fB7qb4HX6RYyUG3kT9CZ4zWUjC4MKHCiXgyz'

# cliente de la api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# usamos la api para traer datos y mostrarlos
print('5 most recent tweets from fisa:')
print()
tweets = api.user_timeline('fisadev', count=10, page=1)
for tweet in tweets[0:5]:
    print(tweet.user.screen_name, tweet.created_at)
    print(tweet.text)
    print('----')
