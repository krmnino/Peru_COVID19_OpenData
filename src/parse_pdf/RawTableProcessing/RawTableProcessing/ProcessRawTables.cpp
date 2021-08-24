#include "RawTableProcessing.hpp"

int check_data_type(std::string& data) {
	std::string::const_iterator it = data.begin();
	bool integer_type = false;
	bool decimal_point = false;
	bool string_type = true;
	while (it != data.end()) {
		if (*it == '.' && decimal_point) {
			// If decimal point appears more than once, then it is string type
			return 0;
		}
		if (*it == '.') {
			// If decimal point appears for the first time, then it may be a double
			decimal_point = true;
		}
		if (0 > * it || *it > 255) {
			// If char val is outside the ASCII range, then it is a string
			return 0;
		}
		else if (!std::isdigit(*it)) {
			// If non-digit value appears, then it is a string
			return 0;
		}
		it++;
	}
	if (decimal_point) {
		// If a decimal point appeared only once, then it is a double
		return 2;
	}
	else {
		// If all chars are digits and no decimal point, then it is a integer
		return 1;
	}
}

Variant convert_to_number(int idx, std::vector<std::vector<Variant>>& col) {
	Variant out;
	if (col[0][idx].get_type() == (int)DataType::STRING) {
		std::string raw_str = *(std::string*)col[0][idx].get_data();
		raw_str.erase(std::remove(raw_str.begin(), raw_str.end(), ','), raw_str.end());
		raw_str.erase(std::remove(raw_str.begin(), raw_str.end(), '"'), raw_str.end());
		switch (check_data_type(raw_str)) {
		case 0:
			out = raw_str;
			break;
		case 1:
			out = std::stoi(raw_str);
			break;
		case 2:
			out = std::stod(raw_str);
			break;
		default:
			break;
		}
	}
	else {
		out = col[0][idx];
	}
	return out;
}

void set_proper_col_names(Config& names_index, Table& raw_table) {
	for (int i = 0; i < raw_table.get_rows(); i++) {
		std::string itr_str = std::to_string(i);
		Variant value = names_index.get_value(itr_str)->get_num_str_data();
		std::string name_str = *(std::string*)value.get_data();
		Variant name_var(name_str);
		raw_table.update_cell_data(0, i, name_var);
	}
}

int process_pa_depto(Table*& raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config = areas_config->get_value("PruebasAcumuladasDepto")->get_list_data();
	raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
	std::vector<Variant> table_col_config = main_config->get_value("PruebasAcumuladasDepto_Hdr")->get_list_data();
	if (raw_table->get_rows() != *(int*)table_config[6].get_data()) {
		std::cout << "PruebasAcumuladasDepto.csv -> Table rows "
			<< raw_table->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config[6].get_data()
			<< std::endl;
		return -1;
	}

	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
		raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}

	set_proper_col_names(*dept_index, *raw_table);

	return 0;
}

int process_ca_depto(Table*& raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config = areas_config->get_value("CasosAcumuladosDepto")->get_list_data();
	raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
	std::vector<Variant> table_col_config = main_config->get_value("CasosAcumuladosDepto_Hdr")->get_list_data();
	if (raw_table->get_rows() != *(int*)table_config[6].get_data()) {
		std::cout << "CasosAcumuladosDepto.csv -> Table rows "
			<< raw_table->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
		raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	set_proper_col_names(*dept_index, *raw_table);
	
	return 0;
}

int process_cp_edades(Table*& raw_table, Config* main_config, Config* areas_config, Config* age_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config = areas_config->get_value("CasosPositivosEdades")->get_list_data();
	raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
	std::vector<Variant> table_col_config = main_config->get_value("CasosPositivosEdades_Hdr")->get_list_data();
	if (raw_table->get_rows() != *(int*)table_config[6].get_data()) {
		std::cout << "CasosPositivosEdades.csv -> Table rows "
			<< raw_table->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
		raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	set_proper_col_names(*age_index, *raw_table);

	return 0;
}

int process_ma_depto(Table*& raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config = areas_config->get_value("MuertesAcumuladasDepto")->get_list_data();
	raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
	std::vector<Variant> table_col_config = main_config->get_value("MuertesAcumuladasDepto_Hdr")->get_list_data();
	if (raw_table->get_rows() != *(int*)table_config[6].get_data()) {
		std::cout << "MuertesAcumuladasDepto.csv -> Table rows "
			<< raw_table->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
		raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	set_proper_col_names(*dept_index, *raw_table);

	return 0;
}

int process_ca_distr_20(Table*& raw_table_p1, Table*& raw_table_p2, Config* main_config, Config* areas_config, Config* dept_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config_p1 = areas_config->get_value("CasosAcumuDistrito2020P1")->get_list_data();
	std::vector<Variant> table_config_p2 = areas_config->get_value("CasosAcumuDistrito2020P2")->get_list_data();
	raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
	raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
	std::vector<Variant> table_col_config_p1 = main_config->get_value("CasosAcumuDistrito2020P1_Hdr")->get_list_data();
	std::vector<Variant> table_col_config_p2 = main_config->get_value("CasosAcumuDistrito2020P2_Hdr")->get_list_data();
	if (raw_table_p1->get_rows() != *(int*)table_config_p1[6].get_data()) {
		std::cout << "CasosAcumuDistrito2020P1.csv -> Table rows "
			<< raw_table_p1->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p1[6].get_data()
			<< std::endl;
		return -1;
	}
	if (raw_table_p2->get_rows() != *(int*)table_config_p2[6].get_data()) {
		std::cout << "CasosAcumuDistrito2020P2.csv -> Table rows "
			<< raw_table_p2->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p2[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config_p1.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
		raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	for (int i = 1; i < table_col_config_p2.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
		raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	// Join part 1 and part 2
	raw_table_p1->join_tables(*raw_table_p2);	

	return 0;
}

int process_ca_distr_21(Table*& raw_table_p1, Table*& raw_table_p2, Config* main_config, Config* areas_config, Config* dept_index){
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config_p1 = areas_config->get_value("CasosAcumuDistrito2021P1")->get_list_data();
	std::vector<Variant> table_config_p2 = areas_config->get_value("CasosAcumuDistrito2021P2")->get_list_data();
	raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
	raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
	std::vector<Variant> table_col_config_p1 = main_config->get_value("CasosAcumuDistrito2021P1_Hdr")->get_list_data();
	std::vector<Variant> table_col_config_p2 = main_config->get_value("CasosAcumuDistrito2021P2_Hdr")->get_list_data();
	if (raw_table_p1->get_rows() != *(int*)table_config_p1[6].get_data()) {
		std::cout << "CasosAcumuDistrito2021P1.csv -> Table rows "
			<< raw_table_p1->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p1[6].get_data()
			<< std::endl;
		return -1;
	}
	if (raw_table_p2->get_rows() != *(int*)table_config_p2[6].get_data()) {
		std::cout << "CasosAcumuDistrito2021P2.csv -> Table rows "
			<< raw_table_p2->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p2[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config_p1.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
		raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	for (int i = 1; i < table_col_config_p2.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
		raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	// Join part 1 and part 2
	raw_table_p1->join_tables(*raw_table_p2);

	return 0;
}

int process_ma_distr(Table*& raw_table_p1, Table*& raw_table_p2, Config* main_config, Config* areas_config, Config* dept_index) {
	std::string raw_tables_dir = *(std::string*)main_config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	std::vector<Variant> table_config_p1 = areas_config->get_value("MuertesAcumulaDistritoP1")->get_list_data();
	std::vector<Variant> table_config_p2 = areas_config->get_value("MuertesAcumulaDistritoP1")->get_list_data();
	raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
	raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
	std::vector<Variant> table_col_config_p1 = main_config->get_value("MuertesAcumulaDistritoP1_Hdr")->get_list_data();
	std::vector<Variant> table_col_config_p2 = main_config->get_value("MuertesAcumulaDistritoP1_Hdr")->get_list_data();
	if (raw_table_p1->get_rows() != *(int*)table_config_p1[6].get_data()) {
		std::cout << "MuertesAcumulaDistritoP1.csv -> Table rows "
			<< raw_table_p1->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p1[6].get_data()
			<< std::endl;
		return -1;
	}
	if (raw_table_p2->get_rows() != *(int*)table_config_p2[6].get_data()) {
		std::cout << "MuertesAcumulaDistritoP2.csv -> Table rows "
			<< raw_table_p2->get_rows()
			<< " do not match the expected number of rows "
			<< *(int*)table_config_p2[6].get_data()
			<< std::endl;
		return -1;
	}
	
	// Clean up incoming data and convert strings to numbers
	for (int i = 1; i < table_col_config_p1.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
		raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	for (int i = 1; i < table_col_config_p2.size(); i++) {
		std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
		raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
	}
	
	// Join part 1 and part 2
	raw_table_p1->join_tables(*raw_table_p2);
	
	return 0;
}