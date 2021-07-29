#ifndef TABLE
#define TABLE

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>

#include "Variant.hpp"

class Table {
private:
	int rows;
	int columns;
	char delimiter;
	std::string filename;
	std::vector<std::string> header_index;
	std::map<std::string, std::vector<Variant>> contents;

	void process_raw_row(std::vector<std::string>&, std::string&, char);
	int check_data_type(std::string&);
public:
	Table(std::string, char delim = ',');
	Table();
	~Table();
	int get_rows();
	int get_columns();
	std::vector<std::string> get_fields();
	std::vector<Variant> get_column_data(std::string);
	std::vector<Variant> get_row_data(int);
	std::vector<Variant> get_end_row();
	Variant get_cell_data(std::string, int);
	void set_filename(std::string);
	void set_delimiter(char);
	void append_begin_row(std::vector<Variant>);
	void append_end_row(std::vector<Variant>);
	void update_cell_data(std::string, int, Variant);
	void update_cell_data(int, int, Variant);
	void save_as_csv(std::string);
	void compute_new_column(std::string, std::vector<std::string>&, Variant (*)(int, std::vector<std::vector<Variant>>&));
	void compute_new_column(std::string, std::vector<int>&, Variant(*)(int, std::vector<std::vector<Variant>>&));
	void compute_update_column(std::string, std::vector<std::string>&, Variant(*)(int, std::vector<std::vector<Variant>>&));
	void compute_update_column(int, std::vector<std::string>&, Variant(*)(int, std::vector<std::vector<Variant>>&));
	void compute_update_column(std::string, std::vector<int>&, Variant(*)(int, std::vector<std::vector<Variant>>&));
	void compute_update_column(int, std::vector<int>&, Variant(*)(int, std::vector<std::vector<Variant>>&));
};

#endif // TABLE