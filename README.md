# EC601

Sprint 1 for Mini-Project1 : Analyzing the sentiment of twitter feeds

## User stories

- **Advertising**<br>I, the advertiser, should be able to analyze a users tweets/retweets/comments to receive information about the products, goods and services that a person likes or dislikes to determine a targeted marketing scheme for that user. 

- **Advertising**<br>I, the advertiser, should be able to classify a person based on their political preferences, marital status, age, education, interests etc by analyzing their twitter accounts to perform targeted marketing. 

- **Reviews**<br>I, the user, should be able to receive the sentiment of the top trending news stories on a particular day.

- **Reviews**<br>I, the consumer, should be able to receive a review on a particular book/movie/TV show/music album etc by analyzing all the tweets related to that particular form of entertainment and summarizing the general public sentiment about it.

- **Politics**<br>I, the voter, should be able to look up the amount of support a certain legislative policy/ law/bill is receiving by analyzing all the tweets related to the legislation.

- **Politics**<br>I, the voter, should be able to gauge the sentiments towards a particular politician and their policies by analyzing news and tweets about that person. 

- **Media**<br>I, the media consumer, should be able to classify the political alignment (Democrat/Republican/Neutral) of a particular news source, based on the sentiments of their tweets related to certain bipartisan issues. 
 
- **Food&Restaurant**<br>I, the consumer, should be able to locate the best possible place to eat by analyzing tweets about all the restaurants in the area and seeing which restaurants receive the most positive feedback. 

- **Business**<br>I, the business owner/manager/product producer should be able to analyze tweets related to the products/brands/goods that I am selling in order to receive consumer feedback. 

<br>

## Minimum Viable Product
An application which can perform natural language processing in order to read & summarize tweets and return certain features of the text. 

<br>

## Modular Design/Architecture
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/structure.png)

<br>

## System Design and how your design addresses your user stories.
I am in charge of Google Natural Language API. According to our user stories, we will analyze the people’s comments on some items(eq. Movie, phone, make-up), and then give the general feedback to user who want to buy these items or companies who produce these items.

So the user can enter the key words which he wants to know about this item. For example, the user enters iphone11, and our twitter part code will search this key word in the recent and popular tweets. Besides the user can choose to add other filters, like the location of post tweets, the period of time, the language.

After the system get related tweets, it will save in the text type and export to the google natural language part. It will analyze the words which express the feelings and the attitude and the extent of these words. Once we get each tweet score and magnitude, we will process these data and get the average ones to show the public attitude to this item. Then the user will have the general feeling about this item.

<br>

## README of how to build your system
Google Natural Language API：
The output of twitter get user comments is in .text type, so first to ensure the text binary type is utf-8, and then use google to analyze the text. By using the with io.open to read the text and “for loop” and readlines() to analyze each line of the text. 

Besides, I find there are 2 methods to analyze the text. The one is to user function to analyze the whole text at a time. The other one is to analyze the tweets in the text one by one, and then calculate the  average score and magnitude.

### **More detailed process:**<br>
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/detailed%20.png)

<br>

## Testing
### Test document providing how each test case addresses the user stories
This is our text which get tweets related to keywords(iphone11).
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/twiiter_result.png)

This is the analysis to 100 tweets(enter whole text at a time)
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/gnl_03_100.png)

This is the analysis to 100 tweets(enter the tweets one by one)
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/gnl_100.png)

This is the analysis to 1000 tweets(enter whole text at a time)
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/gnl_03_1000.png)


This is the analysis to 1000 tweets(enter the tweets one by one)
![image](https://github.com/NityaRaju/EC601/blob/sprint_Ganghao/photos/gnl_1000.png)

### Analysis:
The 2 methods to analyze the same amount of tweets. The score and magnitude in  method which analyze the whole text at a time, both are much higher than that which analyze the tweets one by one. I think maybe it is related to Google Natural Language API inner work. The API may its own work principle. For example, it may  have the offset where there are some opposite attitudes or composition where there are similar attitudes.

When I use one method to analyze the different amount of tweets. I test 100 tweets and 1000 tweets separately. With the amount of tweets increases, basically the score does not have any change, but the magnitude increase a lot. I think score represents this item quality, so it depends on items. It does not vary from user a lot. But, the magnitude represents the extent of people’s feelings, so that can vary from different people a lot. That’s what causes this result.

<br>

## Lessons learned
### What you liked doing?
I liked to come about user stories and reading APIs. For one function, maybe there are not only one related APIs, so read them and I will know the advantages and disadvantages.  To find a bridge to connect the user stories and APIs. To find how we can realize this function through coding. These are what I enjoyed.


### What you could have done better?
Like I mentioned in the analysis of results, I did not completely understand how sentiment analysis(NLP) work. If I enter one tweets into it, I can figure out the results, but when I enter the whole text, I did not know how it calculates or how its algorithm works. Besides, if the sentences included error codes or irrelevant words(like web link, user name), how will NLP process them. So the result of analyze attitude may not totally correct. It still needs to be optimized. 

### What you will avoid in the future?
Completely understand the APIs before using them.
Do not focus on one API, because sometimes there are other more useful APIs to realize the function.

<br>

## References
- Tweepy api:http://docs.tweepy.org/en/v3.5.0/api.html

- Google natural language api:
https://cloud.google.com/natural-language/docs/analyzing-sentiment
