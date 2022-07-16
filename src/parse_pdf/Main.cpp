#include "RawTableProcessing.hpp"

#include <iostream>
#include <algorithm>

#ifdef LINUX
static std::string navigate = "";
#else
static std::string navigate = "../";
#endif // LINUX

int main() {
	std::string config_path;

	// Load main cofiguration file
	config_path = navigate + "config/ParsePDFConfig.cl";
	cl::Config* main_config = new cl::Config(config_path);

	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	// Get report date from PDF report filename
	std::string report_date = get_report_date(main_config);

	// Load Departments Index configuration file
	config_path = main_config->get_value("DepartmentsIndex")->get_data<std::string>();
	cl::Config* dept_index =  new cl::Config(top_level_path + config_path);

	// Load Districts Index configuration file
	config_path = main_config->get_value("DistrictsIndex")->get_data<std::string>();
	cl::Config* distr_index = new cl::Config(top_level_path + config_path);

	// Load Age Groups Index configuration file
	config_path = main_config->get_value("AgeGroupsIndex")->get_data<std::string>();
	cl::Config* age_index = new cl::Config(top_level_path + config_path);

	//int n_tables = areas_config->get_n_entries();
	
	// Process PruebasAcumuladasDepto.csv
	//{
	//	tl::Table* input_raw_table;
	//	process_pa_depto(input_raw_table, main_config, dept_index);
	//	append_end_pa_depto(input_raw_table, main_config, report_date, dept_index);
	//	//append_begin_pa_depto(input_raw_table, main_config, report_date, dept_index);
	//	delete input_raw_table;
	//}

	// Process CasosAcumuladosDepto.csv
	//{
	//	tl::Table* input_raw_table;
	//	process_ca_depto(input_raw_table, main_config, dept_index);
	//	append_end_ca_depto(input_raw_table, main_config, report_date, dept_index);
	//	//append_begin_ca_depto(input_raw_table, main_config, report_date, dept_index);
	//	delete input_raw_table;
	//}
	
	// Process CasosPositivosEdades.csv
	//{
	//	tl::Table* input_raw_table;
	//	process_cp_edades(input_raw_table, main_config, age_index);
	//	append_end_cp_edades(input_raw_table, main_config, report_date, age_index);
	//	//append_begin_cp_edades(input_raw_table, main_config, areas_config, age_index);
	//	delete input_raw_table;
	//}
	
	// Process MuertesAcumuladasDepto.csv
	{
		tl::Table* input_raw_table;
		process_ma_depto(input_raw_table, main_config, dept_index);
		append_end_ma_depto(input_raw_table, main_config, report_date, dept_index);
		//append_begin_ma_depto(input_raw_table, main_config, report_date, dept_index);
		delete input_raw_table;
	}

	//{
	//	Table* input_raw_table;
	//	process_ma_deptosm(input_raw_table, main_config, areas_config, dept_index);
	//	//append_end_ma_depto(input_raw_table, main_config, report_date, dept_index);
	//	append_begin_ma_deptosm(input_raw_table, main_config, report_date, dept_index);
	//	delete input_raw_table;
	//}

	// Process CasosAcumuDistrito2020P1.csv
	// Process CasosAcumuDistrito2020P2.csv
	//{
	//	tl::Table* input_raw_table_p1;
	//	tl::Table* input_raw_table_p2;
	//	process_ca_distr_20(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
	//	append_end_ca_distr_20(input_raw_table_p1, main_config, areas_config, distr_index);
	//	//append_begin_ca_distr_20(input_raw_table_p1, main_config, areas_config, distr_index);
	//	delete input_raw_table_p1;
	//	delete input_raw_table_p2;
	//}
	//
	//// Process CasosAcumuDistrito2021P1.csv
	//// Process CasosAcumuDistrito2021P2.csv
	//{
	//	tl::Table* input_raw_table_p1;
	//	tl::Table* input_raw_table_p2;
	//	process_ca_distr_21(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
	//	append_end_ca_distr_21(input_raw_table_p1, main_config, areas_config, distr_index);
	//	//append_begin_ca_distr_21(input_raw_table_p1, main_config, areas_config, distr_index);
	//	delete input_raw_table_p1;
	//	delete input_raw_table_p2;
	//}
	//
	//// Process MuertesAcumulaDistritoP1.csv
	//// Process MuertesAcumulaDistritoP2.csv
	//{
	//	tl::Table* input_raw_table_p1;
	//	tl::Table* input_raw_table_p2;
	//	process_ma_distr(input_raw_table_p1, input_raw_table_p2, main_config, areas_config, distr_index);
	//	append_end_ma_distr(input_raw_table_p1, main_config, areas_config, distr_index);
	//	//append_begin_ma_distr(input_raw_table_p1, main_config, areas_config, distr_index);
	//	delete input_raw_table_p1;
	//	delete input_raw_table_p2;
	//}
	//
	delete main_config;
	delete dept_index;
	delete distr_index;
	delete age_index;
	
	return 0;
}