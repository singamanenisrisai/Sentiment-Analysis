#!/usr/bin/env python3
import pandas as pnd
dataoutput = pnd.read_csv("tweets.csv")
print(dataoutput)

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag,pos_tag_sents

tweets = dataoutput["text"].map(lambda x: x.lower())
print(tweets)

dataoutput["tweetinput"]=tweets
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
output = SentimentIntensityAnalyzer()

negative=[]
positive=[]
neutral=[]
compound=[]

for tweet in tweets:
    sentiValues = output.polarity_scores(tweet)
    # print(sentiValues["neg"])
    negative.append(sentiValues["neg"])
    positive.append(sentiValues["pos"])
    neutral.append(sentiValues["neu"])
    compound.append(sentiValues["compound"])
    
    # print("{:-<65} {}".format(tweet, str(sentiValues)))
dataoutput["positive"] = positive
dataoutput["neutral"] = neutral
dataoutput["negative"] = negative
dataoutput["compound"] = compound

print(dataoutput)

dataoutput.to_csv("sentiTweets.csv")
