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
