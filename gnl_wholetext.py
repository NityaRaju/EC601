from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

def sample_analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment

    print("analyze by the whole text")
    print("Score: '+' means positive comments, Score: '-'' means negative comments  ")
    print("the higher of Magnitude, the stronger feeling or expression ")
    print('-------------------------------------------------------------------------')
    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude)+'\n')

    return 0


if __name__ == '__main__':
    #pass in the username of the account you want to download
    with open('/media/sf_lighao602/EC601_mini_project/test02.txt', 'r') as f:
        sample_analyze_sentiment(f.read())
