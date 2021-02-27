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

def parse_file(header = True):
    dates = np.asarray([])
    cases = np.array([])
    deaths = np.array([])
    tests = np.array([])
    recovered = np.array([])
    hospitalized = np.array([])
    try:
        open(os.path.dirname(__file__) + '/../data/PER_data.csv', 'r')
    except:
        print('Could not access data file.')
        return 1
    else:
        with open(os.path.dirname(__file__) + '/../data/PER_data.csv', 'r') as file:
            for line in file:
                if(header == True):
                    header = False
                    continue
                if(line == '\n'):
                    break
                parsed_line = line.split(',')
                try: 
                    int(parsed_line[1])
                    int(parsed_line[2])
                    int(parsed_line[3])
                    int(parsed_line[4])
                    int(parsed_line[5])
                except:
                    print('Data contains invalid data. Cannot convert string to integer.')
                    return 1
                dates = np.append(dates, parsed_line[0])
                cases = np.append(cases, int(parsed_line[1]))
                deaths = np.append(deaths, int(parsed_line[2]))
                tests = np.append(tests, int(parsed_line[3]))
                recovered = np.append(recovered, int(parsed_line[4]))
                hospitalized = np.append(hospitalized, int(parsed_line[5]))
        file.close()
    return [dates, cases, deaths, tests, recovered, hospitalized]

def calc_gf(data1, data2):
    if(data2 == 0):
        return data1
    else:
        if(data1 < data2):
            return (data2 / data1) * -1
        else:
            return data1 / data2

def calc_rate(data1, data2):
    if(data2 == 0):
        return 0
    else:
        return data1 / data2

def compute_data(parsed_data):
    days = np.array([])
    new_cases = np.array([])
    cases_growth_factor = np.array([])
    new_deaths = np.array([])
    deaths_growth_factor = np.array([])
    new_tests = np.array([])
    tests_growth_factor = np.array([])
    new_recovered = np.array([])
    recovered_growth_factor = np.array([])
    new_hospitalized = np.array([])
    hospitalized_growth_factor = np.array([])
    case_fatality_rate = np.array([])
    active_cases = np.array([])
    new_active_cases = np.array([])
    daily_positives = np.array([])
    for i, entry in enumerate(parsed_data[0]):
        if(i == 0):
            new_cases = np.append(new_cases, parsed_data[1][i] - 0)
            cases_growth_factor = np.append(cases_growth_factor,  0)
            new_deaths = np.append(new_deaths, parsed_data[2][i] - 0)
            deaths_growth_factor = np.append(deaths_growth_factor, 0)
            new_tests = np.append(new_tests, parsed_data[3][i] - 0)
            tests_growth_factor = np.append(tests_growth_factor, 0)
            new_recovered = np.append(new_recovered, parsed_data[4][i] - 0)
            recovered_growth_factor = np.append(recovered_growth_factor, 0)
            new_hospitalized = np.append(new_hospitalized, parsed_data[5][i] - 0)
            hospitalized_growth_factor = np.append(hospitalized_growth_factor, 0)
            case_fatality_rate = np.append(case_fatality_rate, calc_rate(parsed_data[2][i], parsed_data[1][i]))
            active_cases = np.append(active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i]))
            new_active_cases = np.append(new_active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i] - 0))
            daily_positives = np.append(daily_positives, calc_rate(parsed_data[1][i], parsed_data[3][i]))
            days = np.append(days, i)
            continue
        new_cases = np.append(new_cases, parsed_data[1][i] - parsed_data[1][i-1])
        cases_growth_factor = np.append(cases_growth_factor, calc_gf(parsed_data[1][i], parsed_data[1][i-1]))
        new_deaths = np.append(new_deaths, parsed_data[2][i] - parsed_data[2][i-1])
        deaths_growth_factor = np.append(deaths_growth_factor, calc_gf(parsed_data[2][i], parsed_data[2][i-1]))
        new_tests = np.append(new_tests, parsed_data[3][i] - parsed_data[3][i-1])
        tests_growth_factor = np.append(tests_growth_factor, calc_gf(parsed_data[3][i], parsed_data[3][i-1]))
        new_recovered = np.append(new_recovered, parsed_data[4][i] - parsed_data[4][i-1])
        recovered_growth_factor = np.append(recovered_growth_factor, calc_gf(parsed_data[4][i], parsed_data[4][i-1]))
        new_hospitalized = np.append(new_hospitalized, parsed_data[5][i] - parsed_data[5][i-1])
        hospitalized_growth_factor = np.append(hospitalized_growth_factor, calc_gf(parsed_data[5][i], parsed_data[5][i-1]))
        case_fatality_rate = np.append(case_fatality_rate, calc_rate(parsed_data[2][i], parsed_data[1][i]))
        active_cases = np.append(active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i]))
        new_active_cases = np.append(new_active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i]) - (parsed_data[1][i-1] - parsed_data[4][i-1] - parsed_data[2][i-1]))
        daily_positives = np.append(daily_positives, calc_rate(parsed_data[1][i] - parsed_data[1][i-1], parsed_data[3][i] - parsed_data[3][i-1]))
        days = np.append(days, i)
    parsed_data.append(days)
    parsed_data.append(new_cases)
    parsed_data.append(cases_growth_factor)
    parsed_data.append(new_deaths)
    parsed_data.append(deaths_growth_factor)
    parsed_data.append(new_recovered)
    parsed_data.append(recovered_growth_factor)
    parsed_data.append(new_hospitalized)
    parsed_data.append(hospitalized_growth_factor)
    parsed_data.append(new_tests)
    parsed_data.append(tests_growth_factor)
    parsed_data.append(case_fatality_rate)
    parsed_data.append(active_cases)
    parsed_data.append(new_active_cases)
    parsed_data.append(daily_positives)
    return parsed_data

'''
Structure of diff list
Index   Contents
0       Date
1       New Cases
2       New Deaths
3       New Recovered
4       New Hospitalized
5       New Tests
6       Active Cases
7       New Active Cases
8       % Daily Positives
9       % Case Fatality
'''

def check_date(input_date):
    try:
        datetime.datetime.strptime(input_date, '%Y-%m-%d').date()
        return 0
    except:
        return 1

def update_file(data):
    path = str(pathlib.Path().absolute()).replace('\\', '/')
    path = path[:path.rfind('/')] + '/data/PER_data.csv'
    try:
        open(path, 'a')
    except:
        print('Could not access', '../data/PER_data.csv')
        return 1
    else:
        with open(path, 'a') as file:
            data_values = list(data.values())
            new_data = data_values[0] + ',' + data_values[1] + ',' + data_values[2] + ',' + \
                       data_values[3] + ',' + data_values[4] + ',' + data_values[5] + '\n'
            file.writelines(new_data)
        file.close()
        print('CSV was updated successfully.')
        return 0

def clean_dir():
    path = str(pathlib.Path().absolute()).replace('\\', '/')
    path = path[:path.rfind('/')] + '/res/raw_images/'
    files = [path + f for f in os.listdir(path)]
    for file in files:
        try:
            os.remove(file)
        except:
            return 1
    return 0

def get_raw_image_path():
    path = str(pathlib.Path().absolute()).replace('\\', '/')
    path = path[:path.rfind('/')] + '/res/raw_images/'
    out = ''
    out = path + os.fsdecode(os.listdir(path)[0])
    if(out == path):
        return 1
    else:
        return out

def get_raw_image_dimensions(path):
    image = Image.open(path)
    width, height = image.size
    return (width, height)

def crop_process_image(input_path, output_path, limits, invert=False, grescale=False, contrast=0.0):
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
    
def read_image(path):
    img_2_txt = str(pytesseract.image_to_string(Image.open(path)))
    clean_txt = ''
    for c in img_2_txt:
        if c.isdigit():
            clean_txt += c
    return clean_txt
