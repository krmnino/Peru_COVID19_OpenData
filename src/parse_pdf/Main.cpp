#include "RawTableProcessing.hpp"

#include <iostream>
#include <algorithm>

int main() {
	cl::Config* main_config = new cl::Config("../config/ParsePDFConfig.cl");
	std::string parse_pdf_dir = main_config->get_value("ParsePDFDir")->get_data<std::string>() + "/";
	std::string raw_tables_dir = main_config->get_value("RawTablesDir")->get_data<std::string>() + "/";
	std::string config_files_dir = main_config->get_value("ConfigFilesDir")->get_data<std::string>() + "/";
	cl::Config* areas_config = new cl::Config(parse_pdf_dir + main_config->get_value("PDFAreasCL")->get_data<std::string>());
	cl::Config* dept_index = new cl::Config(config_files_dir + main_config->get_value("DepartmentsIndex")->get_data<std::string>());
	cl::Config* distr_index = new cl::Config(config_files_dir + main_config->get_value("DistrictsIndex")->get_data<std::string>());
	cl::Config* age_index = new cl::Config(config_files_dir + main_config->get_value("AgeGroupsIndex")->get_data<std::string>());
	int n_tables = areas_config->get_n_entries();

	// Process PruebasAcumuladasDepto.csv
	{
		tl::Table* input_raw_table;
		process_pa_depto(input_raw_table, main_config, areas_config, dept_index);
		append_end_pa_depto(input_raw_table, main_config, areas_config, dept_index);
		//append_begin_pa_depto(input_raw_table, main_config, areas_config, dept_index);
		delete input_raw_table;
	}

	// Process CasosAcumuladosDepto.csv
	{
		tl::Table* input_raw_table;
		process_ca_depto(input_raw_table, main_config, areas_config, dept_index);
		append_end_ca_depto(input_raw_table, main_config, areas_config, dept_index);
		//append_begin_ca_depto(input_raw_table, main_config, areas_config, dept_index);
		delete input_raw_table;
	}

	// Process CasosPositivosEdades.csv
	{
		tl::Table* input_raw_table;
		process_cp_edades(input_raw_table, main_config, areas_config, age_index);
		append_end_cp_edades(input_raw_table, main_config, areas_config, age_index);
		//append_begin_cp_edades(input_raw_table, main_config, areas_config, age_index);
		delete input_raw_table;
	}

	// Process MuertesAcumuladasDepto.csv
	{
		tl::Table* input_raw_table;
		process_ma_depto(input_raw_table, main_config, areas_config, dept_index);
		append_end_ma_depto(input_raw_table, main_config, areas_config, dept_index);
		//append_begin_ma_depto(input_raw_table, main_config, areas_config, dept_index);
		delete input_raw_table;
	}

	//{
	//	Table* input_raw_table;
	//	process_ma_deptosm(input_raw_table, main_config, areas_config, dept_index);
	//	//append_end_ma_depto(input_raw_table, main_config, areas_config, dept_index);
	//	append_begin_ma_deptosm(input_raw_table, main_config, areas_config, dept_index);
	//	delete input_raw_table;
	//}

	// Process CasosAcumuDistrito2020P1.csv
	// Process CasosAcumuDistrito2020P2.csv
	{
		tl::Table* input_raw_table_p1;
		tl::Table* input_raw_table_p2;
		process_ca_distr_20(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
		append_end_ca_distr_20(input_raw_table_p1, main_config, areas_config, distr_index);
		//append_begin_ca_distr_20(input_raw_table_p1, main_config, areas_config, distr_index);
		delete input_raw_table_p1;
		delete input_raw_table_p2;
	}
	
	// Process CasosAcumuDistrito2021P1.csv
	// Process CasosAcumuDistrito2021P2.csv
	{
		tl::Table* input_raw_table_p1;
		tl::Table* input_raw_table_p2;
		process_ca_distr_21(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
		append_end_ca_distr_21(input_raw_table_p1, main_config, areas_config, distr_index);
		//append_begin_ca_distr_21(input_raw_table_p1, main_config, areas_config, distr_index);
		delete input_raw_table_p1;
		delete input_raw_table_p2;
	}

	// Process MuertesAcumulaDistritoP1.csv
	// Process MuertesAcumulaDistritoP2.csv
	{
		tl::Table* input_raw_table_p1;
		tl::Table* input_raw_table_p2;
		process_ma_distr(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
		append_end_ma_distr(input_raw_table_p1, main_config, areas_config, distr_index);
		//append_begin_ma_distr(input_raw_table_p1, main_config, areas_config, distr_index);
		delete input_raw_table_p1;
		delete input_raw_table_p2;
	}

	delete main_config;
	delete areas_config;
	delete dept_index;
	delete distr_index;
	delete age_index;
	
	return 0;
}