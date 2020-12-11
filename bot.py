import tweepy # Tweepy module
import time # Time module

from credentials import * # From credentials.py import all variables.

def twitter_setup(): # Function to set-up credentials

    # Authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) # Authenticate with API's key. Provided by apps.twitter.com
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) # Personal access key. Here check that your bot is not "read-only" mode, if you change to read-write, remember regenerate the access token.

    # Generating API Object
    api = tweepy.API(auth) # API function takes all auth parameters, then log in.

    return api # Returns API Object

if __name__ == '__main__':
    
    bot = twitter_setup() # Calls function, then take "api" object and register as "bot"

    secs = int # Declare time in seconds to sleep the bot from tweet to tweet.

    try:                                        # Try to send tweet
        bot.update_status('Hello world!')       # Tweets "Hello world!"
        print('Tweet sent!')                    #
    except tweepy.TweepError as e:              # If fails...
        print(e.reason)                         # print error reason.
    
    time.sleep(secs)                            # Then wait x secs, and try again.