import sys

sys.path.insert(0, '../utilities')

import DataUtility as du
import ConfigUtility as cu

def main():
    config = cu.Config('ParsePDFConfig.cl')
    dept_config = cu.Config(config.get_value('ConfigFilesDir') + '/' + config.get_value('DepartmentsIndex'))
    depto_num = int(config.get_value('DeptoNum'))
    distr_num = int(config.get_value('DistrNum'))


    pa_depto_hdr = config.get_value('PADepto_Hdr')
    for i in range(0, depto_num):
        table_filename = config.get_value('PADepto_Dir') + '/' + dept_config.get_value(str(i)) + '.csv'
        pa_depto_table = du.Table('n', filename=table_filename, header_index=pa_depto_hdr, delimiter=',')
        pa_depto_table.save_as_csv(table_filename)

    ca_depto_hdr = config.get_value('CasosAcumuladosDepto_Hdr')
    cp_edades_hdr = config.get_value('CasosPositivosEdades_Hdr')
    ma_depto_hdr = config.get_value('MuertesAcumuladasDepto_Hdr')
    ca_distr20_hdr = config.get_value('CasosAcumuDistrito2020P1_Hdr')
    ca_distr21_hdr = config.get_value('CasosAcumuDistrito2021P1_Hdr')
    ma_distr_hdr = config.get_value('MuertesAcumulaDistritoP1_Hdr')


    print(1)

main()