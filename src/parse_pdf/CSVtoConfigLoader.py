import sys

sys.path.insert(0, '../utilities')

import DataUtility as du
import ConfigUtility as cu

config = cu.Config('ParsePDFConfig.cl')
PDFAreas = du.Table('l', filename=config.get_value('ParsePDFDir') + '/' + config.get_value('PDFAreasCSV'))

with open(config.get_value('PDFAreasCL'), 'w') as f:
    for i in range(0, PDFAreas.rows):
        entry = PDFAreas.get_entry(i)
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
