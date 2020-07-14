import os
import datetime

def previous_current_day(header = False):
    try:
        open(os.path.dirname(__file__) + '../PER_data.csv', 'r')
    except:
        print('Could not access data file.')
        return 1
    else:
        previous_day = []
        current_day = []
        with open(os.path.dirname(__file__) + '../PER_data.csv', 'r') as file:
            
            for line in file:
                if(header == False):
                    header = True
                    continue
                else:
                    previous_day = current_day
                    current_day = line.split(',')
    previous_day[0] = datetime.datetime.strptime(previous_day[0], '%Y-%m-%d')
    previous_day[1] = int(previous_day[1]) #cases
    previous_day[2] = int(previous_day[2]) #deaths
    previous_day[3] = int(previous_day[3]) #tests
    previous_day[4] = int(previous_day[4]) #recovered
    previous_day[5] = int(previous_day[5][:-1]) #hospitalized
    current_day[0] = datetime.datetime.strptime(current_day[0], '%Y-%m-%d')
    current_day[1] = int(current_day[1]) #cases
    current_day[2] = int(current_day[2]) #deaths
    current_day[3] = int(current_day[3]) #tests
    current_day[4] = int(current_day[4]) #recovered
    current_day[5] = int(current_day[5][:-1]) #hospitalized
    return [previous_day, current_day]


def diff_data(days):
    diff_cases = days[1][1] - days[0][1]
    diff_deaths = days[1][2] - days[0][2]
    diff_tests = days[1][3] - days[0][3]
    diff_recovered = days[1][4] - days[0][4]
    data_difference = [diff_cases, diff_deaths, diff_tests, diff_recovered]
    return data_difference       

def current_active(days):
    return days[0][1] - days[0][2] - days[0][4]



days = previous_current_day()
diff = diff_data(days)
active = current_active(days)
print(active)

    