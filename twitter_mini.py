import twitter

api = twitter.Api(consumer_key='consumer_key',
                  consumer_secret='consumer_secret',
                 access_token_key='access_token_key',
                  access_token_secret='access_token_secret')


results = api.GetSearch(
    raw_query="q=Chanel%20&result_type=mixed&since=2018-09-01&count=100&lang= "'en'"")


with open('/media/sf_EC602/test.txt', 'w') as f:
  for i in range(0,99):
    f.write(results[i].text +'\n')


