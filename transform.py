#!/usr/bin/env python3
import pandas as pnd
dataoutput = pnd.read_csv("tweets.csv")
SentiFinal = pnd.DataFrame()

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag,pos_tag_sents

tweets = dataoutput["text"].map(lambda x: x.lower())

dataoutput["tweetinput"]=tweets
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
output = SentimentIntensityAnalyzer()

negative=[]
positive=[]
neutral=[]
compound=[]
sentiAnalysis=[]
sentiScore = []

for tweet in tweets:
    sentiValues = output.polarity_scores(tweet)
    negative.append(sentiValues["neg"])
    positive.append(sentiValues["pos"])
    neutral.append(sentiValues["neu"])
    compound.append(sentiValues["compound"])

    if sentiValues["neg"]>sentiValues["pos"]:
        sentiAnalysis.append("Negative")
        sentiScore.append(sentiValues["neg"])
    elif sentiValues["pos"]>sentiValues["neg"]:
        sentiAnalysis.append("Positive")
        sentiScore.append(sentiValues["pos"])
    else:
        sentiAnalysis.append("Neutral")
        sentiScore.append(sentiValues["neu"])

dataoutput["positive"] = positive
dataoutput["neutral"] = neutral
dataoutput["negative"] = negative
dataoutput["compound"] = compound
dataoutput["SentiAnalysis"] = sentiAnalysis
dataoutput["SentiScore"] = sentiScore

SentiFinal["Tweets"] = dataoutput["tweetinput"]
SentiFinal["SentimentAnalysis"] = dataoutput["SentiAnalysis"]
SentiFinal["SentimentScore"] = dataoutput["SentiScore"]

print(SentiFinal)
print(dataoutput)

SentiFinal.to_csv("FinalSentiment.csv", index=False)
dataoutput.to_csv("sentiTweets.csv", index=False)

