import datetime

from ExportUtility import plot_graph
from ExportUtility import list_to_csv
from ParseData import parse_file
from ParseData import compute_data
from ParseData import diff_days

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
19      % Daily Positives
'''
raw_data = parse_file()
data = compute_data(raw_data)
diff = diff_days(data)
list_to_csv(data)

plot_graph(data[6], data[1], 'r', "Dias", "# de Casos", "Casos de COVID19 en el Peru: cumulativo", "cases.png")
plot_graph(data[6][-30:], data[8][-30:], 'r', "Dias", "Casos: Porcentaje de Crecimiento",
            "% de Crecimiento de Casos de COVID19 en el Peru: ultimos 30 dias", "gf_cases.png")
plot_graph(data[6][-30:], data[18][-30:], 'r', "Dias", "Casos Activos",
            "Casos Activos de COVID19 en el Peru: ultimos 30 dias", "active_cases.png")

plot_graph(data[6], data[2], 'k', "Dias", "# de Muertes", "Muertes por COVID19 en el Peru: cumulativo", "deaths.png")
plot_graph(data[6][-30:], data[10][-30:], 'k', "Dias", "Muertes: Porcentaje de Crecimiento",
            "% de Crecimiento de Muertes por COVID19 en el Peru: ultimos 30 dias", "gf_deaths.png")

plot_graph(data[6][-30:], data[3][-30:], 'b', "Dias", "# de Pruebas", "Pruebas de COVID19 en el Peru: ultimos 30 dias", "tests.png")
plot_graph(data[6][-30:], data[19][-30:], 'b', "Dias", "% de Casos Diarios Confirmados * 100",
            "% Casos Diarios Confirmados de COVID19 en el Peru: ultimos 30 dias", "perc_confirmed_cases.png")

plot_graph(data[6][-30:], data[4][-30:], 'g', "Dias", "# de Recuperados", "Recuperados de COVID19 en el Peru: ultimos 30 dias", "recovered.png")

plot_graph(data[6][-30:], data[5][-30:], 'y', "Dias", "# de Hospitalizados", "Hospitalizados por COVID19 en el Peru: ultimos 30 dias", "hospitalized.png")





