import sys
import PyPDF2 

sys.path.insert(0, '../utilities/ConfigLoader')

import ConfigLoader as cl

def main():
    config = cl.Config('PDFTablePages.cl')
    pdf_path = config.get_value('ReportPath') + '/' + config.get_value('ReportName')

    with open(pdf_path, 'rb') as file:
        pdf_file = PyPDF2.PdfFileReader(file) 
        pageObj = pdf_file.getPage(int(config.get_value('DatosResumen'))-1) 
        split_lines = pageObj.extractText().split('\n')
        print(split_lines)

main()
    