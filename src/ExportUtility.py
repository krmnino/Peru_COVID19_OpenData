import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import warnings
import os 
from TwitterUtility import Tweet


class GraphData:
    x_data = None
    y_data = []
    x_label = ''
    y_data_labels = []
    colors = []
    title = ''
    suptitle = ''
    filename = ''
    date = ''
    tick_markers = False
    def __init__(self, x_data_, y_data_, x_label_, y_data_labels_, colors_, title_, suptitle_, filename_, date_, tick_markers_):
        self.x_data = x_data_
        self.y_data = y_data_
        self.x_label = x_label_
        self.y_data_labels = y_data_labels_
        self.colors = colors_
        self.title = title_
        self.suptitle = suptitle_
        self.filename = filename_
        self.date = date_
        self.tick_markers = tick_markers_

def plot_loader(graph_data):
    warnings.filterwarnings('ignore')
    for graph in graph_data:
        plt.figure(figsize=(14,10))
        plt.ticklabel_format(style='plain')
        plt.suptitle(graph.suptitle)
        plt.title(graph.title, fontdict={'fontsize' : 25})
        for i in range(0, len(graph.y_data)):
            plt.plot(graph.x_data, graph.y_data[i], graph.colors[i], label=graph.y_data_labels[i])
            if(graph.tick_markers):
                plt.plot(graph.x_data, graph.y_data[i], 'ko')
        plt.xlabel(graph.x_label)
        plt.ylabel(''.join(i + str(' ,') for i in graph.y_data_labels)[:-2])
        if(len(graph.x_data) == 30):
            plt.xticks(graph.x_data[::2], rotation=90)
            plt.locator_params(axis='x', nbins=len(graph.x_data)/2)
        else:
            plt.xticks(graph.x_data[::5], rotation=90)
            plt.locator_params(axis='x', nbins=len(graph.x_data)/5)
        plt.grid()
        plt.savefig('../res/graphs/' + graph.filename)
        print('Graph generated in /res/graphs/' + graph.filename)

def plot_graph(x, y, color, x_label, y_label, chart_title, file_name, date, y_min=-1, y_max=-1):
    warnings.filterwarnings('ignore')
    plt.figure(figsize=(14,10))
    plt.ticklabel_format(style='plain')
    plt.plot(x, y, 'ko', x, y, color)
    plt.title(chart_title, fontdict={'fontsize' : 25})
    plt.suptitle(date + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if(len(x) == 30):
        plt.xticks(x[::2], rotation=90)
        plt.locator_params(axis='x', nbins=len(x)/2)
    else:
        plt.xticks(x[::5], rotation=90)
        plt.locator_params(axis='x', nbins=len(x)/5)
    if(y_min != -1):
        plt.ylim(bottom=y_min)
    if(y_max != -1):
        plt.ylim(top=y_max)
    plt.grid()
    plt.savefig('../res/graphs/' + file_name)
    print('Graph generated in /res/graphs/' + file_name)

def plot_triple_graph(x, y1, y2, y3, color1, color2, color3, x_label, y_label1, y_label2, y_label3, chart_title, file_name, date, y_min=-1, y_max=-1):
    warnings.filterwarnings('ignore')
    plt.figure(figsize=(14,10))
    plt.ticklabel_format(style='plain')
    plt.plot(x, y1, 'ko')
    plt.plot(x, y1, color1, label=y_label1)
    plt.plot(x, y2, 'ko')
    plt.plot(x, y2, color2, label=y_label2)
    plt.plot(x, y3, 'ko')
    plt.plot(x, y3, color3, label=y_label3)
    plt.title(chart_title, fontdict={'fontsize' : 20})
    plt.suptitle(date + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)')
    plt.legend(loc="upper left")
    plt.xlabel(x_label)
    plt.ylabel(y_label1 + ', ' + y_label2 + ', ' + y_label3)
    if(y_min != -1):
        plt.ylim(bottom=y_min)
    if(y_max != -1):
        plt.ylim(top=y_max)
    plt.grid()
    if(len(x) == 30):
        plt.xticks(x[::2], rotation=90)
        plt.locator_params(axis='x', nbins=len(x)/2)
    else:
        plt.xticks(x[::5], rotation=90)
        plt.locator_params(axis='x', nbins=len(x)/5)
    plt.savefig('../res/graphs/' + file_name)
    plt.clf()
    print('Graph generated in /res/graphs/' + file_name)

def list_to_csv(parsed_data):
    try:
        open('../data/PER_full_data.csv', 'w')
    except:
        return 1
    out_file = open('../data/PER_full_data.csv', 'w')
    header = 'Fecha,Dia,Casos,NuevosCasos,%DifCases,CasosActivos,NuevosCasesActivos,Fallecidos,NuevasFallecidos,'
    header += '%DifFallecidos,TasaMortalidad,Pruebas,NuevasPruebas,%DifTests,%PruebasPositivasDiarias,Recuperados,'
    header += 'NuevosRecuperados,%DifRecuperados,Hospitalizados,NuevosHospitalizados,%DiffHospitalized\n'
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
        file = open('../res/tweets.dat', 'w')
        file.close()
    except:
        return 1
    with open('../res/tweets.dat', 'w') as file:
        for t in tweets:
            file.write(t.message + '===\n')
    file.close()
    print('Tweets contents successfully exported in tweets.dat')
    return 0

def update_git_repo(date):
    os.system('./AutoUpdateRepo.sh "' + date + '"')
