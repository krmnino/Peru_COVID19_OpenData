import sys

sys.path.insert(0, '../utilities')
sys.path.insert(0, '../utilities/ConfigLoader')

import DataUtility as du
import ConfigLoader as cl

def generate_padepto_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load department index configuration file
    dept_config = cl.Config(top_level_directory + config.get_value('DepartmentsIndex'))
    # Get number of departments and processed table headers
    depto_num = int(dept_config.get_n_entries())
    processed_table_header = config.get_value('PADepto_PTHdr')
    # Generate department tables
    for i in range(0, depto_num):
        table_filename = top_level_directory + config.get_value('PADepto_Dir') + dept_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("PADepto: Generating table complete")

def generate_cadepto_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load department index configuration file
    dept_config = cl.Config(top_level_directory + config.get_value('DepartmentsIndex'))
    # Get number of departments and processed table headers
    depto_num = int(dept_config.get_n_entries())
    processed_table_header = config.get_value('CADepto_PTHdr')
    # Generate department tables
    for i in range(0, depto_num):
        table_filename = top_level_directory + config.get_value('CADepto_Dir') + dept_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("CADepto: Generating table complete")

def generate_cpedades_table():
     # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Get number of departments and processed table headers
    ca_edades_hdr = config.get_value('CPEdades_PTHdr')
    # Generate cases by age group table
    table_filename = top_level_directory + config.get_value('CPEdades_PTF')
    ca_edades_table = du.Table('n', filename=table_filename, header_index=ca_edades_hdr, delimiter=',')
    ca_edades_table.save_as_csv(table_filename)
    print("CPEdades: Generating table complete")

def generate_madepto_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load department index configuration file
    dept_config = cl.Config(top_level_directory + config.get_value('DepartmentsIndex'))
    # Get number of departments and processed table headers
    depto_num = int(dept_config.get_n_entries())
    processed_table_header = config.get_value('MADepto_PTHdr')
    # Generate department tables
    for i in range(0, depto_num):
        table_filename = top_level_directory + config.get_value('MADepto_Dir') + dept_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("MADepto: Generating table complete")

def generate_cadistr20_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load district index configuration file
    distr_config = cl.Config(top_level_directory + config.get_value('DistrictsIndex'))
    # Get number of district and processed table headers
    distr_num = int(distr_config.get_n_entries())
    processed_table_header = config.get_value('CADistr20_PTHdr')
    # Generate district tables
    for i in range(0, distr_num):
        table_filename = top_level_directory + config.get_value('CADistr20_Dir') + distr_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("CADistr20: Generating table complete")

def generate_cadistr21_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load district index configuration file
    distr_config = cl.Config(top_level_directory + config.get_value('DistrictsIndex'))
    # Get number of district and processed table headers
    distr_num = int(distr_config.get_n_entries())
    processed_table_header = config.get_value('CADistr21_PTHdr')
    # Generate district tables
    for i in range(0, distr_num):
        table_filename = top_level_directory + config.get_value('CADistr21_Dir') + distr_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("CADistr21: Generating table complete")
    
def generate_madistr_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load district index configuration file
    distr_config = cl.Config(top_level_directory + config.get_value('DistrictsIndex'))
    # Get number of district and processed table headers
    distr_num = int(distr_config.get_n_entries())
    processed_table_header = config.get_value('MADistr_PTHdr')
    # Generate district tables
    for i in range(0, distr_num):
        table_filename = top_level_directory + config.get_value('MADistr_Dir') + distr_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("MADistr: Generating table complete")

def generate_madeptosm_tables():
    # Load main configuration file
    config = cl.Config('config/ParsePDFConfig.cl')
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = config.get_value('WindowsTopLevel')
    else:
        top_level_directory = config.get_value('LinuxTopLevel')
    # Load department index configuration file
    dept_config = cl.Config(top_level_directory + config.get_value('DepartmentsIndex'))
    # Get number of departments and processed table headers
    depto_num = int(dept_config.get_n_entries())
    processed_table_header = config.get_value('MADeptoSM_PTHdr')
    # Generate department tables
    for i in range(0, depto_num):
        table_filename = top_level_directory + config.get_value('MADeptoSM_Dir') + dept_config.get_value(str(i)) + '.csv'
        processed_table = du.Table('n', filename=table_filename, header_index=processed_table_header, delimiter=',')
        processed_table.save_as_csv(table_filename)
    print("MADeptoSM: Generating table complete")

def main():
    gen_padepto = True
    gen_cadepto = True
    gen_caedades = True
    gen_madepto = True
    gen_cadistr20 = True
    gen_cadistr21 = True
    gen_madistr = True
    gen_madeptosm = True

    if (gen_padepto):
        generate_padepto_tables()
    if (gen_cadepto):
        generate_cadepto_tables()
    if (gen_caedades):
        generate_cpedades_table()
    if (gen_madepto):
        generate_madepto_tables()
    if (gen_cadistr20):
        generate_cadistr20_tables()
    if (gen_cadistr21):
        generate_cadistr21_tables()
    if (gen_madistr):
        generate_madistr_tables()
    if (gen_madeptosm):
        generate_madeptosm_tables()

main()