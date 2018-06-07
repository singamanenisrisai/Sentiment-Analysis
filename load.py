#!/usr/bin/env python3
import csv
import copy

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(hosts=[{'host':'35.183.29.29','port':'9200'}])

Loadfile = []

def tweets_csv(filename):
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Loadfile.append({
            'Tweets':row[0],
            'SentimentAnalysis':row[1],
            'SentimentScore':row[2]})

tweets_csv("FinalSentiment.csv")

actions = [{"_index":"my_tweets", "_type":"tweets", "_id":i,
            "_source":{'Tweets':Loadfile[i]["Tweets"],'SentimentAnalysis':Loadfile[i]["SentimentAnalysis"],
            'SentimentScore':Loadfile[i]["SentimentScore"], "timestamp":datetime.now()} }
            for i in range(0, len(Loadfile))]

helpers.bulk(es,actions)
