import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials



# Authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# key word to look for twitter
query = "iphone 11"  
# Language code (according to ISO 639-1 standard）here we look for twitter in English(en)
language = "en"

# user_timeline function
results = api.search(q=query, lang=language)

# get twitters
for tweet in results:  
   # 打印存在微博对象中的text字段
   print (tweet.user.screen_name,"Tweeted:",tweet.text)
