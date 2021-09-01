import sys

sys.path.insert(0, '../utilities')

import DataUtility as du
import ConfigUtility as cu

def main():
    config = cu.Config('ParsePDFConfig.cl')
    dept_config = cu.Config(config.get_value('ConfigFilesDir') + '/' + config.get_value('DepartmentsIndex'))
    distr_config = cu.Config(config.get_value('ConfigFilesDir') + '/' + config.get_value('DistrictsIndex'))
    depto_num = int(dept_config.get_n_entries()) - 1
    distr_num = int(distr_config.get_n_entries()) - 1

    ########################################################################################################

    pa_depto_hdr = config.get_value('PADepto_Hdr')
    for i in range(0, depto_num):
        table_filename = config.get_value('PADepto_Dir') + '/' + dept_config.get_value(str(i)) + '.csv'
        pa_depto_table = du.Table('n', filename=table_filename, header_index=pa_depto_hdr, delimiter=',')
        pa_depto_table.save_as_csv(table_filename)
    print("PADepto: Generating table complete")

    ########################################################################################################

    ca_depto_hdr = config.get_value('CADepto_Hdr')
    for i in range(0, depto_num):
        table_filename = config.get_value('CADepto_Dir') + '/' + dept_config.get_value(str(i)) + '.csv'
        ca_depto_table = du.Table('n', filename=table_filename, header_index=ca_depto_hdr, delimiter=',')
        ca_depto_table.save_as_csv(table_filename)
    print("CADepto: Generating table complete")

    ########################################################################################################

    ca_edades_hdr = config.get_value('CAEdades_Hdr')
    table_filename = config.get_value('CAEdades_Dir') + '/' + config.get_value('CAEdades_Table')
    ca_edades_table = du.Table('n', filename=table_filename, header_index=ca_edades_hdr, delimiter=',')
    ca_edades_table.save_as_csv(table_filename)
    print("CAEdades: Generating table complete")

    ########################################################################################################

    ma_depto_hdr = config.get_value('MADepto_Hdr')
    for i in range(0, depto_num):
        table_filename = config.get_value('MADepto_Dir') + '/' + dept_config.get_value(str(i)) + '.csv'
        ca_depto_table = du.Table('n', filename=table_filename, header_index=ma_depto_hdr, delimiter=',')
        ca_depto_table.save_as_csv(table_filename)
    print("MADepto: Generating table complete")
        
    ########################################################################################################

    ca_distr20_hdr = config.get_value('CADistr20_Hdr')
    for i in range(0, distr_num):
        table_filename = config.get_value('CADistr20_Dir') + '/' + distr_config.get_value(str(i)) + '.csv'
        ca_distr20_table = du.Table('n', filename=table_filename, header_index=ca_distr20_hdr, delimiter=',')
        ca_distr20_table.save_as_csv(table_filename)
    print("CADistr20: Generating table complete")

    ########################################################################################################
    
    ca_distr21_hdr = config.get_value('CADistr21_Hdr')
    for i in range(0, distr_num):
        table_filename = config.get_value('CADistr21_Dir') + '/' + distr_config.get_value(str(i)) + '.csv'
        ca_distr21_table = du.Table('n', filename=table_filename, header_index=ca_distr21_hdr, delimiter=',')
        ca_distr21_table.save_as_csv(table_filename)
    print("CADistr21: Generating table complete")

    ########################################################################################################

    ma_distr_hdr = config.get_value('MADistr_Hdr')
    for i in range(0, distr_num):
        table_filename = config.get_value('MADistr_Dir') + '/' + distr_config.get_value(str(i)) + '.csv'
        ma_distr_table = du.Table('n', filename=table_filename, header_index=ma_distr_hdr, delimiter=',')
        ma_distr_table.save_as_csv(table_filename)
    print("MADistr: Generating table complete")

    
main()