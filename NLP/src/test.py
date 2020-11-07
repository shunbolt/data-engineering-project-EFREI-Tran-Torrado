from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import re, string, random, nltk, pickle, argparse

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

# get argument for the model
def parse_args():
    parser = argparse.ArgumentParser(description="Sentence analysis")
    parser.add_argument(
        "--sentence",
        default="I'm happy",
        help="Send a sentence to predict if the sentence is positive, negative or neutral (default: I'm happy)",
    )
    return parser.parse_args()

args = parse_args() 

path = "../model/nltk.NaiveBayesClassifier.pkl"
file = "nltk-NaiveBayesClassifier.pkl"

# Load the Model back from file
with open(path, 'rb') as file:  
    classifier = pickle.load(file)

    
custom_tweet = str(args)

custom_tokens = remove_noise(word_tokenize(custom_tweet))

print(classifier.classify(dict([token, True] for token in custom_tokens)))