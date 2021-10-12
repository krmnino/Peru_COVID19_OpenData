import datetime
import os
import sys
import time
import copy

sys.path.insert(0, '../utilities')

import DataUtility as du
import ConfigUtility as cu
import PlottingUtility as pu

from TwitterUpdate import get_bulletin_image_path
from TwitterUpdate import process_image
from TwitterUpdate import decode_image
from TwitterUpdate import get_top_level_directory_path
from TwitterUpdate import check_date
from TwitterUpdate import get_bulletin_dimensions
from TwitterUpdate import clean_dir
from TwitterUpdate import compute_new_cases
from TwitterUpdate import compute_cases_growth_factor
from TwitterUpdate import compute_active_cases
from TwitterUpdate import compute_new_active_cases
from TwitterUpdate import compute_new_deaths
from TwitterUpdate import compute_deaths_growth_factor
from TwitterUpdate import compute_case_fatality_rate
from TwitterUpdate import compute_new_tests
from TwitterUpdate import compute_tests_growth_factor
from TwitterUpdate import compute_daily_positivity_rate
from TwitterUpdate import compute_new_recovered
from TwitterUpdate import compute_recovered_growth_factor
from TwitterUpdate import compute_new_hospitalized
from TwitterUpdate import compute_hospitalized_growth_factor
from TwitterUpdate import compute_days
from TwitterUpdate import generate_first_tweet_text
from TwitterUpdate import generate_second_tweet_text
from TwitterUpdate import export_tweets_to_file
from TwitterUpdate import update_git_repo_win32
from TwitterUpdate import update_git_repo_linux
from CommandLineUtility import check_data_menu
from CommandLineUtility import check_tweets_menu
from TwitterUtility import TwitterAPISession
from TwitterUtility import Tweet

def run():
    # Obtain current date
    current_date = datetime.date.today().strftime('%Y-%m-%d')

    # Get top level directory
    top_level_directory = get_top_level_directory_path()
    
    # Load configuration files for program and Twitter authentication
    main_config = cu.Config(top_level_directory + '/src/twitter_updates/TwitterUpdateConfig.cl')
    auth_config = cu.Config(top_level_directory + main_config.get_value('TwitterAuth'))
    
    # Remove any old files from /res/raw_images
    clean_dir(main_config.get_value('RawImages'))
    
    # Authenticate Twitter API session
    twitter_session = TwitterAPISession(auth_config)

    # Query ID of the tweet to reply to
    query_tweets = twitter_session.query_n_tweets(
        main_config.get_value('TwitterMINSA'),
        int(main_config.get_value('QueryTweets'))
    )

    # Retrieve a batch of n tweets from MINSA
    ret_tweet = check_tweets_menu(query_tweets)

    # Query images from previously queried tweet
    twitter_session.fetch_image_by_id(
        top_level_directory + main_config.get_value('RawImages'),
        ret_tweet
    )

    # Retrieve bulletin image path
    bulletin_path = get_bulletin_image_path(top_level_directory + main_config.get_value('RawImages'))

    #Get bulletin image dimensions
    image_dimensions = get_bulletin_dimensions(bulletin_path)

    # Crop bulletin into sectors and apply post-processing techniques to improve readability with OCR
    if(image_dimensions[0] < 900 or image_dimensions[1] < 1100):
        #left, up, right, down
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawCases'), (420, 365, 600, 420), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawDeaths'), (420, 560, 560, 620), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawTests'), (100, 600, 300, 660), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawRecov'), (90, 360, 325, 445), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawHospit'), (440, 485, 570, 570), grescale=True, invert=True, contrast=1.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawCases24'), (100, 110, 290, 200), grescale=True, invert=True, contrast=2.0)
    else:
        #left, up, right, down
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawCases'), (660, 590, 960, 670), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawDeaths'), (650, 900, 950, 990), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawTests'), (170, 930, 480, 1020), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawRecov'), (170, 560, 520, 700), grescale=True, invert=False, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawHospit'), (670, 780, 950, 870), grescale=True, invert=True, contrast=2.0)
        process_image(bulletin_path, top_level_directory + main_config.get_value('RawCases24'), (150, 160, 530, 310), grescale=True, invert=True, contrast=2.0)
    
    # Store values read by OCR algorithm in a dictionary
    input_data = {\
        'Date' : current_date,
        'Cases' : decode_image(top_level_directory + main_config.get_value('RawCases')),
        'Deaths' : decode_image(top_level_directory + main_config.get_value('RawDeaths')),
        'Tests' : decode_image(top_level_directory + main_config.get_value('RawTests')),
        'Recovered' : decode_image(top_level_directory + main_config.get_value('RawRecov')),
        'Hospitalized' : decode_image(top_level_directory + main_config.get_value('RawHospit')),
        'Cases24H' : decode_image(top_level_directory + main_config.get_value('RawCases24'))
    }

    # Remove any old files from /res/raw_images
    clean_dir(main_config.get_value('RawImages'))

    # Open temporary command line to check if data is correct
    check_data_menu(input_data) 
    
    # Load simple Peru data set
    PER_data = du.Table('l', filename=top_level_directory + main_config.get_value('PeruSimpleData'), delimiter = ',')

    # Agregate new data entry
    PER_data.append_end_row([   
        input_data['Date'],
        int(input_data['Cases']),
        int(input_data['Deaths']),
        int(input_data['Tests']),
        int(input_data['Recovered']),
        int(input_data['Hospitalized'])
    ])
    
    # Save simple Peru data set
    PER_data.save_as_csv(top_level_directory + main_config.get_value('PeruSimpleData'))

    # Create copy of simple Peru data set to perform extrapolation 
    PER_full_data = du.Table('c', table=PER_data)

    # Compute new derived statistics
    PER_full_data.compute_new_column('NuevosCasos', ['Casos'], compute_new_cases)
    PER_full_data.compute_new_column('%DifCasos', ['Casos'], compute_cases_growth_factor)
    PER_full_data.compute_new_column('CasosActivos', ['Casos', 'Recuperados', 'Fallecidos'], compute_active_cases)
    PER_full_data.compute_new_column('NuevosCasosActivos', ['CasosActivos'], compute_new_active_cases)
    PER_full_data.compute_new_column('NuevosFallecidos', ['Fallecidos'], compute_new_deaths)
    PER_full_data.compute_new_column('%DifFallecidos', ['Fallecidos'], compute_deaths_growth_factor)
    PER_full_data.compute_new_column('TasaLetalidad', ['Casos', 'Fallecidos'], compute_case_fatality_rate)
    PER_full_data.compute_new_column('NuevasPruebas', ['Pruebas'], compute_new_tests)
    PER_full_data.compute_new_column('%DifPruebas', ['Pruebas'], compute_tests_growth_factor)
    PER_full_data.compute_new_column('%PruebasPositivasDiarias', ['NuevasPruebas', 'NuevosCasos'], compute_daily_positivity_rate)
    PER_full_data.compute_new_column('NuevosRecuperados', ['Recuperados'], compute_new_recovered)
    PER_full_data.compute_new_column('%DifRecuperados', ['Recuperados'], compute_tests_growth_factor)
    PER_full_data.compute_new_column('NuevosHospitalizados', ['Hospitalizados'], compute_new_hospitalized)
    PER_full_data.compute_new_column('%DifHospitalizados', ['Hospitalizados'], compute_hospitalized_growth_factor)
    PER_full_data.compute_new_column('Dia', [], compute_days)

    # Reorganize header index before saving
    new_header = [
        'Fecha',
        'Dia',
        'Casos',
        'NuevosCasos',
        '%DifCasos',
        'CasosActivos',
        'NuevosCasosActivos',
        'Fallecidos',
        'NuevosFallecidos',
        '%DifFallecidos',
        'TasaLetalidad',
        'Pruebas',
        'NuevasPruebas',
        '%DifPruebas',
        '%PruebasPositivasDiarias',
        'Recuperados',
        'NuevosRecuperados',
        '%DifRecuperados',
        'Hospitalizados',
        'NuevosHospitalizados',
        '%DifHospitalizados'
    ]

    # Rearrange header index in Peru full data
    PER_full_data.rearrange_header_index(new_header)

    # Save full Peru data set
    PER_full_data.save_as_csv(top_level_directory + main_config.get_value('PeruFullData'))

    # Create quadplot object for first tweet
    quadplot_1 = pu.QuadPlot(
        [main_config.get_value('CasesColor'), main_config.get_value('CasesColor'), main_config.get_value('RecoveredColor'), main_config.get_value('HospitalizedColor')],
        ['Casos Confirmados (ultimos 30 dias)', 'Nuevos Casos Confirmados (ultimos 30 dias)', 'Nuevos Recuperados (ultimos 30 dias)', 'Hospitalizados (ultimos 30 dias)'],
        [False, True, True, True],
        ['bar', 'bar', 'bar', 'bar'],
        ['Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)'],
        ['Casos Confirmados (acumulado por dia)', 'Nuevos Casos Confirmados (por dia)', 'Nuevos Recuperados (por dia)', 'Hospitalizados (por dia)'],
        [PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:]],
        [PER_full_data.get_column_data('Casos')[-30:], PER_full_data.get_column_data('NuevosCasos')[-30:], PER_full_data.get_column_data('NuevosRecuperados')[-30:], PER_full_data.get_column_data('Hospitalizados')[-30:]],
        current_date + ' | Elaborado por Kurt Manrique-Nino | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
        top_level_directory + main_config.get_value('TwitterGraph1'),
        ravg_days=[7, 7, 7, 7],
        ravg_labels=['Promedio ultimos 7 dias', 'Promedio ultimos 7 dias', 'Promedio ultimos 7 dias', 'Promedio ultimos 7 dias'],
        ravg_ydata=[None, PER_full_data.get_column_data('NuevosCasos'), PER_full_data.get_column_data('NuevosRecuperados'), PER_full_data.get_column_data('Hospitalizados')]
    )

    # Create quadplot object for second tweet
    quadplot_2 = pu.QuadPlot(
        [main_config.get_value('DeathsColor'), main_config.get_value('DeathsColor'), main_config.get_value('TestsColor'), main_config.get_value('TestsColor')],
        ['Nuevos Fallecidos (ultimos 30 dias)', 'Tasa de Letalidad (ultimos 30 dias)', 'Nuevas Pruebas (PM+PR+AG) (ultimos 30 dias)', 'Positividad Diaria (PM+PR+AG) (ultimos 30 dias)'],
        [True, True, True, True],
        ['bar', 'scatter', 'bar', 'scatter'],
        ['Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)','Fecha (YYYY-MM-DD)'],
        ['Nuevos Fallecidos (por dia)', 'Tasa de Letalidad (acumulado por dia)', 'Nuevas Pruebas (por dia)', 'Positividad Diaria * 100% (PM+PR+AG)'],
        [PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:], PER_full_data.get_column_data('Fecha')[-30:]],
        [PER_full_data.get_column_data('NuevosFallecidos')[-30:], PER_full_data.get_column_data('TasaLetalidad')[-30:], PER_full_data.get_column_data('NuevasPruebas')[-30:], PER_full_data.get_column_data('%PruebasPositivasDiarias')[-30:]],
        current_date + ' | Elaborado por Kurt Manrique-Nino | Datos del Ministerio de Salud del Peru (@Minsa_Peru)',
        top_level_directory + main_config.get_value('TwitterGraph2'),
        ravg_days=[7, 7, 7, 7],
        ravg_labels=['Promedio ultimos 7 dias', 'Promedio ultimos 7 dias', 'Promedio ultimos 7 dias', 'Promedio ultimos 7 dias'],
        ravg_ydata=[PER_full_data.get_column_data('NuevosFallecidos'), PER_full_data.get_column_data('TasaLetalidad'), PER_full_data.get_column_data('NuevasPruebas'), PER_full_data.get_column_data('%PruebasPositivasDiarias')]
    )

    # Generate and store quadplot
    quadplot_1.export()   

    # Generate and store quadplot
    quadplot_2.export()

    # Obtain the last entry of Peru full data
    latest_entry = PER_full_data.get_end_row()
    
    # Create instances of tweets to store text and image paths
    tweet1 = Tweet()
    tweet2 = Tweet()
    
    # Create and add tweet body for first tweet
    tweet1.set_message(generate_first_tweet_text(top_level_directory + main_config.get_value('TwTemplate1'), latest_entry, int(input_data['Cases24H'])))
    
    # Create and add tweet body for second tweet
    tweet2.set_message(generate_second_tweet_text(top_level_directory + main_config.get_value('TwTemplate2'), latest_entry,
         PER_full_data.get_cell_data('TasaLetalidad', PER_full_data.rows-2), PER_full_data.get_cell_data('%PruebasPositivasDiarias', PER_full_data.rows-2)))

    # Add paths to graph images
    tweet1.add_image(top_level_directory + main_config.get_value('TwitterGraph1'))
    tweet2.add_image(top_level_directory + main_config.get_value('TwitterGraph2'))

    # Export tweet messages into a file
    export_tweets_to_file(top_level_directory + main_config.get_value('TweetExport'), [tweet1, tweet2])
    
    # Reply to @Minsa_Peru with tweet thread
    #twitter_session.reply_thread(ret_tweet.tweet_id, [tweet1, tweet2])

    # Update GitHub repository with new data    
    #if(sys.platform == 'win32'):
    #    update_git_repo_win32(input_data['Date'])
    #else:
    #    update_git_repo_linux(input_data['Date'])

#####################################################################################################################

run()
