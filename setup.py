#!/usr/bin/env python3
import csv
import tweepy
import time
import json

consumer_key = "0yYMSho1hT7DK0nGJfBLrRMfB"
consumer_secret = "XyBolxFugaxVbYswvAsEuEQMgktJdlGnKTlPfAn0bh7iAFbz7O"

access_key = "1000025244453822464-yFQm6l10brepAqDxDR4cFWoY4qBULb"
access_secret = "8KQQJu5XxnieXg0eRwz6Ax8kpEAz8zj6PKgF7e05HEcE4"

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api= tweepy.API(auth)

def get_profile(screen_name):
	api = tweepy.API(auth)
	try:
		user_profile = api.get_user(screen_name)
	except tweepy.error.TweepError as e:
		user_profile = json.loads(e.response.text)

	return user_profile

output = get_profile("realDonaldTrump")

def get_tweets(query):
	api = tweepy.API(auth)

	try:
		tweets = api.search(query)

	except tweepy.error.TweepError as e:
		tweets = [json.loads(e.response.text)]
	return tweets

queries = ["#hate", "#Deadpool2", "#Marvel", "#DonaldTrump", "#JustinTrudeau", "#Spiderman", "#Ironman", "#Batman", "#CaptainAmerica"]

with open ('tweets.csv', 'w') as outfile:

	writer = csv.writer(outfile)
	writer.writerow(['id','user','created_at','text'])
	for query in queries:
		twts = get_tweets(query)
		for tweet in twts:
			writer.writerow([tweet.id_str, tweet.user.screen_name,tweet.created_at,tweet.text])
			print (tweet)
