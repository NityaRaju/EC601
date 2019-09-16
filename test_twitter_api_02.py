import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials



# 传入认证信息，并创建API对象
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# 你想查找的关键字
query = "iphone 11"  
# 语言代码（遵循ISO 639-1标准）
language = "en"

# 使用上面的参数，调用user_timeline函数
results = api.search(q=query, lang=language)

# 遍历所拉取的全部微博
for tweet in results:  
   # 打印存在微博对象中的text字段
   print (tweet.user.screen_name,"Tweeted:",tweet.text)
