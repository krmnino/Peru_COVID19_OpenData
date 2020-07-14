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
19      Daily Positives
'''
raw_data = parse_file()
data = compute_data(raw_data)
diff = diff_days(data)
plot_graph(data[6], data[1], 'r', "Dias", "# de Casos", "Casos de COVID19 en el Peru: cumulativo", "cases.png")
plot_graph(data[6], data[2], 'k', "Dias", "# de Muertes", "Muertes por COVID19 en el Peru: cumulativo", "deaths.png")
plot_graph(data[6], data[3], 'b', "Dias", "# de Pruebas", "Pruebas de COVID19 en el Peru: cumulativo", "tests.png")
plot_graph(data[6], data[4], 'g', "Dias", "# de Recuperados", "Recuperados de COVID19 en el Peru: cumulativo", "recovered.png")
plot_graph(data[6], data[5], 'y', "Dias", "# de Hospitalizados", "Hospitalizados por COVID19 en el Peru: cumulativo", "hospitalized.png")
list_to_csv(data)





