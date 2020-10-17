import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import warnings
import os 


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
    header += '%DifDeaths,TasaMortalidad,Pruebas,NuevasPruebas,%DifTests,%PruebasPositivasDiarias,Recuperados,'
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

def first_tweet(prev_diff, curr_diff, data, cases24h):
    out = 'ANALISIS DIARIO del #COVID19 en #PERU (1/2)\n'
    if(prev_diff[1] <= curr_diff[1]):
        #out += u'\U0001F534' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'
        out += '- Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'
    else:
        #out += u'\U0001F7E2' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'
        out +=  '- Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'

    out += '  -> (+' + str(cases24h) + ') ultimas 24 hrs\n'
    out += '  -> (+' + str(int(curr_diff[1]) - cases24h) + ') 7 dias anteriores\n'
    
    if(prev_diff[6] < curr_diff[6]):
        #out += u'\U0001F534' + ' Activos: ' + str(int(curr_diff[6])) + ' ('
        out += '- Activos: ' + str(int(curr_diff[6])) + ' ('
        if(int(curr_diff[7]) > 0):
            out += '+'
        out += str(int(curr_diff[7])) + ')' + '\n'
    else:
        #out += u'\U0001F7E2' + ' Activos: ' + str(int(curr_diff[6])) + ' (' 
        out += '- Activos: ' + str(int(curr_diff[6])) + ' (' 
        if(int(curr_diff[7]) > 0):
            out += '+'
        out += str(int(curr_diff[7])) + ')' + '\n'

    if(prev_diff[3] <= curr_diff[3]):
        #out += u'\U0001F7E2' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
        out += '- Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
    else:
        #out += u'\U0001F534' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
        out += '- Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'

    if(data[20][len(data[20])-2] <= data[20][len(data[20])-1]):
        #out += u'\U0001F534' + ' Positividad diaria: ' + str((curr_diff[8]) * 100)[:5] + '%\n'
        out += '- Positividad diaria: ' + str((curr_diff[8]) * 100)[:5] + '%\n'
    else:
        #out += u'\U0001F7E2' + ' Positividad diaria: ' + str((curr_diff[8]) * 100)[:5] + '%\n'
        out += '- Positividad diaria: ' + str((curr_diff[8]) * 100)[:5] + '%\n'

    return out

def second_tweet(prev_diff, curr_diff, data):
    out = 'ANALISIS DIARIO del #COVID19 en #PERU (2/2)\n'
    if(prev_diff[2] <= curr_diff[2]):
        #out += u'\U0001F534' + ' Fallecidos: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'
        out += '- Fallecidos: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'
    else:
        #out += u'\U0001F7E2' + ' Fallecidos: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'
        out += 'Fallecidos: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'

    if(data[17][len(data[17])-2] <= data[17][len(data[17])-1]):
        #out += u'\U0001F534' + ' Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
        out += '- Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
    else:
        #out += u'\U0001F7E2' + ' Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
        out += '- Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'

    if(prev_diff[1] <= curr_diff[1]):
        #out += u'\U0001F534' + ' Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'
        out += '- Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'
    else:
        #out += u'\U0001F7E2' + ' Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'
        out += '- Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'
    
    if(data[5][len(data[5])-2] <= data[5][len(data[5])-1]):
        #out += u'\U0001F534' + ' Hospitalizados: ' + str(int(data[5][len(data[5])-1])) + ' (+' + str(int(curr_diff[4])) + ')\n'
        out += '- Hospitalizados: ' + str(int(data[5][len(data[5])-1])) + ' (+' + str(int(curr_diff[4])) + ')\n'
    else:
        #out += u'\U0001F7E2' + ' Hospitalizados: ' + str(int(data[5][len(data[5])-1])) + ' (' + str(int(curr_diff[4])) + ')\n'
        out += '- Hospitalizados: ' + str(int(data[5][len(data[5])-1])) + ' (' + str(int(curr_diff[4])) + ')\n'
    return out

def repo_tweet(date):
    out = 'Repositorio de datos sobre el #COVID19 en #Peru actualizado al dia ' + date + '\n'
    out += 'Sugerencias son bienvenidas!\n'
    out += u'\U0001F4C8' + ' Disponible en formato .CSV y .JSON\n'
    out += u'\U0001F30E' + ' WEB https://krmnino.github.io/Peru_COVID19_OpenData/\n'
    out += u'\U0001F4C1' + ' REPO https://github.com/krmnino/Peru_COVID19_OpenData\n'
    return out

def export_tweets_to_file(tweet_contents):
    try:
        file = open('../res/tweets.dat', 'w')
        file.close()
    except:
        return 1
    with open('../res/tweets.dat', 'w') as file:
        for tweet in tweet_contents:
            file.write(tweet + '===\n')
    file.close()
    print('Tweets contents successfully exported in tweets.dat')
    return 0

def update_git_repo(date):
    os.system('./AutoUpdateRepo.sh "' + date + '"')
