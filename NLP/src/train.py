from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import re, string, random, nltk, pickle

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token
            
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

        
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
neutral_tweets = twitter_samples.strings('tweets.20150430-223406.json')

stop_words = stopwords.words('english')            

positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
neutral_tweet_tokens = twitter_samples.tokenized('tweets.20150430-223406.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []
neutral_cleaned_tokens_list = []

for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

for tokens in neutral_tweet_tokens:
        neutral_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
neutral_tokens_for_model = get_tweets_for_model(neutral_cleaned_tokens_list)

positive_dataset = [(tweet_dict, "Positive")
                            for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                            for tweet_dict in negative_tokens_for_model]

neutral_dataset = [(tweet_dict, "Neutral")
                            for tweet_dict in neutral_tokens_for_model]

dataset = positive_dataset + negative_dataset + neutral_dataset

random.shuffle(dataset)

train_data = dataset[:25000]
test_data = dataset[5000:]

classifier = nltk.NaiveBayesClassifier.train(train_data)

path = "../model/nltk.NaiveBayesClassifier.pkl"
file = "nltk.NaiveBayesClassifier.pkl"

with open(path, 'wb') as file:  
    pickle.dump(classifier, file)

print("Accuracy is:", classify.accuracy(classifier, test_data))