import matplotlib.pyplot as plt
import warnings
from datetime import date

def plot_graph(x, y, color, x_label, y_label, chart_title, file_name):
    warnings.filterwarnings('ignore')
    plt.figure(figsize=(14,10))
    plt.ticklabel_format(style='plain')
    plt.plot(x, y, 'ko', x, y, color)
    plt.title(chart_title, fontdict={'fontsize' : 20})
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.savefig('../export/' + file_name)
    print('Graph generated in export/' + file_name)


def list_to_csv(parsed_data):
    file_name = 'data_' + date.today().strftime('%Y-%m-%d') + '.csv'
    try:
        open('../export/' + file_name, 'w')
    except:
        print('Could not export processed data.')
        return 
    out_file = open('../export/' + file_name, 'w')
    out_file.write('Fecha,Dia,Casos,NuevosCasos,%DifCases,CasosActivos,Muertes,NuevasMuertes,%DifDeaths,TasaMortandad,Pruebas,NuevasPruebas,\
            %DifTests,%CasosConfirmadosDiarios,Recuperados,NuevosRecuperados,%DifRecuperados,Hospitalizados,NuevosHospitalizados,%DiffHospitalized\n')
    for i in range(0, len(parsed_data[0])-1):
        line = str(parsed_data[0][i]) + "," + str(parsed_data[6][i]) + "," + \
            str(parsed_data[1][i]) + "," + str(parsed_data[7][i]) + "," + str(parsed_data[8][i]) + "," + str(parsed_data[18][i]) + "," + \
            str(parsed_data[2][i]) + "," + str(parsed_data[9][i]) + "," + str(parsed_data[10][i]) + "," + str(parsed_data[17][i]) + "," + \
            str(parsed_data[3][i]) + "," + str(parsed_data[15][i]) + "," + str(parsed_data[16][i]) + "," + str(parsed_data[19][i]) + "," + \
            str(parsed_data[4][i]) + "," + str(parsed_data[11][i]) + "," + str(parsed_data[12][i]) + "," + \
            str(parsed_data[5][i]) + "," + str(parsed_data[13][i]) + "," + str(parsed_data[14][i]) + "\n" 
        out_file.write(line)
    out_file.close()
    print('Data successfully exported to export/' + file_name)