import datetime
import os
import sys
import time

from ParsingUtility import parse_file
from ParsingUtility import compute_data
from ParsingUtility import update_file
from ParsingUtility import get_raw_image_path
from ParsingUtility import crop_process_image
from ParsingUtility import read_image
from ParsingUtility import check_date
from ParsingUtility import get_raw_image_dimensions
from ParsingUtility import clean_dir
from ExportUtility import list_to_csv
from ExportUtility import export_tweets_to_file
from ExportUtility import update_git_repo_win32
from ExportUtility import update_git_repo_linux
from ExportUtility import GraphData
from ExportUtility import plot_loader
from TwitterUtility import load_auth
from TwitterUtility import fetch_image
from TwitterUtility import sleep_until
from TwitterUtility import send_tweet
from TwitterUtility import tweets_generator
from CommandLineUtility import check_data_menu

'''
Structure of parsed_data list after computation
index   contents
0	    Dates
1	    Cases
2	    Deaths
3	    Tests
4       Recovered
5       Hospitalized
6   	Days
7   	New Cases
8	    % Cases
9   	New Deaths
10	    % Deaths
11      New Recovered
12      % Recovered
13      New Hospitalized  
14      % Hospitalized
15	    New Tests
16	    % Tests
17      Mortality Rate
18      Active Cases
19      New Active Cases
20      % Daily Positives
'''

def run(opt_date=datetime.date.today().strftime('%Y-%m-%d')):

    #Include this to Command Line Utility
    success_input_date = check_date(opt_date)
    if(success_input_date == 1):
        print('Invalid input date. Exiting...')
        return 1

    auth_data = load_auth()
    if(auth_data == 1):
        print('Could not load authenticator file. Exiting...')
        return 1

    clean_directory = clean_dir()
    if(clean_directory == 1):
        print('Could not clean raw_images directory. Exiting...')
        return 1

    tweet_info = fetch_image(auth_data) #index 0 = tweet_id, index 1 = tweet_body
    if(tweet_info == 1):
        print('No matching image found. Exiting...')
        return 1

    raw_image_path = get_raw_image_path()
    if(raw_image_path == 1):
        print('Could not retrieve image path. Exiting...')
        return 1

    image_dimensions = get_raw_image_dimensions(raw_image_path)

    #left, up, right, down
    if(image_dimensions[0] < 900 or image_dimensions[1] < 1100):
        crop_process_image(raw_image_path, '../res/raw_images/cases.jpg', (420, 365, 600, 420), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/deaths.jpg', (420, 560, 560, 620), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/tests.jpg', (100, 600, 300, 660), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/recovered.jpg', (90, 360, 325, 445), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (440, 485, 570, 570), grescale=True, invert=True, contrast=1.0)
        crop_process_image(raw_image_path, '../res/raw_images/cases24h.jpg', (100, 110, 290, 200), grescale=True, invert=True, contrast=2.0)
    else:
        crop_process_image(raw_image_path, '../res/raw_images/cases.jpg', (660, 590, 960, 670), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/deaths.jpg', (650, 900, 900, 990), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/tests.jpg', (170, 970, 480, 1050), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/recovered.jpg', (170, 560, 520, 700), grescale=True, invert=False, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (670, 780, 950, 870), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/cases24h.jpg', (150, 160, 530, 310), grescale=True, invert=True, contrast=2.0)
    
    

    # [date, cases, deaths, tests, recovered, hospitalized, cases24h]
    input_data = {\
        'Date' : opt_date,
        'Cases' : read_image('../res/raw_images/cases.jpg'),
        'Deaths' : read_image('../res/raw_images/deaths.jpg'),
        'Tests' : read_image('../res/raw_images/tests.jpg'),
        'Recovered' : read_image('../res/raw_images/recovered.jpg'),
        'Hospitalized' : read_image('../res/raw_images/hospitalized.jpg'),
        'Cases24H' : read_image('../res/raw_images/cases24h.jpg')
    }

    if(check_data_menu(input_data) == 1):
        print('Discard readings. Exiting...')
        return 1
    
    success_csv_write = update_file(input_data)
    if(success_csv_write == 1):
        print('Could not update CSV file.')
        return 1

    raw_data = parse_file()
    if(raw_data == 1):
        print('Could not parse CSV file.')
        return 1
    
    data = compute_data(raw_data)

    success_full_csv_write = list_to_csv(data)
    if(success_full_csv_write == 1):
        print('Could not export processed data.')

    graph_data = [\
        GraphData(  data[0], 
                    [data[1],data[18],data[4],data[2]], 
                    0,
                    'Dias',
                    ['# Casos Confirmados', '# Activos', '# Recuperados', '# Fallecidos'],
                    ['r', 'b', 'g', 'k'],
                    'Casos Confirmados, Activos, Recuperados y Fallecidos de COVID19 en el Peru (acumulado)',
                    20,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'conf_act_rec_dea_cumulative.png',
                    input_data['Date'],
                    False,
                    True,
                    -1,
                    0),
        GraphData(  data[0], 
                    [data[19]], 
                    30,
                    'Dias',
                    ['# de Nuevos Casos Activos'],
                    ['r'],
                    'Nuevos Casos Activos de COVID19 en el Peru (ultimos 30 dias)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'new_active_cases.png',
                    input_data['Date'],
                    True,
                    False,
                    -1,
                    -1),
        GraphData(  data[0], 
                    [data[4]], 
                    30,
                    'Dias',
                    ['Recuperados'],
                    ['g'],
                    'Recuperados de COVID19 en el Peru (ultimos 30 dias)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'recovered.png',
                    input_data['Date'],
                    True,
                    False,
                    -1,
                    -1),
        GraphData(  data[0], 
                    [data[20]], 
                    30,
                    'Dias',
                    ['Positividad Diaria (* 100%)'],
                    ['b'],
                    'Positividad Diaria de COVID19 en el Peru (ultimos 30 dias)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'perc_daily_positive_tests.png',
                    input_data['Date'],
                    True,
                    True,
                    1,
                    0),
        GraphData(  data[0], 
                    [data[2]], 
                    0,
                    'Dias',
                    ['# de Fallecidos'],
                    ['k'],
                    'Fallecidos por COVID19 en el Peru (acumulado)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'deaths.png',
                    input_data['Date'],
                    False,
                    False,
                    -1,
                    0),
        GraphData(  data[0], 
                    [data[17]], 
                    30,
                    'Dias',
                    ['Tasa de Letalidad (* 100%)'],
                    ['k'],
                    'Tasa de Letalidad por COVID19 en el Peru (ultimos 30 dias)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'mortality_rate.png',
                    input_data['Date'],
                    True,
                    False,
                    -1,
                    -1),
        GraphData(  data[0], 
                    [data[3]], 
                    0,
                    'Dias',
                    ['# de Pruebas'],
                    ['b'],
                    'Pruebas de COVID19 en el Peru (acumulado)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'tests.png',
                    input_data['Date'],
                    False,
                    False,
                    -1,
                    0),
        GraphData(  data[0], 
                    [data[5]], 
                    30,
                    'Dias',
                    ['# de Hospitalizados'],
                    ['y'],
                    'Hospitalizados por COVID19 en el Peru (ultimos 30 dias)',
                    25,
                    input_data['Date'] + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
                    'hospitalized.png',
                    input_data['Date'],
                    True,
                    False,
                    -1,
                    -1)
    ]

    plot_loader(graph_data)
        
    images = [[graph_data[i].filename for i in range(0, 4)], [graph_data[i].filename for i in range(4, 8)]]
    tweets = tweets_generator(data, images, input_data['Cases24H'])

    success_send_tweet = send_tweet(auth_data, tweets, tweet_info[0])
    if(success_send_tweet == 1):
        print('Could not authenticate session and send tweets.')
        return 1
    
    success_tweets_export = export_tweets_to_file(tweets)
    if(success_tweets_export == 1):
        print('Could not reach tweets.dat')
        return 1

    clean_directory = clean_dir()
    if(clean_directory == 1):
        print('Could not clean raw_images directory. Exiting...')
        return 1

    if(sys.platform == 'win32'):
        update_git_repo_win32(input_data['Date'])
    else:
        update_git_repo_linux(input_data['Date'])

#####################################################################################################################

run()
