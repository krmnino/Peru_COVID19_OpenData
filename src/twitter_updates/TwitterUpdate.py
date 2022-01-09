import os
import sys
import cv2
import datetime
import numpy as np
import pytesseract
import pathlib
from datetime import date
from PIL import Image
from PIL import ImageOps 
from PIL import ImageEnhance
from math import sqrt

sys.path.insert(0, '../utilities')

import TextPlaceholders as tpl
from TwitterUtility import Tweet

if(sys.platform == 'win32'):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#Do not print in scientific notiation
np.set_printoptions(suppress=True)

def check_date(input_date):
    try:
        datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
    except:
        sys.exit('Invalid input date. Exiting...')

def get_top_level_directory_path():
    path = str(pathlib.Path().absolute()).replace('\\', '/')
    path = path[:path.rfind('/')]
    path = path[:path.rfind('/')]
    return path

def clean_dir(ext_path):
    path = get_top_level_directory_path() + ext_path
    files = [path + '/' + f for f in os.listdir(path)]
    for file in files:
        try:
            os.remove(file)
        except:
            sys.exit('Could not clean raw_images directory. Exiting...')

def get_bulletin_image_path(path):
    out = path + '/' + os.fsdecode(os.listdir(path)[0])
    if(out == path):
        sys.exit('Could not retrieve bulletin image path. Exiting...')
    else:
        return out

def get_bulletin_dimensions(path):
    image = Image.open(path)
    width, height = image.size
    return (width, height)

def process_image(input_path, output_path, limits, invert=False, grescale=False, contrast=0.0):
    image = Image.open(input_path)
    #left, up, right, down
    image = image.crop((limits[0], limits[1], limits[2], limits[3])) 
    image = image.convert('RGB')
    if(invert):
        image = ImageOps.invert(image)
    if(grescale):
        image = ImageOps.grayscale(image)
    if(contrast != 0.0):
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
    image.save(output_path)
    upper_black = np.array([255,255,255], dtype = "uint16")
    lower_black = np.array([80,80,80], dtype = "uint16")
    image = cv2.imread(output_path)
    black_mask = cv2.inRange(image, lower_black, upper_black)
    cv2.imwrite(output_path, black_mask)
    
def decode_image(path):
    img_2_txt = str(pytesseract.image_to_string(Image.open(path)))
    clean_txt = ''
    for c in img_2_txt:
        if c.isdigit():
            clean_txt += c
    return clean_txt

def compute_new_cases(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_cases() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_cases_growth_factor(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_cases_growth_factor() is not 1')
    if(index == 0):
        return 0.0
    else:
        if(columns[0][index-1] == 0.0):
            return columns[0][index]
        if(columns[0][index] < columns[0][index-1]):
            return (columns[0][index-1] / columns[0][index]) * -1
        else:
            return columns[0][index] / columns[0][index-1]

def compute_active_cases(index, columns):
    if(len(columns) != 3):
        sys.exit('Number of values passed in compute_cases_growth_factor() is not 3')
    return columns[0][index] - columns[1][index] - columns[2][index]

def compute_new_active_cases(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_active_cases() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_new_deaths(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_deaths() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_deaths_growth_factor(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_deaths_growth_factor() is not 1')
    if(index == 0):
        return 0.0
    else:
        if(columns[0][index-1] == 0.0):
            return columns[0][index]
        if(columns[0][index] < columns[0][index-1]):
            return (columns[0][index-1] / columns[0][index]) * -1
        else:
            return columns[0][index] / columns[0][index-1]

def compute_case_fatality_rate(index, columns):
    if(len(columns) != 2):
        sys.exit('Number of values passed in compute_case_fatality_rate() is not 2')
    if(columns[0][index] == 0):
        return 0.0
    else:
        return columns[1][index] / columns[0][index]

def compute_new_tests(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_tests() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_tests_growth_factor(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_tests_growth_factor() is not 1')
    if(index == 0):
        return 0.0
    else:
        if(columns[0][index-1] == 0.0):
            return columns[0][index]
        if(columns[0][index] < columns[0][index-1]):
            return (columns[0][index-1] / columns[0][index]) * -1
        else:
            return columns[0][index] / columns[0][index-1]

def compute_daily_positivity_rate(index, columns):
    if(len(columns) != 2):
        sys.exit('Number of values passed in compute_daily_positivity_rate() is not 2')
    if(columns[0][index] == 0):
        return 0.0
    else:
        return columns[1][index] / columns[0][index]

def compute_new_recovered(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_recovered() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_recovered_growth_factor(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_recovered_growth_factor() is not 1')
    if(index == 0):
        return 0.0
    else:
        if(columns[0][index-1] == 0.0):
            return columns[0][index]
        if(columns[0][index] < columns[0][index-1]):
            return (columns[0][index-1] / columns[0][index]) * -1
        else:
            return columns[0][index] / columns[0][index-1]

def compute_new_hospitalized(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_new_hospitalized() is not 1')
    if(index == 0):
        return columns[0][index] - 0.0
    else:
        return columns[0][index] - columns[0][index-1]

def compute_hospitalized_growth_factor(index, columns):
    if(len(columns) != 1):
        sys.exit('Number of values passed in compute_hospitalized_growth_factor() is not 1')
    if(index == 0):
        return 0.0
    else:
        if(columns[0][index-1] == 0.0):
            return columns[0][index]
        if(columns[0][index] < columns[0][index-1]):
            return (columns[0][index-1] / columns[0][index]) * -1
        else:
            return columns[0][index] / columns[0][index-1]

def compute_days(index, columns):
    return index

def set_plus_sign(value):
    if(value > 0):
        return '+'
    else:
        return ''

def generate_first_tweet_text(template_path, latest_entry, cases24, new_cases_ind, new_recovered_ind, new_hospitalized_ind):
    template = tpl.Text(template_path)

    template.set_ph_value_by_position(0, new_cases_ind)
    template.set_ph_value_by_position(1, str(latest_entry['Casos']))
    template.set_ph_value_by_position(2, set_plus_sign(latest_entry['NuevosCasos']) + str(int(latest_entry['NuevosCasos'])))

    template.set_ph_value_by_position(3, set_plus_sign(latest_entry['NuevosCasos'] - cases24) + str(int(latest_entry['NuevosCasos'] - cases24)))
    template.set_ph_value_by_position(4, set_plus_sign(cases24) + str(int(cases24)))

    template.set_ph_value_by_position(5, new_recovered_ind)
    template.set_ph_value_by_position(6, str(latest_entry['Recuperados']))
    template.set_ph_value_by_position(7, set_plus_sign(latest_entry['NuevosRecuperados']) + str(int(latest_entry['NuevosRecuperados'])))

    template.set_ph_value_by_position(8, new_hospitalized_ind)
    template.set_ph_value_by_position(9, str(latest_entry['Hospitalizados']))
    template.set_ph_value_by_position(10, set_plus_sign(latest_entry['NuevosHospitalizados']) + str(int(latest_entry['NuevosHospitalizados'])))

    return template.process_text()

def generate_second_tweet_text(template_path, latest_entry, case_fatality_prev, positivity_rate_prev,
                               new_deaths_ind, new_case_fatality_ind, new_tests_ind, new_positivity_ind):
    template = tpl.Text(template_path)

    template.set_ph_value_by_position(0, new_deaths_ind)
    template.set_ph_value_by_position(1, str(latest_entry['Fallecidos']))
    template.set_ph_value_by_position(2, set_plus_sign(latest_entry['NuevosFallecidos']) + str(int(latest_entry['NuevosFallecidos'])))

    case_fatality = (latest_entry['TasaLetalidad']) * 100
    diff_case_fatality = (latest_entry['TasaLetalidad'] - case_fatality_prev) * 100
    template.set_ph_value_by_position(3, new_case_fatality_ind)
    template.set_ph_value_by_position(4, str(round(case_fatality, 4)))
    template.set_ph_value_by_position(5, set_plus_sign(diff_case_fatality) + str(round(diff_case_fatality, 4)))

    template.set_ph_value_by_position(6, new_tests_ind)
    template.set_ph_value_by_position(7, str(latest_entry['Pruebas']))
    template.set_ph_value_by_position(8, set_plus_sign(latest_entry['NuevasPruebas']) + str(int(latest_entry['NuevasPruebas'])))

    positivity_rate = (latest_entry['%PruebasPositivasDiarias']) * 100
    diff_positivity_rate = (latest_entry['%PruebasPositivasDiarias'] - positivity_rate_prev) * 100
    template.set_ph_value_by_position(9, new_positivity_ind)
    template.set_ph_value_by_position(10, str(round(positivity_rate, 3)))
    template.set_ph_value_by_position(11, set_plus_sign(diff_positivity_rate) + str(round(diff_positivity_rate, 3)))

    template.set_ph_value_by_position(12, str(u'\U0001F30E'))

    return template.process_text()

def export_tweets_to_file(path, tweets):
    with open(path, 'w', encoding='utf-8') as file:
        for t in tweets:
            file.write(t.message)        
            file.write('\n')
