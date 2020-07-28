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

def fetch_image(auth_data):
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    api = tweepy.API(auth)
    path = str(pathlib.Path().absolute())
    path = path[:path.rfind('/')] + '/res/raw_images/'
    found_tweet = False
    query_tweets = 1
    tweet_identificator = ''
    tweet_message = ''
    image_urls = []
    while(found_tweet == False and query_tweets <= 15):
        tweets = api.user_timeline(screen_name='Minsa_Peru', count=query_tweets, include_rts=False, include_replies=False, tweet_mode='extended')
        for tweet in tweets:
            if('media' in tweet.entities and 'Esta es la situación del #COVID19' in tweet.full_text):
                tweet_identificator = tweet.id
                tweet_message = tweet.full_text
                for media in tweet.extended_entities['media']:
                    image_urls.append(media['media_url'])
                    found_tweet = True
                break
        print('Quering tweets...')
        query_tweets += 1
    if(query_tweets == 15):
        return 1
    for media_file in image_urls:
        wget.download(media_file, path)
        print()
        return (tweet_identificator, tweet_message)

def send_tweet(auth_data, tweet_contents, tweet_identificator, images):
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    try:
        api = tweepy.API(auth)
    except:
        return 1
    image_prefix_path = str(pathlib.Path().absolute())
    image_prefix_path = image_prefix_path[:image_prefix_path.rfind('/')] + '/res/graphs/'
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
    return 0

def sleep_until(tweet_date):
    tomorrow = datetime.datetime.strptime(tweet_date, '%Y-%m-%d') + datetime.timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d') + ' 15:00:00'
    delta_time = datetime.datetime.strptime(tomorrow_str, '%Y-%m-%d %H:%M:%S') - datetime.datetime.now()
    return delta_time
