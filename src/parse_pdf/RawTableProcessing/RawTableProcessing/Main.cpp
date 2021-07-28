#include "../../../utilities/TableLoader/Table.hpp"
#include "../../../utilities/TableLoader/Variant.hpp"
#include <iostream>

int main() {
	std::string table_path = "../res/raw_tables/PruebasAcumuladasDepto.csv";
	Table* casos_totales = new Table(table_path);
	std::cout << casos_totales->get_columns() << std::endl;
	return 0;
}