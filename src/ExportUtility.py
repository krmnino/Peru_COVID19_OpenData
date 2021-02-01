import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import warnings
import os 
from TwitterUtility import Tweet


class GraphData:
    graph_type = '' #scatter / bar
    x_data = None
    y_data = []
    x_label = ''
    last_days = 0
    y_data_labels = []
    colors = []
    title = ''
    title_size = 0
    suptitle = ''
    filename = ''
    date = ''
    tick_markers = False
    legend = False
    y_max = -1
    y_min = -1

    def __init__(self, graph_type_, x_data_, y_data_, last_days_, x_label_, y_data_labels_, colors_, title_,
                title_size_, suptitle_, filename_, date_, tick_markers_, legend_, y_max_, y_min_):
        self.graph_type = graph_type_
        self.x_data = x_data_
        self.y_data = y_data_
        self.last_days = last_days_
        self.x_label = x_label_
        self.y_data_labels = y_data_labels_
        self.colors = colors_
        self.title = title_
        self.title_size = title_size_
        self.suptitle = suptitle_
        self.filename = filename_
        self.date = date_
        self.tick_markers = tick_markers_
        self.legend = legend_
        self.y_max = y_max_
        self.y_min = y_min_

def plot_loader(graph_data):
    warnings.filterwarnings('ignore')
    for graph in graph_data:
        plt.figure(figsize=(14,10))
        plt.ticklabel_format(style='plain')
        plt.suptitle(graph.suptitle)
        plt.title(graph.title, fontdict={'fontsize' : graph.title_size})
        if(graph.graph_type == 'scatter'):
            for i in range(0, len(graph.y_data)):
                plt.plot(graph.x_data[-graph.last_days:], graph.y_data[i][-graph.last_days:], graph.colors[i], label=graph.y_data_labels[i])
                if(graph.tick_markers):
                    plt.plot(graph.x_data[-graph.last_days:], graph.y_data[i][-graph.last_days:], 'ko')
            plt.xlabel(graph.x_label)
            plt.ylabel(''.join(i + str(' ,') for i in graph.y_data_labels)[:-2])
            if(graph.last_days == 30):
                plt.xticks(graph.x_data[-graph.last_days:][::2], rotation=90)
                plt.locator_params(axis='x', nbins=len(graph.x_data[-graph.last_days:])/2)
            else:
                plt.xticks(graph.x_data[::5], rotation=90)
                plt.locator_params(axis='x', nbins=len(graph.x_data[-graph.last_days:])/10)
            if(graph.y_min != -1):
                plt.ylim(bottom=graph.y_min)
            if(graph.y_max != -1):
                plt.ylim(top=graph.y_max)
            if(graph.legend):
                plt.legend(loc='upper left')
            plt.grid()
        elif(graph.graph_type == 'bar'):
            plt.grid(zorder=0)
            plt.bar(graph.x_data[-graph.last_days:], graph.y_data[0][-graph.last_days:], color=graph.colors[0], zorder=2)
            plt.plot(graph.x_data[-graph.last_days:], graph.y_data[0][-graph.last_days:], linestyle='dashed', color='b')
            if(graph.last_days == 30):
                plt.xticks(graph.x_data[-graph.last_days:], rotation=90)
                plt.locator_params(axis='x', nbins=len(graph.x_data[-graph.last_days:]))
            else:
                plt.xticks(graph.x_data[::5], rotation=90)
                plt.locator_params(axis='x', nbins=len(graph.x_data[-graph.last_days:])/10)
            
        plt.savefig('../res/graphs/' + graph.filename)
        print('Graph generated in /res/graphs/' + graph.filename)

def list_to_csv(parsed_data):
    try:
        open('../data/PER_full_data.csv', 'w')
    except:
        return 1
    out_file = open('../data/PER_full_data.csv', 'w')
    header = 'Fecha,Dia,Casos,NuevosCasos,%DifCasos,CasosActivos,NuevosCasesActivos,Fallecidos,NuevosFallecidos,'
    header += '%DifFallecidos,TasaLetalidad,Pruebas,NuevasPruebas,%DifPruebas,%PruebasPositivasDiarias,Recuperados,'
    header += 'NuevosRecuperados,%DifRecuperados,Hospitalizados,NuevosHospitalizados,%DifHospitalizados\n'
    out_file.write(header)
    for i in range(0, len(parsed_data[0])):
        line = str(parsed_data[0][i]) + "," + str(parsed_data[6][i]) + "," + \
            str(parsed_data[1][i]) + "," + str(parsed_data[7][i]) + "," + str(parsed_data[8][i]) + "," + str(parsed_data[18][i]) + "," + str(parsed_data[19][i]) + "," + \
            str(parsed_data[2][i]) + "," + str(parsed_data[9][i]) + "," + str(parsed_data[10][i]) + "," + str(parsed_data[17][i]) + "," + \
            str(parsed_data[3][i]) + "," + str(parsed_data[15][i]) + "," + str(parsed_data[16][i]) + "," + str(parsed_data[20][i]) + "," + \
            str(parsed_data[4][i]) + "," + str(parsed_data[11][i]) + "," + str(parsed_data[12][i]) + "," + \
            str(parsed_data[5][i]) + "," + str(parsed_data[13][i]) + "," + str(parsed_data[14][i]) + "\n" 
        out_file.write(line)
    out_file.close()
    print('Data successfully exported to /PER_full_data.csv')
    return 0

def export_tweets_to_file(tweets):
    try:
        file = open('../res/tweets.dat', 'w', encoding='utf-8')
        file.close()
    except:
        return 1
    with open('../res/tweets.dat', 'w', encoding='utf-8') as file:
        for t in tweets:
            file.write(t.message + '===\n')
    file.close()
    print('Tweets contents successfully exported in tweets.dat')
    return 0

def update_git_repo_win32(date):
    os.system('sh Windows_AutoUpdateRepo.sh "' + date + '"')

def update_git_repo_linux(date):
    os.system('./Linux_AutoUpdateRepo.sh "' + date + '"')
