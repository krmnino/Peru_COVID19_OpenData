#include "../../../utilities/TableLoader/Table.hpp"
#include "../../../utilities/DataVariant/Variant.hpp"
#include "../../../utilities/ConfigLoader/ConfigLoader.hpp"
#include <iostream>
#include <algorithm>

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
	if (col[0][idx].get_type() == STRING) {
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
	return out;
}

int main() {
	Config* config = new Config("../../ParsePDFConfig.cl");
	std::string parse_pdf_dir = *(std::string*)config->get_value("ParsePDFDir")->get_num_str_data().get_data() + "/";
	std::string raw_tables_dir = *(std::string*)config->get_value("RawTablesDir")->get_num_str_data().get_data() + "/";
	Config* areas_config = new Config(parse_pdf_dir + *(std::string*)config->get_value("PDFAreasCL")->get_num_str_data().get_data());
	int n_tables = areas_config->get_n_pairs();

	
	// Process PruebasAcumuladasDepto.csv
	{
		std::vector<Variant> table_config = areas_config->get_value("PruebasAcumuladasDepto")->get_list_data();
		Table* raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
		std::vector<Variant> table_col_config = config->get_value("PruebasAcumuladasDepto_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
			raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}


		delete raw_table;
	}

	// Process CasosAcumuladosDepto.csv
	{
		std::vector<Variant> table_config = areas_config->get_value("CasosAcumuladosDepto")->get_list_data();
		Table* raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
		std::vector<Variant> table_col_config = config->get_value("CasosAcumuladosDepto_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
			raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}

		delete raw_table;
	}

	// Process CasosPositivosEdades.csv
	{
		std::vector<Variant> table_config = areas_config->get_value("CasosPositivosEdades")->get_list_data();
		Table* raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
		std::vector<Variant> table_col_config = config->get_value("CasosPositivosEdades_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
			raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}
		delete raw_table;
	}

	// Process MuertesAcumuladasDepto.csv
	{
		std::vector<Variant> table_config = areas_config->get_value("MuertesAcumuladasDepto")->get_list_data();
		Table* raw_table = new Table(raw_tables_dir + *(std::string*)table_config[5].get_data(), ';');
		std::vector<Variant> table_col_config = config->get_value("MuertesAcumuladasDepto_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config[i].get_data() };
			raw_table->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}
		delete raw_table;
	}

	// Process CasosAcumuDistrito2020P1.csv
	// Process CasosAcumuDistrito2020P2.csv

	{
		std::vector<Variant> table_config_p1 = areas_config->get_value("CasosAcumuDistrito2020P1")->get_list_data();
		std::vector<Variant> table_config_p2 = areas_config->get_value("CasosAcumuDistrito2020P2")->get_list_data();
		Table* raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
		Table* raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
		std::vector<Variant> table_col_config_p1 = config->get_value("CasosAcumuDistrito2020P1_Hdr")->get_list_data();
		std::vector<Variant> table_col_config_p2 = config->get_value("CasosAcumuDistrito2020P2_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config_p1.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
			raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}
		for (int i = 1; i < table_col_config_p2.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
			raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}

		delete raw_table_p1;
		delete raw_table_p2;
	}

	// Process CasosAcumuDistrito2021P1.csv
	// Process CasosAcumuDistrito2021P2.csv
	{
		std::vector<Variant> table_config_p1 = areas_config->get_value("CasosAcumuDistrito2021P1")->get_list_data();
		std::vector<Variant> table_config_p2 = areas_config->get_value("CasosAcumuDistrito2021P2")->get_list_data();
		Table* raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
		Table* raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
		std::vector<Variant> table_col_config_p1 = config->get_value("CasosAcumuDistrito2021P1_Hdr")->get_list_data();
		std::vector<Variant> table_col_config_p2 = config->get_value("CasosAcumuDistrito2021P2_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config_p1.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
			raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}
		for (int i = 1; i < table_col_config_p2.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
			raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}

		delete raw_table_p1;
		delete raw_table_p2;
	}

	// Process MuertesAcumulaDistritoP1.csv
	// Process MuertesAcumulaDistritoP2.csv

	{
		std::vector<Variant> table_config_p1 = areas_config->get_value("MuertesAcumulaDistritoP1")->get_list_data();
		std::vector<Variant> table_config_p2 = areas_config->get_value("MuertesAcumulaDistritoP1")->get_list_data();
		Table* raw_table_p1 = new Table(raw_tables_dir + *(std::string*)table_config_p1[5].get_data(), ';');
		Table* raw_table_p2 = new Table(raw_tables_dir + *(std::string*)table_config_p2[5].get_data(), ';');
		std::vector<Variant> table_col_config_p1 = config->get_value("MuertesAcumulaDistritoP1_Hdr")->get_list_data();
		std::vector<Variant> table_col_config_p2 = config->get_value("MuertesAcumulaDistritoP1_Hdr")->get_list_data();
		// Clean up incoming data and convert strings to numbers
		for (int i = 1; i < table_col_config_p1.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p1[i].get_data() };
			raw_table_p1->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}
		for (int i = 1; i < table_col_config_p2.size(); i++) {
			std::vector<std::string> table_col_str = { *(std::string*)table_col_config_p2[i].get_data() };
			raw_table_p2->compute_update_column(table_col_str[0], table_col_str, convert_to_number);
		}

		delete raw_table_p1;
		delete raw_table_p2;
	}

	return 0;
}