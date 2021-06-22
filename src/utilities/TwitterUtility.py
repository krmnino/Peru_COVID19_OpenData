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
        self.tweet_id = ''
        self.image_paths = []
    
    def set_message(self, msg):
        self.message = msg

    def set_id(self, id):
        self.tweet_id = id

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

    def pattern_search_tweet(self, twitter_user, search_pattern, query_limit):
        found_tweet = False
        ret_tweet = Tweet()
        print('[SEARCH] -> Quering ' + str(query_limit) + ' tweets..')
        tweets = self.api.user_timeline(screen_name=twitter_user, count=query_limit, include_rts=False, include_replies=False, tweet_mode='extended')
        for tweet in tweets:
            if(search_pattern in tweet.full_text):
                ret_tweet.message = tweet.full_text
                ret_tweet.tweet_id = tweet.id
                found_tweet = True
                break
        if(not found_tweet):
            sys.exit('[SEARCH] -> Could not retrieve tweet')
        print()
        return ret_tweet

    def pattern_search_image(self, path, twitter_user, search_pattern, query_limit):
        found_tweet = False
        image_urls = []
        print('[FETCH] -> Quering ' + str(query_limit) + ' tweets..')
        tweets = self.api.user_timeline(screen_name=twitter_user, count=query_limit, include_rts=False, include_replies=False, tweet_mode='extended')
        for tweet in tweets:
            if('media' in tweet.entities and search_pattern in tweet.full_text):
                for media in tweet.extended_entities['media']:
                    image_urls.append(media['media_url'])
                found_tweet = True
                break
        if(not found_tweet):
            sys.exit('[FETCH] -> Could not retrieve tweet')
        for url in image_urls:
            wget.download(url, out=path)
        print()

    def fetch_image_by_id(self, path, tweet):
        print('[FETCH] -> Fetching tweet: ' + str(tweet.tweet_id))
        tweet = self.api.get_status(tweet.tweet_id, tweet_mode='extended')
        image_urls = []
        try:
            for media in tweet.extended_entities['media']:
                image_urls.append(media['media_url'])
        except:
             sys.exit('Could not retrieve tweet')
        for url in image_urls:
            wget.download(url, out=path)
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

    def query_n_tweets(self, twitter_user, query_limit):
        print('[SEARCH] -> Quering ' + str(query_limit) + ' tweets..')
        tweets = self.api.user_timeline(screen_name=twitter_user, count=query_limit, include_rts=False, include_replies=False, tweet_mode='extended')
        out = []
        for tweet in tweets:
            tmp = Tweet()
            tmp.message = tweet.full_text
            tmp.tweet_id = tweet.id
            out.append(tmp)
        for i, tweet in enumerate(out):
            print('%4s'%(i), '%20s'%(tweet.tweet_id), '%64s'%(tweet.message[:58] + '...'))
        return out