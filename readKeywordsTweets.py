#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv


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

    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.search(q="(kewords here)",count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)
    print(alltweets[-1].id)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))
        #count+=1
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.search(q="(keywords here)", count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, tweet.favorite_count,tweet.user.name] for tweet in alltweets]
    print(outtweets.count)
    str1=screen_name
    organizacion = ''.join(str(e) for e in str1)
    name = '%s_tweets_' + organizacion + '.csv'
    FILE = open(name % screen_name, 'w')
    writer = csv.writer(FILE)
    writer.writerow(["id", "created_at", "text","retweets","favorites","user"])
    writer.writerows(outtweets)


    pass


if __name__ == '__main__':
    organizacion = ["keywoardtest-drugs"]
    get_all_tweets(organizacion)

