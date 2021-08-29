#include "RawTableProcessing.hpp"

#include <iostream>
#include <algorithm>


int main() {
	Config* main_config = new Config("../../ParsePDFConfig.cl");
	std::string parse_pdf_dir = *(std::string*)main_config->get_value("ParsePDFDir")->get_num_str_data().get_data() + "/";
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::string config_files_dir = *(std::string*)main_config->get_value("ConfigFilesDir")->get_num_str_data().get_data() + "/";
	Config* areas_config = new Config(parse_pdf_dir + *(std::string*)main_config->get_value("PDFAreasCL")->get_num_str_data().get_data());
	Config* dept_index = new Config(config_files_dir + *(std::string*)main_config->get_value("DepartmentsIndex")->get_num_str_data().get_data());
	Config* age_index = new Config(config_files_dir + *(std::string*)main_config->get_value("AgeGroupsIndex")->get_num_str_data().get_data());
	int n_tables = areas_config->get_n_pairs();


	// Process PruebasAcumuladasDepto.csv
	{
		Table* table;
		process_pa_depto(table, main_config, areas_config, dept_index);
		
		delete table;
	}

	// Process CasosAcumuladosDepto.csv
	{
		Table* table;
		process_ca_depto(table, main_config, areas_config, dept_index);
		delete table;
	}

	// Process CasosPositivosEdades.csv
	{
		Table* table;
		process_cp_edades(table, main_config, areas_config, dept_index);
		delete table;
	}

	// Process MuertesAcumuladasDepto.csv
	{
		Table* table;
		process_ma_depto(table, main_config, areas_config, dept_index);
		delete table;
	}

	// Process CasosAcumuDistrito2020P1.csv
	// Process CasosAcumuDistrito2020P2.csv
	{
		Table* table_p1;
		Table* table_p2;
		process_ca_distr_20(table_p1, table_p2, main_config, areas_config, dept_index);
		delete table_p1;
		delete table_p2;
	}
	
	// Process CasosAcumuDistrito2021P1.csv
	// Process CasosAcumuDistrito2021P2.csv
	{
		Table* table_p1;
		Table* table_p2;
		process_ca_distr_20(table_p1, table_p2, main_config, areas_config, dept_index);
		delete table_p1;
		delete table_p2;
	}
	
	return 0;
}