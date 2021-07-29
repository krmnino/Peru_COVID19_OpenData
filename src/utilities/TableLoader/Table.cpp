
#include "Table.hpp"

Table::Table(std::string filename, char delim) {
	this->rows = 0;
	this->columns = 0;
	this->delimiter = delim;

	std::vector<std::string> buffer;
	std::string line;
	std::ifstream file;
	file.open(filename);
	while (std::getline(file, line)) {
		buffer.push_back(line);
	}

	std::vector<std::vector<std::string>> raw_table;
	for (unsigned int i = 0; i < buffer.size(); i++) {
		std::vector<std::string> temp;
		this->process_raw_row(temp, buffer[i], delimiter);
		raw_table.push_back(temp);
		this->rows++;
	}
	this->rows--;

	for (unsigned int i = 0; i < raw_table[0].size(); i++){
		// Allocate empty vector of Variant types
		std::vector<Variant> vect;
		// Populate header index with pair index number and field name
		this->header_index.push_back(raw_table[0][i]);
		// Populate contents map with pair field name and empty vector
		this->contents.insert(std::make_pair(raw_table[0][i], vect));
		this->columns++;
	}

	for (unsigned int i = 0; i < this->columns; i++) {
		for (unsigned int j = 1; j < raw_table.size(); j++) {
			// Check if data is string, double, or integer
			auto tmp = raw_table[j][i];
			switch (this->check_data_type(raw_table[j][i])) {
			case 0:
				this->contents[this->header_index[i]].push_back(raw_table[j][i]);
				break;
			case 1:
				this->contents[this->header_index[i]].push_back(std::stoi(raw_table[j][i]));
				break;
			case 2:
				this->contents[this->header_index[i]].push_back(std::stod(raw_table[j][i]));
				break;
			default:
				break;
			}
		}
	}
}

Table::~Table() {}

void Table::process_raw_row(std::vector<std::string>& processed, std::string& row, char delimiter) {
	int base = 0;
	for (unsigned int i = 0; i < row.length(); i++) {
		if (row.at(i) == delimiter) {
			processed.push_back(row.substr(base, i - base));
			base = i + 1;
		}
		else if (i == row.length() - 1) {
			processed.push_back(row.substr(base, i + 1 - base));
			base = i + 1;
		}
	}
}

/*
Return - Meaning
0	   - String
1      - Integer
2      - Double
*/
int Table::check_data_type(std::string& data) {
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
		if (0 > *it || *it > 255) {
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

int Table::get_rows() {
	return this->rows;
}

int Table::get_columns() {
	return this->columns;
}

std::vector<std::string> Table::get_fields() {
	return this->header_index;
}

std::vector<Variant> Table::get_column_data(std::string field_name) {
	return this->contents[field_name];
}

std::vector<Variant> Table::get_row_data(int row_n) {
	std::vector<Variant> out;
	if (0 > row_n || row_n >= this->rows) {
		return out;
	}
	for (int i = 0; i < this->columns; i++) {
		out.push_back(this->contents[this->header_index[i]][row_n]);
	}
	return out;
}

std::vector<Variant> Table::get_end_row() {
	std::vector<Variant> out;
	if (this->rows == 0) {
		return out;
	}
	for (int i = 0; i < this->columns; i++) {
		out.push_back(this->contents[this->header_index[i]][this->rows-1]);
	}
	return out;
}

Variant Table::get_cell_data(std::string field, int row) {
	Variant out;
	if (0 > row || row >= this->rows) {
		return out;
	}
	auto ret = this->contents[field];
	if (ret.size() == 0) {
		return out;
	}
	return this->contents[field][row];
}

void Table::set_filename(std::string fn) {
	this->filename = fn;
}

void Table::set_delimiter(char new_delim) {
	this->delimiter = new_delim;
}

void Table::append_begin_row(std::vector<Variant> data) {
	if (data.size() != this->columns) {
		return;
	}
	for (int i = 0; i < this->columns; i++) {
		this->contents[this->header_index[i]].insert(this->contents[this->header_index[i]].begin(), data[i]);
	}
	this->rows++;
}

void Table::append_end_row(std::vector<Variant> data) {
	if (data.size() != this->columns) {
		return;
	}
	for (int i = 0; i < this->columns; i++) {
		this->contents[this->header_index[i]].push_back(data[i]);
	}
	this->rows++;
}

void Table::update_cell_data(std::string field, int row, Variant data) {
	if (0 > row || row >= this->rows) {
		return;
	}
	auto ret = this->contents[field];
	if (ret.size() == 0) {
		return;
	}
	this->contents[field][row] = data;
}

void Table::update_cell_data(int col, int row, Variant data) {
	if (0 > col || col >= this->columns) {
		return;
	}
	if (0 > row || row >= this->rows) {
		return;
	}
	this->contents[this->header_index[col]][row] = data;
}

void Table::save_as_csv(std::string path) {
	std::ofstream out(path);
	for (int i = 0; i < this->columns; i++) {
		out << this->header_index[i];
		if (i != this->columns - 1) {
			out << std::string(1, this->delimiter);
		}
		else {
			out << "\n";
		}
	}
	for (unsigned int i = 0; i < this->rows; i++) {
		for (unsigned int j = 0; j < this->columns; j++) {
			out << this->contents[this->header_index[j]][i];
			if (j != this->columns - 1) {
				out << std::string(1, this->delimiter);
			}
			else {
				out << "\n";
			}
		}
	}
	out.close();
}

void Table::compute_new_column(std::string new_col_name, std::vector<std::string>& table_col_names, Variant (*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_names.size(); i++) {
		table_columns.push_back(this->contents[table_col_names[i]]);
	}
	this->header_index.push_back(new_col_name);
	this->contents.insert(std::make_pair(new_col_name, std::vector<Variant>(this->rows)));
	this->columns++;
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[new_col_name][i] = fn(i, table_columns);
	}
}

void Table::compute_new_column(std::string new_col_name, std::vector<int>& table_col_idxs, Variant(*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_idxs.size(); i++) {
		table_columns.push_back(this->contents[this->header_index[table_col_idxs[i]]]);
	}
	this->header_index.push_back(new_col_name);
	this->contents.insert(std::make_pair(new_col_name, std::vector<Variant>(this->rows)));
	this->columns++;
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[new_col_name][i] = fn(i, table_columns);
	}
}

void Table::compute_update_column(std::string col_name, std::vector<std::string>& table_col_names, Variant(*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_names.size(); i++) {
		table_columns.push_back(this->contents[table_col_names[i]]);
	}
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[col_name][i] = fn(i, table_columns);
	}
}

void Table::compute_update_column(int col_idx, std::vector<std::string>& table_col_names, Variant(*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_names.size(); i++) {
		table_columns.push_back(this->contents[table_col_names[i]]);
	}
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[this->header_index[col_idx]][i] = fn(i, table_columns);
	}
}

void Table::compute_update_column(std::string col_name, std::vector<int>& table_col_idxs, Variant(*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_idxs.size(); i++) {
		table_columns.push_back(this->contents[this->header_index[table_col_idxs[i]]]);
	}
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[col_name][i] = fn(i, table_columns);
	}
}

void Table::compute_update_column(int col_idx, std::vector<int>& table_col_idxs, Variant(*fn)(int, std::vector<std::vector<Variant>>&)) {
	std::vector<std::vector<Variant>> table_columns;
	for (unsigned int i = 0; i < table_col_idxs.size(); i++) {
		table_columns.push_back(this->contents[this->header_index[table_col_idxs[i]]]);
	}
	for (unsigned int i = 0; i < this->rows; i++) {
		this->contents[this->header_index[col_idx]][i] = fn(i, table_columns);
	}
}