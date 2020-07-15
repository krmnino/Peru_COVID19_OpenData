import matplotlib.pyplot as plt
import warnings

def plot_graph(x, y, color, x_label, y_label, chart_title, file_name, date):
    warnings.filterwarnings('ignore')
    plt.figure(figsize=(14,10))
    plt.ticklabel_format(style='plain')
    plt.plot(x, y, 'ko', x, y, color)
    plt.title(chart_title, fontdict={'fontsize' : 25})
    plt.suptitle(date + ' | Elaborado por Kurt Manrique-Nino (@krm_nino) | Datos del Ministerio de Salud del Peru (@Minsa_Peru)')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.savefig('../graphs/' + file_name)
    print('Graph generated in graphs/' + file_name)

def list_to_csv(parsed_data):
    try:
        open('../PER_full_data.csv', 'w')
    except:
        print('Could not export processed data.')
        return 
    out_file = open('../PER_full_data.csv', 'w')
    out_file.write('Fecha,Dia,Casos,NuevosCasos,%DifCases,CasosActivos,NuevosCasesActivos,Muertes,NuevasMuertes,%DifDeaths,TasaMortalidad,Pruebas,NuevasPruebas,\
            %DifTests,%PruebasPositivasDiarias,Recuperados,NuevosRecuperados,%DifRecuperados,Hospitalizados,NuevosHospitalizados,%DiffHospitalized\n')
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

def tweet_highlights(prev_diff, curr_diff, data):
    out = 'Info destacada de hoy en #Peru - #COVID19\n'
    if(prev_diff[1] <= curr_diff[1]):
        out += u'\U0001F534' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'

    if(prev_diff[2] <= curr_diff[2]):
        out += u'\U0001F534' + ' Muertes: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Muertes: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'

    if(data[18][len(data[18])-2] <= data[18][len(data[18])-1]):
        out += u'\U0001F534' + ' Casos Activos: ' + str(int(curr_diff[6])) + ' (+' + str(int(curr_diff[7])) + ')' + '\n'
    else:
        out += u'\U0001F7E2' + ' Casos Activos: ' + str(int(curr_diff[6])) + ' (' + str(int(curr_diff[7])) + ')' + '\n'

    if(prev_diff[3] <= curr_diff[3]):
        out += u'\U0001F7E2' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
    else:
        out += u'\U0001F534' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'

    if(data[5][len(data[5])-2] <= data[5][len(data[5])-1]):
        out += u'\U0001F534' + ' Hospital.: ' + str(int(data[5][len(data[5])-1])) + ' (+' + str(int(curr_diff[4])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Hospital.: ' + str(int(data[5][len(data[5])-1])) + ' (' + str(int(curr_diff[4])) + ')\n'

    if(data[20][len(data[20])-2] <= data[20][len(data[20])-1]):
        out += u'\U0001F534' + ' % Pruebas Positivas: ' + str((curr_diff[8]) * 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' % Pruebas Positivas: ' + str((curr_diff[8]) * 100)[:5] + '%\n'

    if(data[17][len(data[17])-2] <= data[17][len(data[17])-1]):
        out += u'\U0001F534' + ' Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
    print(out)
    print(len(out))
    return out
    
def tweet_cases(prev_diff, curr_diff, data):
    out = 'Casos de #COVID19 en #Peru\n'
    if(prev_diff[1] <= curr_diff[1]):
        out += u'\U0001F534' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Casos: ' + str(int(data[1][len(data[1])-1])) + ' (+' + str(int(curr_diff[1])) + ')\n'

    if(data[8][len(data[8])-2] <= data[8][len(data[8])-1]):
        out += u'\U0001F534' + ' Tasa de Crecimiento: ' + str(data[8][len(data[8])-1] * 100 - 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' Tasa de Crecimiento: ' + str(data[8][len(data[8])-1] * 100 - 100)[:5] +'%\n'

    if(data[18][len(data[18])-2] <= data[18][len(data[18])-1]):
        out += u'\U0001F534' + ' Casos Activos: ' + str(int(curr_diff[6])) + ' (+' + str(int(curr_diff[7])) + ')' + '\n'
    else:
        out += u'\U0001F7E2' + ' Casos Activos: ' + str(int(curr_diff[6])) + ' (' + str(int(curr_diff[7])) + ')' + '\n'
    print(out)
    print(len(out))
    return out


def tweet_deaths(prev_diff, curr_diff, data):
    out = 'Muertes de #COVID19 en #Peru\n'
    if(prev_diff[1] <= curr_diff[1]):
        out += u'\U0001F534' + ' Muertes: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Muertes: ' + str(int(data[2][len(data[2])-1])) + ' (+' + str(int(curr_diff[2])) + ')\n'

    if(data[10][len(data[10])-2] <= data[10][len(data[10])-1]):
        out += u'\U0001F534' + ' Tasa de Crecimiento: ' + str(data[10][len(data[10])-1] * 100 - 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' Tasa de Crecimiento: ' + str(data[10][len(data[10])-1] * 100 - 100)[:5] +'%\n'

    if(data[17][len(data[17])-2] <= data[17][len(data[17])-1]):
        out += u'\U0001F534' + ' % Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' % Tasa Mortalidad: ' + str((curr_diff[9]) * 100)[:5] + '%\n'
    print(out)
    print(len(out))
    return out

def tweet_tests_hosp_rec(prev_diff, curr_diff, data):
    out = 'Tests, hospitalizados y recuperados de #COVID19 en #Peru\n'
    if(prev_diff[1] <= curr_diff[1]):
        out += u'\U0001F534' + ' Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Tests: ' + str(int(data[3][len(data[2])-1])) + ' (+' + str(int(curr_diff[5])) + ')\n'

    if(prev_diff[8] <= curr_diff[8]):
        out += u'\U0001F534' + ' % Pruebas Positivas Hoy: ' + str((curr_diff[8]) * 100)[:5] + '%\n'
    else:
        out += u'\U0001F7E2' + ' % Pruebas Positivas Hoy: ' + str((curr_diff[8]) * 100)[:5] + '%\n'

    if(prev_diff[3] <= curr_diff[3]):
        out += u'\U0001F7E2' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
    else:
        out += u'\U0001F534' + ' Recuperados: ' + str(int(data[4][len(data[4])-1])) + ' (+' + str(int(curr_diff[3])) + ')\n'
    
    if(data[12][len(data[12])-2] <= data[12][len(data[12])-1]):
        out += u'\U0001F7E2' + ' Tasa de Recup.: ' + str(data[12][len(data[12])-1] * 100 - 100)[:5] + '%\n'
    else:
        out += u'\U0001F534' + ' Tasa de Recup.: ' + str(data[12][len(data[12])-1] * 100 - 100)[:5] +'%\n'

    if(data[5][len(data[5])-2] <= data[5][len(data[5])-1]):
        out += u'\U0001F534' + ' Hospital.: ' + str(int(data[5][len(data[5])-1])) + ' (+' + str(int(curr_diff[4])) + ')\n'
    else:
        out += u'\U0001F7E2' + ' Hospital.: ' + str(int(data[5][len(data[5])-1])) + ' (' + str(int(curr_diff[4])) + ')\n'
    
    if(data[14][len(data[14])-2] <= data[14][len(data[14])-1]):
        out += u'\U0001F7E2' + ' Tasa de Hospital.: ' + str(data[14][len(data[14])-1] * 100 - 100)[:5] + '%\n'
    else:
        out += u'\U0001F534' + ' Tasa de Hospital.: ' + str(data[14][len(data[14])-1] * 100 - 100)[:5] +'%\n'
    print(out)
    print(len(out))
    return out

def tweet_repo(date):
    out = 'Repositorio de datos sobre el #COVID19 en #Peru actualizado al dia de hoy (' + date + ')\n'
    out += u'\U0001F4C8' + ' Disponible en formato CSV (Proximamente JSON)\n'
    out += u'\U0001F30E' + ' WEB https://krmnino.github.io/Peru_COVID19_Stats/\n'
    out += u'\U0001F4C1' + ' REPO https://github.com/krmnino/Peru_COVID19_Stats\n'
    print(out)
    print(len(out))
    return out

def export_tweets(tweet_contents):
    with open('tweets.dat', 'w') as file:
        for tweet in tweet_contents:
            file.write(tweet + '===\n')
    file.close

