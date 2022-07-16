#include "RawTableProcessing.hpp"

int append_end_pa_depto(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* dept_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("PADepto_Dir")->get_data<std::string>();
	for (int i = 0; i < dept_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Depto", i).get_data<std::string>() + ".csv";
		tl::Table* processed_table = new tl::Table(table_path);

		// Set processed table instance filename field
		processed_table->set_filename(table_path);

		// Extract row from raw table 
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		processed_table->append_end_row(input_row);
		processed_table->save_as_csv(processed_table->get_filename());
		delete processed_table;
	}
	return 0;
}

int append_end_ca_depto(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* dept_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("CADepto_Dir")->get_data<std::string>();
	for (int i = 0; i < dept_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Depto", i).get_data<std::string>() + ".csv";
		tl::Table* processed_table = new tl::Table(table_path);
		
		// Set processed table instance filename field
		processed_table->set_filename(table_path);

		// Extract row from raw table 
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		processed_table->append_end_row(input_row);
		processed_table->save_as_csv(processed_table->get_filename());
		delete processed_table;
	}
	return 0;
}

int append_end_cp_edades(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* age_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	// Open processed table
	std::string table_path = top_level_path + main_config->get_value("CPEdades_PTF")->get_data<std::string>();
	tl::Table* ages_table = new tl::Table(table_path);

	// Set processed table instance filename field
	ages_table->set_filename(table_path);

	// Extract number of columns in processed column
	int input_row_index = 0;
	size_t num_entries = main_config->get_value("CPEdades_PTHdr")->get_data<cl::List>().size();
	std::vector<Variant> input_row;
	input_row.resize(num_entries);
	input_row[input_row_index++] = date;

	// For each row in raw table
	for (int i = 0; i < input_raw_table->get_rows(); i++) {
		std::vector<Variant> row = input_raw_table->get_row_data(i);
		// Extract entry in row and add it to input_row
		for (int j = 1; j < row.size(); j++) {
			input_row[input_row_index++] = row[j];
		}
	}

	// Save processed table
	ages_table->append_end_row(input_row);
	ages_table->save_as_csv(ages_table->get_filename());
	delete ages_table;
	return 0;
}

int append_end_ma_depto(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* dept_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("MADepto_Dir")->get_data<std::string>();
	for (int i = 0; i < dept_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Depto", i).get_data<std::string>() + ".csv";
		tl::Table* processed_table = new tl::Table(table_path);

		// Set processed table instance filename field
		processed_table->set_filename(table_path);

		// Extract row from raw table
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		processed_table->append_end_row(input_row);
		processed_table->save_as_csv(processed_table->get_filename());
		delete processed_table;
	}
	return 0;
}

int append_end_ma_deptosm(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* dept_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("MADeptoSM_Dir")->get_data<std::string>();
	for (int i = 0; i < dept_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Depto", i).get_data<std::string>() + ".csv";
		tl::Table* processed_table = new tl::Table(table_path);

		// Set processed table instance filename field
		processed_table->set_filename(table_path);

		// Extract row from raw table 
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		processed_table->append_end_row(input_row);
		processed_table->save_as_csv(processed_table->get_filename());
		delete processed_table;
	}
	return 0;
}

int append_end_ca_distr_20(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* distr_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("CADistr20_Dir")->get_data<std::string>();
	for (int i = 0; i < distr_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Distrito", i).get_data<std::string>() + ".csv";
		tl::Table* processed_table = new tl::Table(table_path);

		// Set processed table instance filename field
		processed_table->set_filename(table_path);

		// Extract row from raw table
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		processed_table->append_end_row(input_row);
		processed_table->save_as_csv(processed_table->get_filename());
		delete processed_table;
	}
	return 0;
}

int append_end_ca_distr_21(tl::Table*& input_raw_table, cl::Config* main_config, std::string date, cl::Config* distr_index) {
	// Extract top level directory path
	#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
	#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
	#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("CADistr21_Dir")->get_data<std::string>() + "/";
	for (int i = 0; i < distr_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Distrito", i).get_data<std::string>() + ".csv";
		tl::Table* distr_table = new tl::Table(table_path);

		// Set processed table instance filename field
		distr_table->set_filename(table_path);

		// Extract row from raw table
		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = date;

		// Save processed table
		distr_table->append_end_row(input_row);
		distr_table->save_as_csv(distr_table->get_filename());
		delete distr_table;
	}
	return 0;
}

int append_end_ma_distr(tl::Table*& input_raw_table, cl::Config* main_config, cl::Config* areas_config, cl::Config* distr_index) {
	// Extract top level directory path
#ifdef LINUX
	std::string top_level_path = main_config->get_value("LinuxTopLevel")->get_data<std::string>();
#else
	std::string top_level_path = main_config->get_value("WindowsTopLevel")->get_data<std::string>();
#endif // LINUX

	std::string processed_dir = top_level_path + main_config->get_value("MADistr_Dir")->get_data<std::string>() + "/";
	for (int i = 0; i < distr_index->get_n_entries(); i++) {
		// Open processed table
		std::string table_path = processed_dir + input_raw_table->get_cell_data("Distrito", i).get_data<std::string>() + ".csv";
		tl::Table* distr_table = new tl::Table(table_path);

		// Set processed table instance filename field
		distr_table->set_filename(table_path);

		std::vector<Variant> input_row = input_raw_table->get_row_data(i);
		input_row[0] = areas_config->get_value("Date")->get_data<std::string>();

		// Extract row from raw table
		distr_table->append_end_row(input_row);
		distr_table->save_as_csv(distr_table->get_filename());
		delete distr_table;
	}
	return 0;
}