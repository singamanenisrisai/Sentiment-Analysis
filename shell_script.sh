#!/bin/sh

echo Running First Program

python3 setup.py

echo First Program Executed Successsfully.
echo Captured Tweets
echo Executing Second Script

python3 transform.py

echo Second Script executed successfully
echo Sentiment Analysis Done
echo Uploading tweets into Elasticsearch

python3 load.py

echo Executed Shell script successfully
