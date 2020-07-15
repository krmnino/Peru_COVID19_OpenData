import datetime
import os
import time

from ParseData import parse_file
from ParseData import compute_data
from ParseData import diff_prev_day
from ParseData import diff_curr_day
from ParseData import update_file
from ExportUtility import plot_graph
from ExportUtility import list_to_csv
from ExportUtility import tweet_highlights
from ExportUtility import tweet_deaths
from ExportUtility import tweet_tests_hosp_rec
from ExportUtility import tweet_repo
from ExportUtility import export_tweets
from TweetAcquisitionUtility import load_auth
from TweetAcquisitionUtility import fetch_images
from TweetAcquisitionUtility import get_raw_image_path
from TweetAcquisitionUtility import crop_image
from TweetAcquisitionUtility import read_image
from TweetAcquisitionUtility import sleep_until

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
            break
        tweet_date = fetch_images(auth_data)
        if(tweet_date == 1):
            break
        raw_image_path = get_raw_image_path()

        if(raw_image_path != 1):
            crop_image(raw_image_path, 'raw_images/cases.jpg', (120, 360, 404, 440), grescale=True, contrast=2.0)
            crop_image(raw_image_path, 'raw_images/deaths.jpg', (175, 800, 470, 920), grescale=True, contrast=2.0)
            crop_image(raw_image_path, 'raw_images/tests.jpg', (650, 310, 970, 430), grescale=True, invert=True, contrast=3.5)
            crop_image(raw_image_path, 'raw_images/recovered.jpg', (180, 700, 480, 820), grescale=True, invert=True, contrast=4.0)
            crop_image(raw_image_path, 'raw_images/hospitalized.jpg', (690, 710, 955, 830), grescale=True, invert=True, contrast=2.5)

            cases = ''.join(c for c in read_image('raw_images/cases.jpg') if c.isdigit())
            deaths = ''.join(c for c in read_image('raw_images/deaths.jpg') if c.isdigit())
            tests = ''.join(c for c in read_image('raw_images/tests.jpg') if c.isdigit())
            recovered = ''.join(c for c in read_image('raw_images/recovered.jpg') if c.isdigit())
            hospitalized = ''.join(c for c in read_image('raw_images/hospitalized.jpg') if c.isdigit())

            os.remove(raw_image_path)
            if(update_file(tweet_date, cases, deaths, tests, recovered, hospitalized)):
                print(tweet_date + ': CSV updated successfully')
                raw_data = parse_file()
                data = compute_data(raw_data)
                prev_day = diff_prev_day(data)
                curr_day = diff_curr_day(data)
                list_to_csv(data)
                plot_graph(data[6], data[1], 'r', "Dias", "# de Casos",
                    "Casos de COVID19 en el Peru: cumulativo", "cases.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[8][-30:], 'r', "Dias", "Casos: Tasa de Crecimiento",
                    "Tasa de Crecimiento de Casos de COVID19 en el Peru: ultimos 30 dias", "gf_cases.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[19][-30:], 'r', "Dias", "Casos Activos",
                    "Casos Activos de COVID19 en el Peru: ultimos 30 dias", "active_cases.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[19][-30:], 'r', "Dias", "Nuevos Casos Activos",
                    "Nuevos Casos Activos de COVID19 en el Peru: ultimos 30 dias", "new_active_cases.png", data[0][len(data[0])-1])
                plot_graph(data[6], data[2], 'k', "Dias", "# de Muertes",
                    "Muertes por COVID19 en el Peru: cumulativo", "deaths.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[10][-30:], 'k', "Dias", "Muertes: Tasa de Crecimiento",
                    "Tasa de Crecimiento de Muertes por COVID19 en el Peru: ultimos 30 dias", "gf_deaths.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[17][-30:], 'k', "Dias", "Tasa de Mortalidad",
                    "Tasa de Mortalidad por COVID19 en el Peru: ultimos 30 dias", "mortality_rate.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[3][-30:], 'b', "Dias", "# de Pruebas",
                    "Pruebas de COVID19 en el Peru: ultimos 30 dias", "tests.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[20][-30:], 'b', "Dias", "% de Pruebas Positivas Diarias * 100",
                            "% de Pruebas Positivas Diarias de COVID19 en el Peru: ultimos 30 dias", "perc_daily_positive_tests.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[4][-30:], 'g', "Dias", "# de Recuperados",
                    "Recuperados de COVID19 en el Peru: ultimos 30 dias", "recovered.png", data[0][len(data[0])-1])
                plot_graph(data[6][-30:], data[5][-30:], 'y', "Dias", "# de Hospitalizados",
                    "Hospitalizados por COVID19 en el Peru: ultimos 30 dias", "hospitalized.png", data[0][len(data[0])-1])
                tweets = []
                tweets.append(tweet_highlights(prev_day, curr_day, data))  #attach cases.png, gf_cases.png, active_cases.png, new_active_cases.png
                tweets.append(tweet_deaths(prev_day, curr_day, data)) #attach deaths.png, gf_deaths.png, mortality_rate.png
                tweets.append(tweet_tests_hosp_rec(prev_day, curr_day, data)) #attach tests.png perc_daily_positive_tests.png recovered.png hospitalized.png
                tweets.append(tweet_repo(tweet_date))
                export_tweets(tweets)

                if(loop == False):
                    break

                delta_time = sleep_until(tweet_date)
                print('Program will resume in ' + str(delta_time) + '(' + str(delta_time.seconds) + ' seconds)')
                time.sleep(delta_time.seconds)
            else:
                time.sleep(60)

#####################################################################################################################

run(loop=False)