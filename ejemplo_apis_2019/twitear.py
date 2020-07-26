"""
Ejemplo de consumo de api usando una lib específica para esa api, y que requiere OAuth.
"""
import tweepy


# autenticación de oauth de la app
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
# autenticación de oauth del usuario (
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

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
