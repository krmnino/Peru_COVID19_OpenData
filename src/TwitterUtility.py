import tweepy
import wget
import os
import time
import datetime
import pathlib
import sys

class Tweet:
    message = ''
    image_paths = []
    
    def __init__(self):
        pass

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
    path = str(pathlib.Path().absolute()).replace('\\', '/')
    path = path[:path.rfind('/')] + '/res/raw_images/'
    found_tweet = False
    query_tweets = 0
    tweet_identificator = ''
    tweet_message = ''
    image_url = ''
    while(found_tweet == False and query_tweets < 15):
        print('Quering tweets...')
        tweets = api.user_timeline(screen_name='Minsa_Peru', count=query_tweets, include_rts=False, include_replies=False, tweet_mode='extended')
        for tweet in tweets:
            if('media' in tweet.entities and 'Esta es la' in tweet.full_text):
                tweet_identificator = tweet.id
                tweet_message = tweet.full_text
                for media in tweet.extended_entities['media']:
                    image_url = media['media_url']
                    found_tweet = True
                break
        query_tweets += 1
    if(query_tweets == 15):
        return 1
    print()
    wget.download(image_url, out=path)
    return (tweet_identificator, tweet_message)

def tweets_generator(data, image_paths, cases24hrs):
    # Generate tweet message with data summary
    lines = []

    out = ''
    out += u'\U0001F534 Casos: ' + str(int(data[1][len(data[0])-1])) \
        if data[7][len(data[0])-1] >= data[7][len(data[0])-2] \
        else u'\U0001F7E2 Casos: ' + str(int(data[1][len(data[1])-1]))
    out += ' (+' + str(int(data[7][len(data[0])-1])) + ')\n'
    out += ' -> (ultimos 7-dias: ' + str(int(data[7][len(data[0])-1]) - int(cases24hrs)) \
            + ') + (ultimas 24-horas: ' + str(cases24hrs) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Activos: ' + str(int(data[18][len(data[0])-1])) \
        if data[19][len(data[0])-1] >= data[19][len(data[0])-2] \
        else u'\U0001F7E2 Activos: ' + str(int(data[18][len(data[0])-1]))
    out += ' (+' + str(int(data[19][len(data[0])-1])) + ')\n' \
        if data[19][len(data[0])-1] > 0 \
        else ' (' + str(int(data[19][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F7E2 Recuperados: ' + str(int(data[4][len(data[0])-1])) \
        if data[11][len(data[0])-1] >= data[11][len(data[0])-2] \
        else u'\U0001F534 Recuperados: ' + str(int(data[4][len(data[0])-1]))
    out += ' (+' + str(int(data[11][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Hospitalizados: ' + str(int(data[5][len(data[0])-1])) \
        if data[13][len(data[0])-1] > 0 \
        else u'\U0001F7E2 Hospitalizados: ' + str(int(data[5][len(data[0])-1]))
    out += ' (+' + str(int(data[13][len(data[0])-1])) + ')\n' \
        if data[13][len(data[0])-1] > 0 \
        else ' (' + str(int(data[13][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Fallecidos: ' + str(int(data[2][len(data[0])-1])) \
        if data[9][len(data[0])-1] >= data[9][len(data[0])-2] \
        else u'\U0001F7E2 Fallecidos: ' + str(int(data[2][len(data[1])-1]))
    out += ' (+' + str(int(data[9][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Tasa Letalidad: ' + str(round(data[17][len(data[0])-1] * 100, 4)) + '%' \
        if data[17][len(data[0])-1] >= data[17][len(data[0])-2] \
        else u'\U0001F7E2 Tasa Letalidad: ' + str(round(data[17][len(data[0])-1] * 100, 4)) + '%'
    out += ' (+' + str(round((data[17][len(data[0])-1] - data[17][len(data[0])-2]) * 100, 4)) + '%)\n' \
        if data[17][len(data[0])-1] - data[17][len(data[0])-2] > 0 \
        else ' (' + str(round((data[17][len(data[0])-1] - data[17][len(data[0])-2]) * 100, 4)) + '%)\n'
    lines.append(out)

    out = ''
    out += u'\U0001F7E2 Pruebas (PM+PR+AG): ' + str(int(data[3][len(data[0])-1])) \
        if data[15][len(data[0])-1] >= data[15][len(data[0])-2] \
        else u'\U0001F534 Pruebas (PM+PR+AG): ' + str(int(data[3][len(data[1])-1]))
    out += ' (+' + str(int(data[15][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Positividad Diaria: ' + str(round(data[20][len(data[0])-1] * 100, 2)) + '%' \
        if data[20][len(data[0])-1] >= data[20][len(data[0])-2] \
        else u'\U0001F7E2 Positividad Diaria: ' + str(round(data[20][len(data[0])-1] * 100, 2)) + '%'
    out += ' (+' + str(round((data[20][len(data[0])-1] - data[20][len(data[0])-2]) * 100, 2)) + '%)\n' \
        if data[20][len(data[0])-1] - data[20][len(data[0])-2] > 0 \
        else ' (' + str(round((data[20][len(data[0])-1] - data[20][len(data[0])-2]) * 100, 2)) + '%)\n'
    lines.append(out)

    # Generate Tweet objects: first 2 carry data, last one links to repo
    tweets = [Tweet(), Tweet(), Tweet()]
    tweets[0].message = 'ANALISIS DIARIO del #COVID19 en #PERU (1/2)\n'
    tweets[0].message += lines[0]
    tweets[0].message += lines[1]
    tweets[0].message += lines[2]
    tweets[0].message += lines[3]
    tweets[0].image_paths = image_paths[0]
    
    tweets[1].message = 'ANALISIS DIARIO del #COVID19 en #PERU (2/2)\n'
    tweets[1].message += lines[4] 
    tweets[1].message += lines[5] 
    tweets[1].message += lines[6] 
    tweets[1].message += lines[7]
    tweets[1].image_paths = image_paths[1]

    tweets[2].message = 'Repositorio de datos sobre el #COVID19 en #Peru actualizado al dia ' + data[0][len(data[0]) - 1] + '\n'
    tweets[2].message += 'Sugerencias son bienvenidas!\n'
    tweets[2].message += u'\U0001F4C8' + ' Disponible en formato .CSV y .JSON\n'
    tweets[2].message += u'\U0001F30E' + ' WEB https://peru-covid19.com/\n'

    return tweets

def send_thread(auth_data, tweets):
    tweet_identificator = ''
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    try:
        api = tweepy.API(auth)
    except:
        return 1
    image_prefix_path = str(pathlib.Path().absolute()).replace('\\', '/')
    image_prefix_path = image_prefix_path[:image_prefix_path.rfind('/')] + '/res/graphs/'
    sent_first_tweet = False
    for i in range(0, len(tweets)):
        if len(tweets[i].image_paths) > 0:
            media_ids = [api.media_upload(image_prefix_path + j).media_id_string for j in tweets[i].image_paths]
            api.update_status(media_ids=media_ids, status=tweets[i].message, in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
        else:
            if(not sent_first_tweet):
                api.update_status(status=tweets[i].message, auto_populate_reply_metadata=True)
            else:
                api.update_status(status=tweets[i].message, in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
        rply_tweets = api.user_timeline(screen_name='krm_nino', count=1, tweet_mode='extended')
        tweet_identificator = rply_tweets[0].id
        print('Sent tweet: ' + str(i + 1) + ' out of 3')
        time.sleep(2)
    return 0

def reply_thread(auth_data, tweets, tweet_identificator):
    auth = tweepy.OAuthHandler(auth_data[0], auth_data[1])
    auth.set_access_token(auth_data[2], auth_data[3])
    try:
        api = tweepy.API(auth)
    except:
        return 1
    image_prefix_path = str(pathlib.Path().absolute()).replace('\\', '/')
    image_prefix_path = image_prefix_path[:image_prefix_path.rfind('/')] + '/res/graphs/'
    for i in range(0, len(tweets)):
        if len(tweets[i].image_paths) > 0:
            media_ids = [api.media_upload(image_prefix_path + j).media_id_string for j in tweets[i].image_paths]
            api.update_status(media_ids=media_ids, status=tweets[i].message, in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
        else:           
            api.update_status(status=tweets[i].message, in_reply_to_status_id = tweet_identificator, auto_populate_reply_metadata=True)
        rply_tweets = api.user_timeline(screen_name='krm_nino', count=1, tweet_mode='extended')
        tweet_identificator = rply_tweets[0].id
        print('Sent tweet: ' + str(i + 1) + ' out of 3')
        time.sleep(2)
    return 0

def sleep_until(tweet_date):
    tomorrow = datetime.datetime.strptime(tweet_date, '%Y-%m-%d') + datetime.timedelta(days=1)
    tomorrow_str = tomorrow.strftime('%Y-%m-%d') + ' 15:00:00'
    delta_time = datetime.datetime.strptime(tomorrow_str, '%Y-%m-%d %H:%M:%S') - datetime.datetime.now()
    return delta_time
