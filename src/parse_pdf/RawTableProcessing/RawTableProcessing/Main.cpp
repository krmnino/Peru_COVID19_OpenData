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
		Table* input_raw_table;
		process_pa_depto(input_raw_table, main_config, areas_config, dept_index);
		append_end_pa_depto(input_raw_table, main_config, areas_config, dept_index);

		delete input_raw_table;
	}

	// Process CasosAcumuladosDepto.csv
	{
		Table* input_raw_table;
		process_ca_depto(input_raw_table, main_config, areas_config, dept_index);
		append_end_ca_depto(input_raw_table, main_config, areas_config, dept_index);
		delete input_raw_table;
	}

	// Process CasosPositivosEdades.csv
	{
		Table* input_raw_table;
		process_cp_edades(input_raw_table, main_config, areas_config, age_index);
		append_end_cp_edades(input_raw_table, main_config, areas_config, age_index);
		delete input_raw_table;
	}

	// Process MuertesAcumuladasDepto.csv
	{
		Table* input_raw_table;
		process_ma_depto(input_raw_table, main_config, areas_config, dept_index);
		delete input_raw_table;
	}

	// Process CasosAcumuDistrito2020P1.csv
	// Process CasosAcumuDistrito2020P2.csv
	{
		Table* input_raw_table_p1;
		Table* input_raw_table_p2;
		process_ca_distr_20(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, dept_index);
		delete input_raw_table_p1;
		delete input_raw_table_p2;
	}
	
	// Process CasosAcumuDistrito2021P1.csv
	// Process CasosAcumuDistrito2021P2.csv
	{
		Table* input_raw_table_p1;
		Table* input_raw_table_p2;
		process_ca_distr_20(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, dept_index);
		delete input_raw_table_p1;
		delete input_raw_table_p2;
	}
	
	return 0;
}