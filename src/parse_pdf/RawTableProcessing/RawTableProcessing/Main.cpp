#include "../../../utilities/TableLoader/Table.hpp"
#include "../../../utilities/TableLoader/Variant.hpp"
#include <iostream>

int main() {
	std::string tables_abs_path = "C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables/";
	std::string areas_filename = "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFAreas.csv";
	Table* areas_table = new Table(areas_filename);
	std::vector<Variant> table_names = areas_table->get_column_data("name");
	
	for (int i = 0; i < areas_table->get_rows(); i++) {
		std::string table_full_path = tables_abs_path + *(std::string*)table_names[i].get_data() + ".csv";
		std::cout << table_full_path << std::endl;
		Table* raw_table = new Table(table_full_path, ';');
		delete raw_table;
	}

	return 0;
}