import tweepy
import pandas as pd
import json
from datetime import datetime
import fs  # PyFilesystem
from google.cloud import storage 

# twitter api keys
access_key = "FSiSuquUPIqW2iIj0zdZjYuzu"
access_secret="KnvGiOImdnktFEvtOqbJMTPqX5b48VUVHJJRVyBr1trleu9hJu" 
consumer_key ="1208858853535825923-bMoNZXwsgUINczMM8G7A3Jf6CpMr0b"
consumer_secret="kMxvQrazkDIXTfEMdxLO0tm4eyijuAazNGx6K9jaWMh22"

#twitter authentication 
auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#creating an API object 
api = tweepy.API(auth)

#scraping a users twitter 
tweets = api.user_timeline(screen_name="kimvtaii",
                            # 200 is the maximum allowed count 
                            count=200,
                            include_rts=False,
                            # Necessary to keep full_text 
                            tweet_mode="extended"
                            )
print(tweets)