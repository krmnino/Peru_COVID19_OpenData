import tweepy
import wget
import os
import time
import datetime
import pathlib
import sys

sys.path.insert(0, './utilities')
import ConfigUtility as cu

class Tweet:    
    def __init__(self):
        self.message = ''
        self.image_paths = []
    
    def set_message(self, msg):
        self.message = msg

    def add_image(self, path):
        if(len(self.image_paths) >= 4):
            print("Tweet already carries 4 images with it.")
        else:
            self.image_paths.append(path)

class TwitterAPISession:
    def __init__(self, auth_config):
        self.auth_config = tweepy.OAuthHandler(auth_config.get_value('ConsumerKey'), auth_config.get_value('ConsumerSecret'))
        self.auth_config.set_access_token(auth_config.get_value('AccessToken'), auth_config.get_value('AccessSecret'))
        try:
            self.api = tweepy.API(self.auth_config)
            self.inited = True
        except:
            sys.exit('Could not authenticate Twitter API session')

    def query_tweet(self, twitter_user, search_pattern, query_limit):
        found_tweet = False
        query_counter = 1
        tweet_identificator = ''
        while(found_tweet == False and query_counter < query_limit):
            print('[SEARCH] -> Quering tweets...')
            tweets = self.api.user_timeline(screen_name=twitter_user, count=query_counter, include_rts=False, include_replies=False, tweet_mode='extended')
            for tweet in tweets:
                if('media' in tweet.entities and search_pattern in tweet.full_text):
                    tweet_identificator = tweet.id
                    found_tweet = True
                    break
            query_counter += 1
        if(query_counter == 15):
            sys.exit('Could not retrieve tweet')
        return tweet_identificator

    def fetch_image(self, path, twitter_user, search_pattern, query_limit):
        found_tweet = False
        query_counter = 1
        image_url = ''
        while(found_tweet == False and query_counter < query_limit):
            print('[DOWNLOAD] -> Quering tweets...')
            tweets = self.api.user_timeline(screen_name=twitter_user, count=query_counter, include_rts=False, include_replies=False, tweet_mode='extended')
            for tweet in tweets:
                if('media' in tweet.entities and search_pattern in tweet.full_text):
                    for media in tweet.extended_entities['media']:
                        image_url = media['media_url']
                        found_tweet = True
                    break
            query_counter += 1
        if(query_counter == 15):
            sys.exit('Could not retrieve tweet')
        wget.download(image_url, out=path)
        print()

    def reply_thread(self, tweet_identificator, tweets):
        for i in range(0, len(tweets)):
            if(len(tweets[i].image_paths) > 0):
                media_ids = [self.api.media_upload(tweets[i].image_paths[j]).media_id_string for j in range(0, len(tweets[i].image_paths))]
                self.api.update_status(media_ids=media_ids, status=tweets[i].message, in_reply_to_status_id=tweet_identificator, auto_populate_reply_metadata=True)
            else:           
                self.api.update_status(status=tweets[i].message, in_reply_to_status_id=tweet_identificator, auto_populate_reply_metadata=True)
            rply_tweets = self.api.user_timeline(screen_name='krm_nino', count=1, tweet_mode='extended')
            tweet_identificator = rply_tweets[0].id
            print('Sent tweet: ' + str(i + 1) + ' out of ' + str(len(tweets)))
            time.sleep(2)

    def send_thread(self, tweets):
        sent_first_tweet = False
        tweet_identificator = None
        for i in range(0, len(tweets)):
            if len(tweets[i].image_paths) > 0:
                if(not sent_first_tweet):
                    media_ids = [self.api.media_upload(tweets[i].image_paths[j]).media_id_string for j in range(0, len(tweets[i].image_paths))]
                    self.api.update_status(media_ids=media_ids, status=tweets[i].message, auto_populate_reply_metadata=True)
                    sent_first_tweet = True
                else:
                    media_ids = [self.api.media_upload(tweets[i].image_paths[j]).media_id_string for j in range(0, len(tweets[i].image_paths))]
                    self.api.update_status(media_ids=media_ids, status=tweets[i].message, in_reply_to_status_id=tweet_identificator, auto_populate_reply_metadata=True)
            else:
                if(not sent_first_tweet):
                    self.api.update_status(status=tweets[i].message, auto_populate_reply_metadata=True)
                    sent_first_tweet = True
                else:
                    self.api.update_status(status=tweets[i].message, in_reply_to_status_id=tweet_identificator, auto_populate_reply_metadata=True)
            rply_tweets = self.api.user_timeline(screen_name='krm_nino', count=1, tweet_mode='extended')
            tweet_identificator = rply_tweets[0].id
            print('Sent tweet: ' + str(i + 1) + ' out of ' + str(len(tweets)))
            time.sleep(2)
