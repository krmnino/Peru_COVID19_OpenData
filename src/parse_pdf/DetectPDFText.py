import sys
from pdf2image import convert_from_path
import numpy as np
import cv2
from PIL import Image
from PIL import ImageOps 
from PIL import ImageEnhance
import pytesseract

sys.path.insert(0, '../utilities')

import ConfigUtility as cu    

if(sys.platform == 'win32'):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def process_pa_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    # Extract page from PDF file
    pa_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('PruebasAcumuladasDepto')),
                                 last_page=int(table_pg_config.get_value('PruebasAcumuladasDepto')),
                                 dpi=200)[0]
    # Apply postprocessing to image
    pa_depto = ImageOps.invert(pa_depto)
    pa_depto = ImageOps.grayscale(pa_depto)
    enhancer = ImageEnhance.Contrast(pa_depto)
    pa_depto = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_pa_depto = np.array(pa_depto)
    # Resize image to fit in 1080p screen
    cv2_pa_depto = cv2.resize(cv2_pa_depto, (w_width, w_height))
    # Select area and crop image
    bounds_pa_depto = cv2.selectROI('PruebasAcumuladasDepto', cv2_pa_depto, False, False)
    cv2.destroyWindow('PruebasAcumuladasDepto')
    cv2_pa_depto = cv2_pa_depto[int(bounds_pa_depto[1]):int(bounds_pa_depto[1]+bounds_pa_depto[3]),
                                int(bounds_pa_depto[0]):int(bounds_pa_depto[0]+bounds_pa_depto[2])]
    # Show cropped image if showimg = True
    if(showimg):
        cv2.imshow('test.jpeg', cv2_pa_depto)
        cv2.waitKey(0)
    img_pa_depto = Image.fromarray(cv2_pa_depto)
    # Perform OCR in PIL image with pytesseract
    pa_depto_data = pytesseract.image_to_string(img_pa_depto)
    print('PruebasAcumuladasDepto done.')


def process_ca_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    # Extract page from PDF file
    ca_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('CasosAcumuladosDepto')),
                                 last_page=int(table_pg_config.get_value('CasosAcumuladosDepto')),
                                 dpi=200)[0]
    # Apply postprocessing to image
    ca_depto = ImageOps.invert(ca_depto)
    ca_depto = ImageOps.grayscale(ca_depto)
    enhancer = ImageEnhance.Contrast(ca_depto)
    ca_depto = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_ca_depto = np.array(ca_depto)
    # Resize image to fit in 1080p screen
    cv2_ca_depto = cv2.resize(cv2_ca_depto, (w_width, w_height))
    # Select area and crop image
    bounds_ca_depto = cv2.selectROI('CasosAcumuladosDepto', cv2_ca_depto, False, False)
    cv2.destroyWindow('CasosAcumuladosDepto')
    cv2_ca_depto = cv2_ca_depto[int(bounds_ca_depto[1]):int(bounds_ca_depto[1]+bounds_ca_depto[3]),
                                int(bounds_ca_depto[0]):int(bounds_ca_depto[0]+bounds_ca_depto[2])]
    # Show cropped image if showimg = True
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_depto)
        cv2.waitKey(0)
    # Convert opencv2 image back to PIL image
    img_ca_depto = Image.fromarray(cv2_ca_depto)
    # Perform OCR in PIL image with pytesseract
    ca_depto_data = pytesseract.image_to_string(img_ca_depto)
    print('PruebasAcumuladasDepto done.')
    print('CasosAcumuladosDepto done.')


def process_cp_edades(table_pg_config, pdf_path, w_width, w_height, showimg):
    cp_edades = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('CasosPositivosEdades')),
                                 last_page=int(table_pg_config.get_value('CasosPositivosEdades')))[0]
    cv2_cp_edades = np.array(cp_edades)
    cv2_cp_edades = cv2.resize(cv2_cp_edades, (w_width, w_height))
    bounds_cp_edades = cv2.selectROI('CasosPositivosEdades', cv2_cp_edades, False, False)
    cv2.destroyWindow('CasosPositivosEdades')
    cv2_cp_edades = cv2_cp_edades[int(bounds_cp_edades[1]):int(bounds_cp_edades[1]+bounds_cp_edades[3]),
                                  int(bounds_cp_edades[0]):int(bounds_cp_edades[0]+bounds_cp_edades[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_cp_edades)
        cv2.waitKey(0)
    print('CasosPositivosEdades done.')


def process_ma_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    ma_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('MuertesAcumuladasDepto')),
                                 last_page=int(table_pg_config.get_value('MuertesAcumuladasDepto')))[0]
    cv2_ma_depto = np.array(ma_depto)
    cv2_ma_depto = cv2.resize(cv2_ma_depto, (w_width, w_height))
    bounds_ma_depto = cv2.selectROI('MuertesAcumuladasDepto', cv2_ma_depto, False, False)
    cv2.destroyWindow('MuertesAcumuladasDepto')
    cv2_ma_depto = cv2_ma_depto[int(bounds_ma_depto[1]):int(bounds_ma_depto[1]+bounds_ma_depto[3]),
                                int(bounds_ma_depto[0]):int(bounds_ma_depto[0]+bounds_ma_depto[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ma_depto)
        cv2.waitKey(0)
    print('MuertesAcumuladasDepto done.')


def process_ca_distr_20(table_pg_config, pdf_path, w_width, w_height, showimg):
    ca_distr_20 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CasosAcumuDistrito2020P1')),
                                    last_page=int(table_pg_config.get_value('CasosAcumuDistrito2020P1')))[0]
    cv2_ca_distr_20 = np.array(ca_distr_20)
    cv2_ca_distr_20 = cv2.resize(cv2_ca_distr_20, (w_width, w_height))
    bounds_ca_distr_20 = cv2.selectROI('CasosAcumuDistrito2020', cv2_ca_distr_20, False, False)
    cv2.destroyWindow('CasosAcumuDistrito2020')
    cv2_ca_distr_20 = cv2_ca_distr_20[int(bounds_ca_distr_20[1]):int(bounds_ca_distr_20[1]+bounds_ca_distr_20[3]),
                                      int(bounds_ca_distr_20[0]):int(bounds_ca_distr_20[0]+bounds_ca_distr_20[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_distr_20)
        cv2.waitKey(0)
    print('CasosAcumuDistrito2020 done.')


def process_ca_distr_21(table_pg_config, pdf_path, w_width, w_height, showimg):
    ca_distr_21 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CasosAcumuDistrito2021P1')),
                                    last_page=int(table_pg_config.get_value('CasosAcumuDistrito2021P1')))[0]
    cv2_ca_distr_21 = np.array(ca_distr_21)
    cv2_ca_distr_21 = cv2.resize(cv2_ca_distr_21, (w_width, w_height))
    bounds_ca_distr_21 = cv2.selectROI('CasosAcumuDistrito2021', cv2_ca_distr_21, False, False)
    cv2.destroyWindow('CasosAcumuDistrito2021')
    cv2_ca_distr_21 = cv2_ca_distr_21[int(bounds_ca_distr_21[1]):int(bounds_ca_distr_21[1]+bounds_ca_distr_21[3]),
                                      int(bounds_ca_distr_21[0]):int(bounds_ca_distr_21[0]+bounds_ca_distr_21[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_distr_21)
        cv2.waitKey(0)
    print('CasosAcumuDistrito2021 done.')


def process_ma_distr(table_pg_config, pdf_path, w_width, w_height, showimg):
    ma_distr = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('MuertesAcumulaDistritoP1')),
                                 last_page=int(table_pg_config.get_value('MuertesAcumulaDistritoP1')))[0]
    cv2_ma_distr = np.array(ma_distr)
    cv2_ma_distr = cv2.resize(cv2_ma_distr, (w_width, w_height))
    bounds_ma_distr = cv2.selectROI('MuertesAcumulaDistrito', cv2_ma_distr, False, False)
    cv2.destroyWindow('MuertesAcumulaDistrito')
    cv2_ma_distr = cv2_ma_distr[int(bounds_ma_distr[1]):int(bounds_ma_distr[1]+bounds_ma_distr[3]),
                                int(bounds_ma_distr[0]):int(bounds_ma_distr[0]+bounds_ma_distr[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ma_distr)
        cv2.waitKey(0)
    print('MuertesAcumulaDistrito done.')

#####################################################################################################

def main():
    table_pg_config = cu.Config('PDFTablePages.cl')
    pdf_path = table_pg_config.get_value('ReportPath') + table_pg_config.get_value('ReportName')
    w_width = 1760
    w_height = 990

    process_pa_depto(table_pg_config, pdf_path, w_width, w_height, True)
    #process_ca_depto(table_pg_config, pdf_path, w_width, w_height, False)
    #process_cp_edades(table_pg_config, pdf_path, w_width, w_height, False)
    #process_ma_depto(table_pg_config, pdf_path, w_width, w_height, False)
    #process_ca_distr_20(table_pg_config, pdf_path, w_width, w_height, False)
    #process_ca_distr_21(table_pg_config, pdf_path, w_width, w_height, False)
    #process_ma_distr(table_pg_config, pdf_path, w_width, w_height, False)
    
#####################################################################################################

main()
    