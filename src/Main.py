import datetime
import os
import time

from ParsingUtility import parse_file
from ParsingUtility import compute_data
from ParsingUtility import diff_prev_day
from ParsingUtility import diff_curr_day
from ParsingUtility import update_file
from ParsingUtility import get_raw_image_path
from ParsingUtility import crop_process_image
from ParsingUtility import read_image
from ParsingUtility import check_date
from ParsingUtility import get_raw_image_dimensions
from ExportUtility import plot_graph
from ExportUtility import plot_triple_graph
from ExportUtility import list_to_csv
from ExportUtility import export_tweets_to_file
from ExportUtility import update_git_repo
from TwitterUtility import load_auth
from TwitterUtility import fetch_image
from TwitterUtility import sleep_until
from TwitterUtility import send_tweet
from TwitterUtility import tweets_generator


start_quarantine = datetime.datetime(2020, 3, 15)

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

    success_input_date = check_date(opt_date)
    if(success_input_date == 1):
        print('Invalid input date. Exiting...')
        return 1

    auth_data = load_auth()
    if(auth_data == 1):
        print('Could not load authenticator file. Exiting...')
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
        crop_process_image(raw_image_path, '../res/raw_images/cases.jpg', (400, 370, 580, 420), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/deaths.jpg', (420, 550, 580, 620), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/tests.jpg', (100, 370, 295, 415), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/recovered.jpg', (100, 570, 290, 630), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (400, 470, 580, 520), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/cases24h.jpg', (180, 180, 500, 310), grescale=True, invert=True, contrast=2.0)
    else:
        crop_process_image(raw_image_path, '../res/raw_images/cases.jpg', (660, 590, 960, 670), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/deaths.jpg', (650, 900, 900, 990), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/tests.jpg', (170, 970, 480, 1050), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/recovered.jpg', (170, 560, 520, 700), grescale=True, invert=False, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (670, 780, 950, 870), grescale=True, invert=True, contrast=2.0)
        crop_process_image(raw_image_path, '../res/raw_images/cases24h.jpg', (150, 160, 530, 310), grescale=True, invert=True, contrast=2.0)
    
    read_image_data = []
    cases = ''.join(c for c in read_image('../res/raw_images/cases.jpg') if c.isdigit())
    deaths = ''.join(c for c in read_image('../res/raw_images/deaths.jpg') if c.isdigit())
    tests = ''.join(c for c in read_image('../res/raw_images/tests.jpg') if c.isdigit())
    recovered = ''.join(c for c in read_image('../res/raw_images/recovered.jpg') if c.isdigit())
    hospitalized = ''.join(c for c in read_image('../res/raw_images/hospitalized.jpg') if c.isdigit())
    cases24h = ''.join(c for c in read_image('../res/raw_images/cases24h.jpg') if c.isdigit())
    os.remove(raw_image_path)

    print('======================================================================')
    print('Message: ', tweet_info[1])
    print('Date: ', opt_date)
    print('Cases: ', cases)
    print('Deaths: ', deaths)
    print('Tests: ', tests)
    print('Recovered: ', recovered)
    print('Hospitalized: ', hospitalized)
    print('Cases 24H: ', cases24h)
    verify = input('Verify the numbers above before continuing. Proceed? [Y/N]: ')
    print('======================================================================')

    if(verify == 'Y' or verify == 'y'):
        pass
    elif(verify == 'N' or verify == 'n'):
        print('Discard readings. Exiting...')
        return 1
    else:
        print('Invalid input. Exiting...')
        return 1
    
    success_csv_write = update_file(opt_date, cases, deaths, tests, recovered, hospitalized)
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

    plot_triple_graph(data[0], data[1], data[18], data[4], 'r', 'b', 'g', "Dias", "# de Casos Confirmados",
        "# de Casos Activos", "# de Recuperados", "Casos Confirmados, Activos y Recuperados de COVID19 en el Peru (acumulado)",
        "conf_act_rec_cumulative.png", opt_date, y_min=0)

    plot_graph(data[0][-30:], data[19][-30:], 'r', "Dias", "Nuevos Casos Activos",
        "Nuevos Casos Activos de COVID19 en el Peru (ultimos 30 dias)", "new_active_cases.png", opt_date)

    plot_graph(data[0][-30:], data[4][-30:], 'g', "Dias", "Recuperados",
        "Recuperados de COVID19 en el Peru (ultimos 30 dias)", "recovered.png", opt_date)

    plot_graph(data[0][-30:], data[20][-30:], 'b', "Dias", "Positividad Diaria (* 100%)",
        "Positividad Diaria de COVID19 en el Peru (ultimos 30 dias)", "perc_daily_positive_tests.png",
        opt_date, y_min=0, y_max=1)
    
    plot_graph(data[0], data[2], 'k', "Dias", "# de Fallecidos", "Fallecidos por COVID19 en el Peru (acumulado)",
        "deaths.png", opt_date, y_min=0)

    plot_graph(data[0][-30:], data[17][-30:], 'k', "Dias", "Tasa de Mortalidad (* 100%)",
        "Tasa de Mortalidad por COVID19 en el Peru (ultimos 30 dias)", "mortality_rate.png", opt_date)

    plot_graph(data[0], data[3], 'b', "Dias", "# de Pruebas", "Pruebas de COVID19 en el Peru (acumulado)",
        "tests.png", opt_date, y_min=0)

    plot_graph(data[0][-30:], data[5][-30:], 'y', "Dias", "# de Hospitalizados", "Hospitalizados por COVID19 en el Peru (ultimos 30 dias)",
        "hospitalized.png", opt_date)
    
    images = [['conf_act_rec_cumulative.png', 'new_active_cases.png', 'recovered.png', 'perc_daily_positive_tests.png'],
            ['deaths.png', 'mortality_rate.png', 'tests.png', 'hospitalized.png']]
    tweets = tweets_generator(data, images, cases24h)
    
    success_send_tweet = send_tweet(auth_data, tweets, tweet_info[0])
    if(success_send_tweet == 1):
        print('Could not authenticate session and send tweets.')
        return 1

    success_tweets_export = export_tweets_to_file(tweets)
    if(success_tweets_export == 1):
        print('Could not reach tweets.dat')
        return 1

    update_git_repo(opt_date)
    
#####################################################################################################################

run()
