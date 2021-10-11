import sys

sys.path.insert(0, '../utilities')

import DataUtility as du
import ConfigUtility as cu

def get_date(raw_str):
    raw_str = raw_str[11:]
    raw_str = raw_str[:len(raw_str)-4]
    day = raw_str[0:2]
    month = raw_str[2:4]
    year = '20' + raw_str[4:]
    return year + '-' + month + '-' + day

def main():
    config = cu.Config('ParsePDFConfig.cl')
    config_table_pages = cu.Config('PDFTablePages.cl')
    PDFAreas = du.Table('l', filename=config.get_value('ParsePDFDir') + '/' + config.get_value('PDFAreasCSV'), delimiter=',')

    with open(config.get_value('PDFAreasCL'), 'w') as f:
        for i in range(0, PDFAreas.rows - 2):
            entry = PDFAreas.get_row_data(i)
            entry_cl = ''
            key = ''
            values = []
            for i, val in enumerate(entry):
                if(i == 0):
                    key = entry[val]
                else:
                    values.append(entry[val])
            entry_cl += key + '=['
            for i in range(0, len(val)):
                if(i != len(val)-1):
                    entry_cl += str(values[i]) + ','
                else:
                    entry_cl += str(values[i]) + '];\n'
            f.write(entry_cl)
        date_str = get_date(config_table_pages.get_value('ReportName'))
        f.write('ReportPath = ' + list(PDFAreas.get_row_data(10).values())[5] + ';\n')
        f.write('ReportName = ' + list(PDFAreas.get_row_data(11).values())[5] + ';\n')
        f.write('Date = ' + date_str + ';\n')
    
main()