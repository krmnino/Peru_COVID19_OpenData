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

    print(lines)
    


raw_data = parse_file()
if(raw_data == 1):
    print('Could not parse CSV file.')

data = compute_data(raw_data)

tweet_summary(data)