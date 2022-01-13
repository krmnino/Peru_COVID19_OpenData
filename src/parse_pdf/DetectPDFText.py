import sys
from pdf2image import convert_from_path

sys.path.insert(0, '../utilities')

import ConfigUtility as cu    

def main():
    config = cu.Config('PDFTablePages.cl')
    pdf_path = config.get_value('ReportPath') + config.get_value('ReportName')
    print(pdf_path)

    pa_depto = convert_from_path(pdf_path,
                                 first_page=int(config.get_value('PruebasAcumuladasDepto')),
                                 last_page=int(config.get_value('PruebasAcumuladasDepto')))[0]
    print('PruebasAcumuladasDepto done.')

    ca_depto = convert_from_path(pdf_path,
                                 first_page=int(config.get_value('CasosAcumuladosDepto')),
                                 last_page=int(config.get_value('CasosAcumuladosDepto')))[0]
    print('CasosAcumuladosDepto done.')

    cp_edades = convert_from_path(pdf_path,
                                 first_page=int(config.get_value('CasosPositivosEdades')),
                                 last_page=int(config.get_value('CasosPositivosEdades')))[0]
    print('CasosPositivosEdades done.')

    ma_depto = convert_from_path(pdf_path,
                                 first_page=int(config.get_value('MuertesAcumuladasDepto')),
                                 last_page=int(config.get_value('MuertesAcumuladasDepto')))[0]
    print('MuertesAcumuladasDepto done.')

    ca_distr_20 = convert_from_path(pdf_path,
                                    first_page=int(config.get_value('CasosAcumuDistrito2020P1')),
                                    last_page=int(config.get_value('CasosAcumuDistrito2020P1')))[0]
    print('CasosAcumuDistrito2020 done.')

    ca_distr_21 = convert_from_path(pdf_path,
                                    first_page=int(config.get_value('CasosAcumuDistrito2021P1')),
                                    last_page=int(config.get_value('CasosAcumuDistrito2021P1')))[0]
    print('CasosAcumuDistrito2021 done.')

    ma_distr = convert_from_path(pdf_path,
                                 first_page=int(config.get_value('MuertesAcumulaDistritoP1')),
                                 last_page=int(config.get_value('MuertesAcumulaDistritoP1')))[0]
    print('MuertesAcumulaDistrito done.')
    
    #image = images[0]
    #image = image.crop((100, 100, 500, 500))
    #pageObj = pdf_file.getPage(int(config.get_value('DatosResumen'))-1) 
        
    #image.save('slide.jpeg')
    #print(len(images))
        

main()
    