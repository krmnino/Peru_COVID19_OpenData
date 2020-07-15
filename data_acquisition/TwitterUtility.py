import tweepy
import wget
import os
import time
import datetime
import pathlib

def load_auth():
    '''
    idx  contents
    0    consumer_key
    1    consumer_secret
    2    access_token
    3    access_secret
    '''
    auth_data = []
    try:
        open('auth.dat', 'r')
    except:
        return 1
    else:
        with open('auth.dat', 'r') as file:
            for line in file:
                auth_data.append(line[:len(line)-1])
        file.close()
    return auth_data

def fetch_images(auth_data):
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    api = tweepy.API(auth)
    path = str(pathlib.Path().absolute()) + '/raw_images'
    tweets = api.user_timeline(screen_name='Minsa_Peru', count=5, include_rts=False, include_replies=False, tweet_mode='extended')
    image_urls = []
    tweet_date = ''
    tweet_identificator = ''
    for tweet in tweets:
        if('media' in tweet.entities and 'Sala situacional' in tweet.full_text):
            tweet_date = tweet.created_at.strftime("%Y-%m-%d")
            tweet_identificator = tweet.id
            for media in tweet.extended_entities['media']:
                image_urls.append(media['media_url'])
    if(len(image_urls) == 0):
        return 1
    for media_file in image_urls:
        wget.download(media_file, path)
        print()
        return (tweet_date, tweet_identificator)


def send_tweet(auth_data, tweet_contents, tweet_identificator, images):
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    api = tweepy.API(auth)
    image_prefix_path = str(pathlib.Path().absolute())
    image_prefix_path = image_prefix_path[:image_prefix_path.rfind('/')] + '/graphs/'
    for i in range(0, 4):
        if (i != 3):
            media_ids = [api.media_upload(image_prefix_path + j).media_id_string  for j in images[i]]
            api.update_status(media_ids=media_ids, status=tweet_contents[i], in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
            rply_tweets = api.user_timeline(screen_name='krm_nino', count=1, tweet_mode='extended')
            tweet_identificator = rply_tweets[0].id
        else:
            api.update_status(status=tweet_contents[i], in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
        print('Sent tweet: ' + str(i + 1) + ' out of 4')
        time.sleep(i + 2)

def sleep_until(tweet_date):
    tomorrow = datetime.datetime.strptime(tweet_date, '%Y-%m-%d') + datetime.timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d') + ' 15:00:00'
    delta_time = datetime.datetime.strptime(tomorrow_str, '%Y-%m-%d %H:%M:%S') - datetime.datetime.now()
    return delta_time
