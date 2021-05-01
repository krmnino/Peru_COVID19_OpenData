import PlottingUtility as pu
import DataUtility as du
import copy
import sys

data = du.Table('../../data/PER_data.csv')
compute_data = copy.deepcopy(data)


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

plot = pu.Plot(4,
            ['#E04646', '#9CD347', '#D8D13B', '#8C8C8C'],
            ['casos', 'recuperados', 'hospitalizados', 'fallecidos'],
            [False, False, False, False],
            ['bar', 'bar', 'bar', 'bar'],
            ['fecha','fecha','fecha','fecha'],
            ['nuevos casos', 'nuevos recuperados', 'nuevos hospitalizados', 'nuevos fallecidos'],
            [data.get_column('Fecha'), data.get_column('Fecha'), data.get_column('Fecha'), data.get_column('Fecha')],
            [data.get_column('Casos'), data.get_column('Recuperados'), data.get_column('Hospitalizados'), data.get_column('Fallecidos')])



#print(data.get_latest_entry())

print(compute_data.get_fields())
compute_data.compute_add_column(['Casos'], compute_new_cases, 'NuevosCasos')
compute_data.compute_add_column(['Casos'], compute_cases_growth_factor, '%DifCasos')
compute_data.compute_add_column(['Casos', 'Recuperados', 'Fallecidos'], compute_active_cases, 'CasosActivos')
print(compute_data.get_column('%DifCasos'))
