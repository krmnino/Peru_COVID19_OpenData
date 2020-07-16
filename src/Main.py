import datetime
import os
import time

from ParseData import parse_file
from ParseData import compute_data
from ParseData import diff_prev_day
from ParseData import diff_curr_day
from ParseData import update_file
from ParseData import get_raw_image_path
from ParseData import crop_image
from ParseData import read_image
from ExportUtility import plot_graph
from ExportUtility import plot_triple_graph
from ExportUtility import list_to_csv
from ExportUtility import tweet_highlights
from ExportUtility import tweet_deaths
from ExportUtility import tweet_tests_hosp_rec
from ExportUtility import tweet_repo
from ExportUtility import export_tweets_to_file
from ExportUtility import update_git_repo
from ExportUtility import generate_JSON_files
from TwitterUtility import load_auth
from TwitterUtility import fetch_images
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

def run(loop=True):
    while(True):
        auth_data = load_auth()
        if(auth_data == 1):
            print('Could not load authenticator file. Waiting 60 seconds...')
            time.sleep(60)
            continue
        tweet_info = fetch_images(auth_data) #index 0 = date, index 1 = url
        if(tweet_info == 1 and loop == False):
            print('Not matching image found. Exiting...')
            break
        if(tweet_info == 1 and loop == True):
            print('Not matching image found. Waiting 60 seconds...')
            time.sleep(60)
            continue
        raw_image_path = get_raw_image_path()
        if(raw_image_path != 1):
            crop_image(raw_image_path, '../res/raw_images/cases.jpg', (120, 360, 404, 440), grescale=True, contrast=2.0)
            crop_image(raw_image_path, '../res/raw_images/deaths.jpg', (175, 800, 470, 920), grescale=True, contrast=2.0)
            crop_image(raw_image_path, '../res/raw_images/tests.jpg', (650, 310, 970, 430), grescale=True, invert=True, contrast=3.5)
            crop_image(raw_image_path, '../res/raw_images/recovered.jpg', (180, 700, 480, 820), grescale=True, invert=True, contrast=4.0)
            crop_image(raw_image_path, '../res/raw_images/hospitalized.jpg', (690, 710, 955, 830), grescale=True, invert=True, contrast=2.5)

            cases = ''.join(c for c in read_image('../res/raw_images/cases.jpg') if c.isdigit())
            deaths = ''.join(c for c in read_image('../res/raw_images/deaths.jpg') if c.isdigit())
            tests = ''.join(c for c in read_image('../res/raw_images/tests.jpg') if c.isdigit())
            recovered = ''.join(c for c in read_image('../res/raw_images/recovered.jpg') if c.isdigit())
            hospitalized = ''.join(c for c in read_image('../res/raw_images/hospitalized.jpg') if c.isdigit())

            os.remove(raw_image_path)
            if(update_file(tweet_info[0], cases, deaths, tests, recovered, hospitalized)):
                print(tweet_info[0] + ': CSV updated successfully')

                generate_JSON_files()

                raw_data = parse_file()
                data = compute_data(raw_data)
                prev_day = diff_prev_day(data)
                curr_day = diff_curr_day(data)
                list_to_csv(data)
                
                plot_triple_graph(data[6], data[1], data[18], data[4], 'r', 'b', 'g', "Dias", "# de Casos Confirmados",
                    "# de Casos Activos", "# de Recuperados", "Casos Confirmados, Activos y Recuperados de COVID19 en el Peru (cumulativo)",
                    "conf_act_rec_cumulative.png", data[0][len(data[0])-1], x_min=0, y_min=0)
                
                plot_graph(data[6][-30:], data[8][-30:], 'r', "Dias", "Casos: Tasa de Crecimiento (* 100% - 100%)",
                    "Tasa de Crecimiento: Casos de COVID19 en el Peru (ultimos 30 dias)", "gf_cases.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_triple_graph(data[6][-30:], data[1][-30:], data[18][-30:], data[4][-30:], 'r', 'b', 'g', "Dias",
                    "# de Casos Confirmados", "# de Casos Activos", "# de Recuperados", "Casos Confirmados, Activos y Recuperados de COVID19 en el Peru (ultimos 30 dias)",
                    "conf_act_rec_days.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_graph(data[6][-30:], data[19][-30:], 'r', "Dias", "Nuevos Casos Activos",
                    "Nuevos Casos Activos de COVID19 en el Peru (ultimos 30 dias)", "new_active_cases.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_graph(data[6], data[2], 'k', "Dias", "# de Fallecidos", "Fallecidos por COVID19 en el Peru (cumulativo)",
                    "deaths.png", data[0][len(data[0])-1], x_min=0, y_min=0)
                
                plot_graph(data[6][-30:], data[10][-30:], 'k', "Dias", "Fallecidos: Tasa de Crecimiento (* 100% - 100%)",
                    "Tasa de Crecimiento: Fallecidos por COVID19 en el Peru (ultimos 30 dias)", "gf_deaths.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_graph(data[6][-30:], data[17][-30:], 'k', "Dias", "Tasa de Mortalidad (* 100%)",
                    "Tasa de Mortalidad por COVID19 en el Peru (ultimos 30 dias)", "mortality_rate.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_graph(data[6], data[3], 'b', "Dias", "# de Pruebas", "Pruebas de COVID19 en el Peru (cumulativo)",
                    "tests.png", data[0][len(data[0])-1], x_min=0, y_min=0)
                
                plot_graph(data[6][-30:], data[20][-30:], 'b', "Dias", "% de Pruebas Positivas Diarias (* 100%)",
                    "% de Pruebas Positivas Diarias de COVID19 en el Peru (ultimos 30 dias)", "perc_daily_positive_tests.png",
                    data[0][len(data[0])-1], x_min=data[6][-30], y_min=0, y_max=1)
                
                plot_graph(data[6][-30:], data[12][-30:], 'g', "Dias", "Recuperados : Tasa de Crecimiento (* 100% - 100%)",
                    "Tasa de Crecimiento: Recuperados de COVID19 en el Peru (ultimos 30 dias)", "gf_recovered.png", data[0][len(data[0])-1], x_min=data[6][-30])
                
                plot_graph(data[6][-30:], data[5][-30:], 'y', "Dias", "# de Hospitalizados", "Hospitalizados por COVID19 en el Peru (ultimos 30 dias)",
                    "hospitalized.png", data[0][len(data[0])-1], x_min=data[6][-30])
                tweets = []
                images = [['conf_act_rec_cumulative.png', 'gf_cases.png', 'conf_act_rec_days.png', 'new_active_cases.png'],
                        ['deaths.png', 'gf_deaths.png', 'mortality_rate.png'],
                        ['tests.png', 'perc_daily_positive_tests.png', 'gf_recovered.png', 'hospitalized.png']]
                tweets.append(tweet_highlights(prev_day, curr_day, data)) 
                tweets.append(tweet_deaths(prev_day, curr_day, data)) 
                tweets.append(tweet_tests_hosp_rec(prev_day, curr_day, data))
                tweets.append(tweet_repo(tweet_info[0]))
                if(export_tweets_to_file(tweets) == 0):
                    print('Tweets contents successfully exported in tweets.dat')
                send_tweet(auth_data, tweets, tweet_info[1], images)
                update_git_repo(tweet_info[0])
                if(loop == False):
                    break

                delta_time = sleep_until(tweet_info[0])
                print('Program will resume in ' + str(delta_time) + '(' + str(delta_time.seconds) + ' seconds)')
                time.sleep(delta_time.seconds)
            else:
                print('Could not update CSV file. Waiting 60 seconds...')
                time.sleep(60)
                continue
        else:
            print('Could not find fetched image from Twitter. Waiting 60 seconds...')
            time.sleep(60)


#####################################################################################################################

run(loop=False)
