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

# The lower the prercentage, the better (closest to color green)
def text_indicator_lower_green(percent_change):
    if(percent_change < 0.2):
        return u'\U0001F7E2'
    if(percent_change >= 0.2 and percent_change < 0.4):
        return u'\U0001F7E1'
    if(percent_change >= 0.4 and percent_change < 0.6):
        return u'\U0001F7E0'
    elif(percent_change >= 0.6):
        return u'\U0001F534'
    else:
        return ''

# The higher the prercentage, the better (closest to color green)
def text_indicator_higher_green(percent_change):
    if(percent_change < 0.2):
        return u'\U0001F534'
    if(percent_change >= 0.2 and percent_change < 0.4):
        return u'\U0001F7E0'
    if(percent_change >= 0.4 and percent_change < 0.6):
        return u'\U0001F7E1'
    elif(percent_change >= 0.6):
        return u'\U0001F7E2'
    else:
        return ''

# The lower the prercentage, the better (closest to color green)
def text_indicator_positivity(percent_change):
    if(percent_change < 0.05):
        return u'\U0001F7E2'
    if(percent_change >= 0.05 and percent_change < 0.10):
        return u'\U0001F7E1'
    if(percent_change >= 0.10 and percent_change < 0.15):
        return u'\U0001F7E0'
    elif(percent_change >= 0.15):
        return u'\U0001F534'
    else:
        return ''

def set_plus_sign(value):
    if(value > 0):
        return '+'
    else:
        return ''


def generate_first_tweet_text(template_path, latest_entry, cases24):
    template = tpl.Text(template_path)

    gf_cases = (latest_entry['%DifCasos'] - 1.0) * 100
    template.set_placeholder_value(43, text_indicator_lower_green(gf_cases))
    template.set_placeholder_value(52, str(latest_entry['Casos']))
    template.set_placeholder_value(56, set_plus_sign(latest_entry['NuevosCasos']) + str(latest_entry['NuevosCasos']))

    template.set_placeholder_value(79, set_plus_sign(latest_entry['NuevosCasos'] - cases24) + str(latest_entry['NuevosCasos'] - cases24))
    template.set_placeholder_value(103, set_plus_sign(cases24) + str(cases24))

    gf_recovered = (latest_entry['%DifRecuperados'] - 1.0) * 100
    template.set_placeholder_value(106, text_indicator_higher_green(gf_recovered))
    template.set_placeholder_value(121, str(latest_entry['Recuperados']))
    template.set_placeholder_value(124, set_plus_sign(latest_entry['NuevosRecuperados']) + str(latest_entry['NuevosRecuperados']))

    gf_hospitalized = (latest_entry['%DifHospitalizados'] - 1.0) * 100
    template.set_placeholder_value(127, text_indicator_lower_green(gf_hospitalized))
    template.set_placeholder_value(145, str(latest_entry['Hospitalizados']))
    template.set_placeholder_value(148, set_plus_sign(latest_entry['NuevosHospitalizados']) + str(latest_entry['NuevosHospitalizados']))

    return template.process_text()

def generate_second_tweet_text(template_path, latest_entry, case_fatality_prev, positivity_rate_prev):
    template = tpl.Text(template_path)

    gf_deaths = (latest_entry['%DifFallecidos'] - 1.0) * 100
    template.set_placeholder_value(43, text_indicator_lower_green(gf_deaths))
    template.set_placeholder_value(61, str(latest_entry['Fallecidos']))
    template.set_placeholder_value(64, set_plus_sign(latest_entry['NuevosFallecidos']) + str(latest_entry['NuevosFallecidos']))

    case_fatality = (latest_entry['TasaLetalidad']) * 100
    diff_case_fatality = (latest_entry['TasaLetalidad'] - case_fatality_prev) * 100
    template.set_placeholder_value(67, text_indicator_lower_green(case_fatality))
    template.set_placeholder_value(85, str(round(case_fatality, 4)))
    template.set_placeholder_value(89, set_plus_sign(diff_case_fatality) + str(round(diff_case_fatality, 4)))

    gf_recovered = (latest_entry['%DifPruebas'] - 1.0) * 100
    template.set_placeholder_value(93, text_indicator_higher_green(gf_recovered))
    template.set_placeholder_value(115, str(latest_entry['Pruebas']))
    template.set_placeholder_value(118, set_plus_sign(latest_entry['NuevasPruebas']) + str(latest_entry['NuevasPruebas']))

    positivity_rate = (latest_entry['%PruebasPositivasDiarias']) * 100
    diff_positivity_rate = (latest_entry['%PruebasPositivasDiarias'] - positivity_rate_prev) * 100
    template.set_placeholder_value(121, text_indicator_positivity(latest_entry['%PruebasPositivasDiarias']))
    template.set_placeholder_value(143, str(round(positivity_rate, 3)))
    template.set_placeholder_value(147, set_plus_sign(diff_positivity_rate) + str(round(diff_positivity_rate, 3)))

    template.set_placeholder_value(151, str(u'\U0001F30E'))

    return template.process_text()

def export_tweets_to_file(path, tweets):
    with open(path, 'w', encoding='utf-8') as file:
        for t in tweets:
            file.write(t.message)        
            file.write('\n')

def update_git_repo_win32(date):
    os.system('sh Windows_AutoUpdateRepo.sh "' + date + '"')

def update_git_repo_linux(date):
    os.system('./Linux_AutoUpdateRepo.sh "' + date + '"')
