from ParsingUtility import parse_file
from ParsingUtility import compute_data

def tweet_summary(data):
    lines = []

    out = ''
    out += u'\U0001F534 Casos: ' + str(int(data[1][len(data[0])-1])) \
        if data[7][len(data[0])-1] >= data[7][len(data[0])-2] \
        else u'\U0001F7E2 Casos: ' + str(int(data[1][len(data[1])-1]))
    out += ' (+' + str(int(data[7][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Activos: ' + str(int(data[18][len(data[0])-1])) \
        if data[19][len(data[0])-1] >= data[19][len(data[0])-2] \
        else u'\U0001F7E2 Activos: ' + str(int(data[18][len(data[0])-1]))
    out += ' (+' + str(int(data[19][len(data[0])-1])) + ')\n' \
        if data[19][len(data[0])-1] > 0 \
        else ' (' + str(int(data[19][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F7E2 Recovered: ' + str(int(data[4][len(data[0])-1])) \
        if data[11][len(data[0])-1] >= data[11][len(data[0])-2] \
        else u'\U0001F534 Recovered: ' + str(int(data[18][len(data[0])-1]))
    out += ' (+' + str(int(data[11][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Positividad Diaria: ' + str(round(data[20][len(data[0])-1] * 100, 2)) + '%' \
        if data[20][len(data[0])-1] >= data[20][len(data[0])-2] \
        else u'\U0001F7E2 Positividad Diaria: ' + str(round(data[20][len(data[0])-1] * 100, 2)) + '%'
    out += ' (+' + str(round((data[20][len(data[0])-1] - data[20][len(data[0])-2]) * 100, 2)) + '%)\n' \
        if data[20][len(data[0])-1] - data[20][len(data[0])-2] > 0 \
        else ' (' + str(round((data[20][len(data[0])-1] - data[20][len(data[0])-2]) * 100, 2)) + '%)\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Fallecidos: ' + str(int(data[2][len(data[0])-1])) \
        if data[9][len(data[0])-1] >= data[9][len(data[0])-2] \
        else u'\U0001F7E2 Fallecidos: ' + str(int(data[2][len(data[1])-1]))
    out += ' (+' + str(int(data[9][len(data[0])-1])) + ')\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Tasa Mortalidad: ' + str(round(data[17][len(data[0])-1] * 100, 4)) + '%' \
        if data[17][len(data[0])-1] >= data[17][len(data[0])-2] \
        else u'\U0001F7E2 Tasa Mortalidad: ' + str(round(data[17][len(data[0])-1] * 100, 4)) + '%'
    out += ' (+' + str(round((data[17][len(data[0])-1] - data[17][len(data[0])-2]) * 100, 4)) + '%)\n' \
        if data[17][len(data[0])-1] - data[17][len(data[0])-2] > 0 \
        else ' (' + str(round((data[17][len(data[0])-1] - data[17][len(data[0])-2]) * 100, 4)) + '%)\n'
    lines.append(out)

    out = ''
    out += u'\U0001F534 Hospitalizados: ' + str(int(data[5][len(data[0])-1])) \
        if data[13][len(data[0])-2] >= data[13][len(data[0])-3] \
        else u'\U0001F7E2 Hospitalizados: ' + str(int(data[5][len(data[0])-1]))
    out += ' (+' + str(int(data[13][len(data[0])-1])) + ')\n' \
        if data[13][len(data[0])-1] > 0 \
        else ' (' + str(int(data[13][len(data[0])-1])) + ')\n'
    lines.append(out)

    print(lines)
    


raw_data = parse_file()
if(raw_data == 1):
    print('Could not parse CSV file.')

data = compute_data(raw_data)

tweet_summary(data)