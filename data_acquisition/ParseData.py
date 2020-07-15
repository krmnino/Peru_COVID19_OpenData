import os
import datetime
import numpy as np
from datetime import date
from PIL import Image
from PIL import ImageOps 
from PIL import ImageEnhance
import pytesseract


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
        open(os.path.dirname(__file__) + '/../PER_data.csv', 'r')
    except:
        print('Could not access data file.')
        return 1
    else:
        with open(os.path.dirname(__file__) + '/../PER_data.csv', 'r') as file:
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
    mortality_rate = np.array([])
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
            mortality_rate = np.append(mortality_rate, calc_rate(parsed_data[2][i], parsed_data[1][i]))
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
        mortality_rate = np.append(mortality_rate, calc_rate(parsed_data[2][i], parsed_data[1][i]))
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
    parsed_data.append(mortality_rate)
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
9       % Mortality
'''

def diff_prev_day(data):
    return [data[0][len(data[0])-2], data[7][len(data[0])-2], data[9][len(data[0])-2], data[11][len(data[0])-2], data[13][len(data[0])-2],
            data[15][len(data[0])-2], data[18][len(data[0])-2], data[19][len(data[0])-2], data[20][len(data[0])-2], data[17][len(data[0])-2]]

def diff_curr_day(data):
    return [data[0][len(data[0])-1], data[7][len(data[0])-1], data[9][len(data[0])-1], data[11][len(data[0])-1], data[13][len(data[0])-1],
            data[15][len(data[0])-1], data[18][len(data[0])-1], data[19][len(data[0])-1], data[20][len(data[0])-1], data[17][len(data[0])-1]]

def update_file(date, cases, deaths, tests, recovered, hospitalized):
    try:
        open('../PER_data.csv', 'a')
    except:
        print('Could not access', '../PER_data.csv')
        return False
    else:
        with open('../PER_data.csv', 'a') as file:
            new_data = date + ',' + cases + ',' + deaths + ',' + tests + ',' + recovered + ',' + hospitalized + '\n'
            file.writelines(new_data)
        file.close()
        return True

def get_raw_image_path():
    for file in os.listdir('raw_images'):
        filename = os.fsdecode(file)
        return 'raw_images/' + filename

def crop_image(input_path, output_path, limits, invert=False, grescale=False, contrast=0.0):
    image = Image.open(input_path)
    #left, up, right, down
    image = image.crop((limits[0], limits[1], limits[2], limits[3])) 
    if(invert):
        image = ImageOps.invert(image)
    if(grescale):
        image = ImageOps.grayscale(image)
    if(contrast != 0.0):
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
    image.save(output_path)
    
def read_image(path):
    img_2_txt = str(pytesseract.image_to_string(Image.open(path)))
    os.remove(path)
    return img_2_txt
