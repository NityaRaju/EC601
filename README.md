# MiniProject 1

### Product Mission
## Target User(s): 
Tech-savvy consumers who consider Twitter an accurate source for reviews, updates, and the sentiment of the general public towards a certain product/service/establishment etc. If the user does not trust Twitters general opinions/views, then this system may not be for them. Some people believe the general public on twitter are misleading/inaccurate/ improperly critical etc. This application would not be designed for them. But anyone else who wants a quick summary of a large number of twitter reviews, to see if the general opinion towards a product/service/establishment is positive or negative(direction of sentiment), and how positive or negative it is (magnitude of sentiment). 

## User Stories: 
Main User stories for our use:
I, the user, should be able to receive the sentiment of the top trending news stories on a particular day. 
I, the consumer, should be able to receive a review on a particular book/movie/TV show/music album etc by analyzing all the tweets related to that particular form of entertainment and summarizing the general public sentiment about it.
I, the voter, should be able to look up the amount of support a certain legislative policy/ law/bill is receiving by analyzing all the tweets related to the legislation.
I, the consumer, should be able to locate the best possible place to eat by analyzing tweets about all the restaurants in the area and seeing which restaurants receive the most positive feedback. 
I, the business owner/manager/product producer should be able to analyze tweets related to the products/brands/goods that I am selling in order to receive consumer feedback. 
Other potential User stories: 
I, the advertiser, should be able to analyze a users tweets/retweets/comments to receive information about the products, goods and services that a person likes or dislikes to determine a targeted marketing scheme for that user. 
I, the advertiser, should be able to classify a person based on their political preferences, marital status, age, education, interests etc by analyzing their twitter accounts to perform targeted marketing. 
I, the media consumer, should be able to classify the political alignment (Democrat/Republican/Neutral) of a particular news source, based on the sentiments of their tweets related to certain bipartisan issues.   
I, the voter, should be able to gauge the sentiments towards a particular politician and their policies by analyzing news and tweets about that person, in addition to their own tweets. 

## MVP: 
For all these use cases, An application which can perform natural language processing in order to read & summarize tweets and return certain features of the text would be the minimum viable product. 
User Interface Design for main user story if required

## System Design and how your design addresses your user stories
In particular, if we focus on use cases 1-5, which are the use cases our system is set up for, then we see that the system design is an application/program which can accept the name of a product/service/establishment/trending topic/media source/ etc as a search query, and then use the Twitter API to return all the relevant tweets which contain that particular source term. (A number of additional search parameters may also be included to refine the search by date,popularity,location etc). Once the relevant tweets have been obtained from the Twitter API, we can use the Google Natural Language processing API to analyze these tweets and give us the sentiment. This way our users can find relevant reviews about the object they are interested in.

## How to build the system
Our system is comprised of a number of application programming interfaces which all interact with each other to give us the needed results. The first API we will be dealing with is the Twitter API. First, a Twitter developer account must be created and you must initialize the building of an application via Twitter. Then Twitter will grant you access to its API keys and tokens. With these API keys, we can now receive a wide range of information from the twitter website, so that we may use the data in the development of our own application. In order to use this API, we download a python-twitter library, such as python-twitter or tweepy because these libraries provide pure python interfaces for the twitter API. This way, we can write python code to extract the information we need. In the python code, we provide the authentication for the Twitter API using our API key credentials and then we use the api.GetSearch() function from the python-twitter library to return a list of twitter.Status instances containing the search parameter we are interested in. The GetSearch function allows us to specify a certain search term, in addition to number of results, type of result, language of result  etc. We can then index into this list to return only the relevant tweet (without the timestamp, location, user profile etc). All these tweets can then be exported into a .txt file to be analyzed by the Google natural language API. . 

### Testing 
## Test document providing how each test case addresses the user stories
News story test case: Using the search query ‘immigration’, we can specify the date from which we want to see the results (so that we can get only the latest stories), choose ‘recent’ tweets (if we want to get updates on a new breaking story), and additionally apply location and language filters as well to the tweets if the user would like. 

Entertainment review test case: Using the name of a particular book/movie/TVshow etc as a search query, we can specify the release date of the media as the date from which we want to see results, choose ‘popular’ tweets (to get most legitimate or validated reviews), and additionally apply location and language filters as well to the tweets if the user would like. 

Restaurant review test case: Using the name of a particular restaurant as a search query, and also specifying a geocode (latitude or longitude) to ensure only reviews relevant to the restaurant in question show up. Can choose ‘mixed’ tweets (to get both recent and popular tweets) and additionally apply location and language filters as well to the tweets if the user would like. 

Product review test case: Using certain products/brands/goods as a search query, the business owner can apply any number of additional filters on the tweets (date, location, popularity etc) as he/she may see fit for the purposes of their analysis so they may receive customer feedback. 

## Result of testing (screen shots, etc.)



### Lessons learned 
## What you liked doing?
It was interesting to see all the various ways information from twitter could be summarized and accessed. Initially, it seemed like the main function of the API would be to obtain just raw tweets from twitter, but there was an abundance of information that could be obtained about every tweet, user, hashtag and profile. I liked learning how to use APIs because they are truly at the client-server intersection and it made me realize that there is much data from so many different companies that can be harnessed and used in various ways. It think its very beneficial to be able to access data from companies with large user bases such as Twitter, Uber, Facebook etc because so many additional applications can be built off from this data to improve efficiency and convenience for users in other areas. 

## What you could have done better?
I could have learnt how to use the python-twitter libraries better, because the main issue I faced was while using tweepy. I managed to install tweepy onto my computer but for some reason the code was not compiling because the modules in the library could not be accessed. I could have dealt with this issue better through more debugging because the same code ran on my partners computer but not mine. 

## What you will avoid in the future?
However, at the same time, I will avoid excessive debugging procedures in the future because I realized that python-twitter was a perfectly good alternative to tweepy which helped our system to execute as expected. So in the future, I will always try to explore as many alternative solutions to a problem, as soon as possible. 



