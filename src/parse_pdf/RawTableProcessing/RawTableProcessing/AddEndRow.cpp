#include "RawTableProcessing.hpp"

int append_end_pa_depto(Table*& input_raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	if (input_raw_table->get_rows() != dept_index->get_n_pairs()) {
		return -1;
	}
	std::string pa_depto_table_dir = *(std::string*)main_config->get_value("PADepto_Dir")->get_num_str_data().get_data() + "/";
	for (int i = 0; i < dept_index->get_n_pairs(); i++) {
		std::string table_path = pa_depto_table_dir + *(std::string*)input_raw_table->get_cell_data("Depto", i).get_data() + ".csv";
		Table* depto_table = new Table(table_path);
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = *(std::string*)areas_config->get_value("Date")->get_num_str_data().get_data();
		depto_table->append_end_row(input_row);
		//depto_table->save_as_csv(depto_table->get_filename());
		delete depto_table;
	}
	return 0;
}

int append_end_ca_depto(Table*& input_raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	if (input_raw_table->get_rows() != dept_index->get_n_pairs()) {
		return -1;
	}
	std::string ca_depto_table_dir = *(std::string*)main_config->get_value("CADepto_Dir")->get_num_str_data().get_data() + "/";
	for (int i = 0; i < dept_index->get_n_pairs(); i++) {
		std::string table_path = ca_depto_table_dir + *(std::string*)input_raw_table->get_cell_data("Depto", i).get_data() + ".csv";
		Table* depto_table = new Table(table_path);
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = *(std::string*)areas_config->get_value("Date")->get_num_str_data().get_data();
		depto_table->append_end_row(input_row);
		//depto_table->save_as_csv(depto_table->get_filename());
		delete depto_table;
	}
	return 0;
}

int append_end_cp_edades(Table*& input_raw_table, Config* main_config, Config* areas_config, Config* age_index) {
	std::string ca_edades_table_fn = *(std::string*)main_config->get_value("CAEdades_Dir")->get_num_str_data().get_data() + "/" + 
							      *(std::string*)main_config->get_value("CAEdades_Table")->get_num_str_data().get_data();
	Table* ages_table = new Table(ca_edades_table_fn);
	int num_entries = main_config->get_value("CAEdades_Hdr")->get_list_data().size();
	int curr_entry = 0;
	std::vector<Variant> input_row;
	input_row.resize(num_entries + 1);
	input_row[curr_entry++] = *(std::string*)areas_config->get_value("Date")->get_num_str_data().get_data();
	for (int i = 0; i < input_raw_table->get_rows(); i++) {
		std::vector<Variant> row = input_raw_table->get_row_data(i);
		for (int j = 1; j < row.size(); j++) {
			input_row[curr_entry++] = row[j];
		}
	}
	ages_table->append_end_row(input_row);
	//ages_table->save_as_csv(ages_table->get_filename());
	delete ages_table;
	return 0;
}

int append_end_ma_depto(Table*& input_raw_table, Config* main_config, Config* areas_config, Config* dept_index) {
	if (input_raw_table->get_rows() != dept_index->get_n_pairs()) {
		return -1;
	}
	std::string ma_depto_table_dir = *(std::string*)main_config->get_value("MADepto_Dir")->get_num_str_data().get_data() + "/";
	for (int i = 0; i < dept_index->get_n_pairs(); i++) {
		std::string table_path = ma_depto_table_dir + *(std::string*)input_raw_table->get_cell_data("Depto", i).get_data() + ".csv";
		Table* depto_table = new Table(table_path);
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = *(std::string*)areas_config->get_value("Date")->get_num_str_data().get_data();
		depto_table->append_end_row(input_row);
		//depto_table->save_as_csv(depto_table->get_filename());
		delete depto_table;
	}
	return 0;
}