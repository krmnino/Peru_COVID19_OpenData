import datetime
import os
import time

from ParseData import parse_file
from ParseData import compute_data
from ParseData import diff_prev_day
from ParseData import diff_curr_day
from ParseData import update_file
from ParseData import get_raw_image_path
from ParseData import crop_process_image
from ParseData import read_image
from ParseData import check_date
from ExportUtility import plot_graph
from ExportUtility import plot_triple_graph
from ExportUtility import list_to_csv
from ExportUtility import tweet_highlights
from ExportUtility import tweet_deaths
from ExportUtility import tweet_tests_hosp_rec
from ExportUtility import tweet_repo
from ExportUtility import export_tweets_to_file
from ExportUtility import update_git_repo
from TwitterUtility import load_auth
from TwitterUtility import fetch_image
from TwitterUtility import sleep_until
from TwitterUtility import send_tweet


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

    crop_process_image(raw_image_path, '../res/raw_images/cases.jpg', (120, 360, 420, 440), grescale=True, contrast=2.0)
    crop_process_image(raw_image_path, '../res/raw_images/deaths.jpg', (175, 800, 460, 920), grescale=True, contrast=2.0)
    crop_process_image(raw_image_path, '../res/raw_images/tests.jpg', (650, 330, 970, 430), grescale=True, invert=True, contrast=4.0)
    crop_process_image(raw_image_path, '../res/raw_images/recovered.jpg', (180, 700, 450, 820), grescale=True, invert=True, contrast=2.5)
    crop_process_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (690, 710, 955, 830), grescale=True, invert=True, contrast=2.5)
    read_image_data = []
    cases = ''.join(c for c in read_image('../res/raw_images/cases.jpg') if c.isdigit())
    deaths = ''.join(c for c in read_image('../res/raw_images/deaths.jpg') if c.isdigit())
    tests = ''.join(c for c in read_image('../res/raw_images/tests.jpg') if c.isdigit())
    recovered = ''.join(c for c in read_image('../res/raw_images/recovered.jpg') if c.isdigit())
    hospitalized = ''.join(c for c in read_image('../res/raw_images/hospitalized.jpg') if c.isdigit())
    os.remove(raw_image_path)

    print('======================================================================')
    print('Message: ', tweet_info[1])
    print('Date: ', opt_date)
    print('Cases: ', cases)
    print('Deaths: ', deaths)
    print('Tests: ', tests)
    print('Recovered: ', recovered)
    print('Hospitalized: ', hospitalized)
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
    prev_day = diff_prev_day(data)
    curr_day = diff_curr_day(data)

    success_full_csv_write = list_to_csv(data)
    if(success_full_csv_write == 1):
        print('Could not export processed data.')

    plot_triple_graph(data[0], data[1], data[18], data[4], 'r', 'b', 'g', "Dias", "# de Casos Confirmados",
        "# de Casos Activos", "# de Recuperados", "Casos Confirmados, Activos y Recuperados de COVID19 en el Peru (acumulado)",
        "conf_act_rec_cumulative.png", opt_date, y_min=0)
    
    plot_graph(data[0][-30:], data[8][-30:], 'r', "Dias", "Casos: Tasa de Crecimiento (* 100% - 100%)",
        "Tasa de Crecimiento: Casos de COVID19 en el Peru (ultimos 30 dias)", "gf_cases.png", opt_date)
    
    plot_triple_graph(data[0][-30:], data[1][-30:], data[18][-30:], data[4][-30:], 'r', 'b', 'g', "Dias",
        "# de Casos Confirmados", "# de Casos Activos", "# de Recuperados", "Casos Confirmados, Activos y Recuperados de COVID19 en el Peru (ultimos 30 dias)",
        "conf_act_rec_days.png", opt_date)
    
    plot_graph(data[0][-30:], data[19][-30:], 'r', "Dias", "Nuevos Casos Activos",
        "Nuevos Casos Activos de COVID19 en el Peru (ultimos 30 dias)", "new_active_cases.png", opt_date)
    
    plot_graph(data[0], data[2], 'k', "Dias", "# de Fallecidos", "Fallecidos por COVID19 en el Peru (acumulado)",
        "deaths.png", opt_date, y_min=0)
    
    plot_graph(data[0][-30:], data[10][-30:], 'k', "Dias", "Fallecidos: Tasa de Crecimiento (* 100% - 100%)",
        "Tasa de Crecimiento: Fallecidos por COVID19 en el Peru (ultimos 30 dias)", "gf_deaths.png", opt_date)
    
    plot_graph(data[0][-30:], data[17][-30:], 'k', "Dias", "Tasa de Mortalidad (* 100%)",
        "Tasa de Mortalidad por COVID19 en el Peru (ultimos 30 dias)", "mortality_rate.png", opt_date)
    
    plot_graph(data[0], data[3], 'b', "Dias", "# de Pruebas", "Pruebas de COVID19 en el Peru (acumulado)",
        "tests.png", opt_date, y_min=0)
    
    plot_graph(data[0][-30:], data[20][-30:], 'b', "Dias", "% de Pruebas Positivas Diarias (* 100%)",
        "% de Pruebas Positivas Diarias de COVID19 en el Peru (ultimos 30 dias)", "perc_daily_positive_tests.png",
        opt_date, y_min=0, y_max=1)
    
    plot_graph(data[0][-30:], data[12][-30:], 'g', "Dias", "Recuperados : Tasa de Crecimiento (* 100% - 100%)",
        "Tasa de Crecimiento: Recuperados de COVID19 en el Peru (ultimos 30 dias)", "gf_recovered.png", opt_date)
    
    plot_graph(data[0][-30:], data[5][-30:], 'y', "Dias", "# de Hospitalizados", "Hospitalizados por COVID19 en el Peru (ultimos 30 dias)",
        "hospitalized.png", opt_date)
    
    tweets = []
    images = [['conf_act_rec_cumulative.png', 'gf_cases.png', 'conf_act_rec_days.png', 'new_active_cases.png'],
            ['deaths.png', 'gf_deaths.png', 'mortality_rate.png'],
            ['tests.png', 'perc_daily_positive_tests.png', 'gf_recovered.png', 'hospitalized.png']]
    tweets.append(tweet_highlights(prev_day, curr_day, data)) 
    tweets.append(tweet_deaths(prev_day, curr_day, data)) 
    tweets.append(tweet_tests_hosp_rec(prev_day, curr_day, data))
    tweets.append(tweet_repo(opt_date))

    success_tweets_export = export_tweets_to_file(tweets)
    if(success_tweets_export == 1):
        print('Could not reach tweets.dat')
        return 1

    '''
    success_send_tweet = send_tweet(auth_data, tweets, tweet_info[0], images)
    if(success_send_tweet == 1):
        print('Could not authenticate session and send tweets.')
        return 1

    update_git_repo(opt_date)
    '''
#####################################################################################################################

run()
