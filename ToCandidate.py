#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.mentions(q="@any twitter account",count=200)

    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.mentions(q="@any twitter account",count=200)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, tweet.favorite_count,tweet.user.name] for tweet in alltweets]


    name='%s_tweets_to' + organizacion +  '.csv'
    FILE=open(name % screen_name, 'w')
    writer = csv.writer(FILE)
    writer.writerow(["id", "created_at", "text","retweets","favorites","user"])
    writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    organizacion=""
    get_all_tweets(organizacion)
    
    