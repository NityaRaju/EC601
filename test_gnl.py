from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    # content = 'Your text to analyze, e.g. Hello, world!'

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    print(content)
    #print('Polarity: {}'.format(sentiment.polarity))
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))


if __name__ == '__main__':
    #pass in the username of the account you want to download
    sample_analyze_sentiment('I am too sad for your excuse. You are really fucking guy.')