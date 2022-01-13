import sys
from pdf2image import convert_from_path
import numpy as np
import cv2

sys.path.insert(0, '../utilities')

import ConfigUtility as cu    

def process_pa_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    pa_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('PruebasAcumuladasDepto')),
                                 last_page=int(table_pg_config.get_value('PruebasAcumuladasDepto')))[0]
    print('PruebasAcumuladasDepto done.')
    cv2_pa_depto = np.array(pa_depto)
    cv2_pa_depto = cv2.resize(cv2_pa_depto, (w_width, w_height))
    bounds_pa_depto = cv2.selectROI('PruebasAcumuladasDepto', cv2_pa_depto, False, False)
    cv2.destroyWindow('PruebasAcumuladasDepto')
    cv2_pa_depto = cv2_pa_depto[int(bounds_pa_depto[1]):int(bounds_pa_depto[1]+bounds_pa_depto[3]),
                                int(bounds_pa_depto[0]):int(bounds_pa_depto[0]+bounds_pa_depto[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_pa_depto)


def process_ca_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    ca_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('CasosAcumuladosDepto')),
                                 last_page=int(table_pg_config.get_value('CasosAcumuladosDepto')))[0]
    print('CasosAcumuladosDepto done.')
    cv2_ca_depto = np.array(ca_depto)
    cv2_ca_depto = cv2.resize(cv2_ca_depto, (w_width, w_height))
    bounds_ca_depto = cv2.selectROI('CasosAcumuladosDepto', cv2_ca_depto, False, False)
    cv2.destroyWindow('CasosAcumuladosDepto')
    cv2_ca_depto = cv2_ca_depto[int(bounds_ca_depto[1]):int(bounds_ca_depto[1]+bounds_ca_depto[3]),
                                int(bounds_ca_depto[0]):int(bounds_ca_depto[0]+bounds_ca_depto[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_depto)


def process_cp_edades(table_pg_config, pdf_path, w_width, w_height, showimg):
    cp_edades = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('CasosPositivosEdades')),
                                 last_page=int(table_pg_config.get_value('CasosPositivosEdades')))[0]
    print('CasosPositivosEdades done.')
    cv2_cp_edades = np.array(cp_edades)
    cv2_cp_edades = cv2.resize(cv2_cp_edades, (w_width, w_height))
    bounds_cp_edades = cv2.selectROI('CasosPositivosEdades', cv2_cp_edades, False, False)
    cv2.destroyWindow('CasosPositivosEdades')
    cv2_cp_edades = cv2_cp_edades[int(bounds_cp_edades[1]):int(bounds_cp_edades[1]+bounds_cp_edades[3]),
                                  int(bounds_cp_edades[0]):int(bounds_cp_edades[0]+bounds_cp_edades[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_cp_edades)


def process_ma_depto(table_pg_config, pdf_path, w_width, w_height, showimg):
    ma_depto = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('MuertesAcumuladasDepto')),
                                 last_page=int(table_pg_config.get_value('MuertesAcumuladasDepto')))[0]
    print('MuertesAcumuladasDepto done.')
    cv2_ma_depto = np.array(ma_depto)
    cv2_ma_depto = cv2.resize(cv2_ma_depto, (w_width, w_height))
    bounds_ma_depto = cv2.selectROI('MuertesAcumuladasDepto', cv2_ma_depto, False, False)
    cv2.destroyWindow('MuertesAcumuladasDepto')
    cv2_ma_depto = cv2_ma_depto[int(bounds_ma_depto[1]):int(bounds_ma_depto[1]+bounds_ma_depto[3]),
                                int(bounds_ma_depto[0]):int(bounds_ma_depto[0]+bounds_ma_depto[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ma_depto)


def process_ca_distr_20(table_pg_config, pdf_path, w_width, w_height, showimg):
    ca_distr_20 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CasosAcumuDistrito2020P1')),
                                    last_page=int(table_pg_config.get_value('CasosAcumuDistrito2020P1')))[0]
    print('CasosAcumuDistrito2020 done.')
    cv2_ca_distr_20 = np.array(ca_distr_20)
    cv2_ca_distr_20 = cv2.resize(cv2_ca_distr_20, (w_width, w_height))
    bounds_ca_distr_20 = cv2.selectROI('CasosAcumuDistrito2020', cv2_ca_distr_20, False, False)
    cv2.destroyWindow('CasosAcumuDistrito2020')
    cv2_ca_distr_20 = cv2_ca_distr_20[int(bounds_ca_distr_20[1]):int(bounds_ca_distr_20[1]+bounds_ca_distr_20[3]),
                                      int(bounds_ca_distr_20[0]):int(bounds_ca_distr_20[0]+bounds_ca_distr_20[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_distr_20)


def process_ca_distr_21(table_pg_config, pdf_path, w_width, w_height, showimg):
    ca_distr_21 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CasosAcumuDistrito2021P1')),
                                    last_page=int(table_pg_config.get_value('CasosAcumuDistrito2021P1')))[0]
    print('CasosAcumuDistrito2021 done.')
    cv2_ca_distr_21 = np.array(ca_distr_21)
    cv2_ca_distr_21 = cv2.resize(cv2_ca_distr_21, (w_width, w_height))
    bounds_ca_distr_21 = cv2.selectROI('CasosAcumuDistrito2021', cv2_ca_distr_21, False, False)
    cv2.destroyWindow('CasosAcumuDistrito2021')
    cv2_ca_distr_21 = cv2_ca_distr_21[int(bounds_ca_distr_21[1]):int(bounds_ca_distr_21[1]+bounds_ca_distr_21[3]),
                                      int(bounds_ca_distr_21[0]):int(bounds_ca_distr_21[0]+bounds_ca_distr_21[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ca_distr_21)


def process_ma_distr(table_pg_config, pdf_path, w_width, w_height, showimg):
    ma_distr = convert_from_path(pdf_path,
                                 first_page=int(table_pg_config.get_value('MuertesAcumulaDistritoP1')),
                                 last_page=int(table_pg_config.get_value('MuertesAcumulaDistritoP1')))[0]
    print('MuertesAcumulaDistrito done.')
    cv2_ma_distr = np.array(ma_distr)
    cv2_ma_distr = cv2.resize(cv2_ma_distr, (w_width, w_height))
    bounds_ma_distr = cv2.selectROI('MuertesAcumulaDistrito', cv2_ma_distr, False, False)
    cv2.destroyWindow('MuertesAcumulaDistrito')
    cv2_ma_distr = cv2_ma_distr[int(bounds_ma_distr[1]):int(bounds_ma_distr[1]+bounds_ma_distr[3]),
                                int(bounds_ma_distr[0]):int(bounds_ma_distr[0]+bounds_ma_distr[2])]
    if(showimg):
        cv2.imshow('test.jpeg', cv2_ma_distr)

#####################################################################################################

def main():
    table_pg_config = cu.Config('PDFTablePages.cl')
    pdf_path = table_pg_config.get_value('ReportPath') + table_pg_config.get_value('ReportName')
    w_width = 1280
    w_height = 720

    process_pa_depto(table_pg_config, pdf_path, w_width, w_height, False)
    process_ca_depto(table_pg_config, pdf_path, w_width, w_height, False)
    process_cp_edades(table_pg_config, pdf_path, w_width, w_height, False)
    process_ma_depto(table_pg_config, pdf_path, w_width, w_height, False)
    process_ca_distr_20(table_pg_config, pdf_path, w_width, w_height, False)
    process_ca_distr_21(table_pg_config, pdf_path, w_width, w_height, False)
    process_ma_distr(table_pg_config, pdf_path, w_width, w_height, False)
    
#####################################################################################################

main()
    