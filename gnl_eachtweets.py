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

    a = sentiment.score
    b = sentiment.magnitude

    return a,b


if __name__ == '__main__':
    #pass in the username of the account you want to download
    with open('/media/sf_lighao602/EC601_mini_project/test02.txt', 'r') as f:
        sum01 = 0
        sum02 = 0
        n = 0

        for line in f.readlines():
            a,b = sample_analyze_sentiment(line)
            sum01 = sum01 + a
            sum02 = sum02 + b
            n = n + 1

        avg_score = sum01/n
        avg_magnitude = sum02/n


        print("analyze by every tweet in text")
        print("Score: + means positive comments, Score: - means negative comments  ")
        print("the higher of Magnitude, the stronger feeling or expression ")
        print('-------------------------------------------------------------------------')
        print('Score: {}'.format(avg_score))
        print('Magnitude: {}'.format(avg_magnitude)+'\n')
