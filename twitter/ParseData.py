import os
import datetime
import numpy as np

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
        open(os.path.dirname(__file__) + '../PER_data.csv', 'r')
    except:
        print('Could not access data file.')
        return 1
    else:
        with open(os.path.dirname(__file__) + '../PER_data.csv', 'r') as file:
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

def calc_rate(data1, data2):
    if(data2 == 0):
        return data1
    else:
        if(data1 < data2):
            return (data2 / data1) * -1
        else:
            return data1 / data2

def calc_mort_rate(data1, data2):
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
            mortality_rate = np.append(mortality_rate, calc_mort_rate(parsed_data[2][i], parsed_data[1][i]))
            active_cases = np.append(active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i]))
            days = np.append(days, i)
            continue
        new_cases = np.append(new_cases, parsed_data[1][i] - parsed_data[1][i-1])
        cases_growth_factor = np.append(cases_growth_factor, calc_rate(parsed_data[1][i], parsed_data[1][i-1]))
        new_deaths = np.append(new_deaths, parsed_data[2][i] - parsed_data[2][i-1])
        deaths_growth_factor = np.append(deaths_growth_factor, calc_rate(parsed_data[2][i], parsed_data[2][i-1]))
        new_tests = np.append(new_tests, parsed_data[3][i] - parsed_data[3][i-1])
        tests_growth_factor = np.append(tests_growth_factor, calc_rate(parsed_data[3][i], parsed_data[3][i-1]))
        new_recovered = np.append(new_recovered, parsed_data[4][i] - parsed_data[4][i-1])
        recovered_growth_factor = np.append(recovered_growth_factor, calc_rate(parsed_data[4][i], parsed_data[4][i-1]))
        new_hospitalized = np.append(new_hospitalized, parsed_data[5][i] - parsed_data[5][i-1])
        hospitalized_growth_factor = np.append(hospitalized_growth_factor, calc_rate(parsed_data[5][i], parsed_data[5][i-1]))
        mortality_rate = np.append(mortality_rate, calc_mort_rate(parsed_data[2][i], parsed_data[1][i]))
        active_cases = np.append(active_cases, (parsed_data[1][i] - parsed_data[4][i] - parsed_data[2][i]))
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
    return parsed_data

def previous_current_days(data, header = False):
    previous_day = [data[0][len(data[0])-2], data[1][len(data[0])-2], data[2][len(data[0])-2], data[3][len(data[0])-2],
                    data[4][len(data[0])-2], data[5][len(data[0])-2], data[18][len(data[0])-2]]
    current_day = [data[0][len(data[0])-1], data[1][len(data[0])-1], data[2][len(data[0])-1], data[3][len(data[0])-1],
                    data[4][len(data[0])-1], data[5][len(data[0])-1], data[18][len(data[0])-1]]
    return [previous_day, current_day]


def diff_data(days):
    diff_cases = days[1][1] - days[0][1]
    diff_deaths = days[1][2] - days[0][2]
    diff_tests = days[1][3] - days[0][3]
    diff_recovered = days[1][4] - days[0][4]
    diff_hospitalized = days[1][5] - days[0][5]
    diff_active = days[1][6] - days[0][6]
    data_difference = [diff_cases, diff_deaths, diff_tests, diff_recovered, diff_hospitalized, diff_active]
    return data_difference       

def mortality_rate(days):
    return float(days[1][2] / days[1][1])

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
'''
raw_data = parse_file()
data = compute_data(raw_data)
days = previous_current_days(data)
diff = diff_data(days)
print(diff)
#mort_rate = mortality_rate(days)
#print(mort_rate)
