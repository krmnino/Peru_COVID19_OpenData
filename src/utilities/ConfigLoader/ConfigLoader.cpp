#include "ConfigLoader.hpp"

namespace cl {
Config::Config(std::string filename) {
	this->n_pairs = 0;
	std::string buffer;
	std::string line;
	std::ifstream file;
	file.open(filename);
	while (std::getline(file, line)) {
		if (line.length() == 0) {
			continue;
		}
		if (line.at(0) == '#') {
			continue;
		}
		if (line.at(line.size() - 1) != ';') {
			CL_Error ex(CLErrorCode::SEMICOLON);
			std::cerr << ex.what() << std::endl;
			throw ex;

		}
		buffer += line;
	}
	buffer.erase(std::remove(buffer.begin(), buffer.end(), '\t'), buffer.end());
	std::vector<std::string> raw_entries;
	split_string(raw_entries, buffer, ';');
	std::vector<std::string> raw_keyvals;
	int entry_idx = 0;
	for (unsigned int i = 0; i < raw_entries.size(); i++) {
		if (raw_entries[i].length() == 0) {
			continue;
		}
		split_string(raw_keyvals, raw_entries[i], '=');
		if (raw_keyvals.size() != 2) {
			CL_Error ex(CLErrorCode::EQUALS_SIGN);
			std::cerr << ex.what() << std::endl;
			throw ex;
		}
		remove_side_spaces(raw_keyvals[0]);
		remove_side_spaces(raw_keyvals[1]);
		Value* new_val = new Value(raw_keyvals[1]);

		// Search if key exists in dictionary
		std::map<std::string, int>::const_iterator it = this->keys_index.find(raw_keyvals[0]);
		if (it == this->keys_index.end()) {
			this->keys_index.insert(std::make_pair(raw_keyvals[0], entry_idx));
			this->values.push_back(new_val);
			entry_idx++;
			this->n_pairs++;
		}
		else {
			int idx = it->second;
			delete this->values[idx];
			this->values[idx] = new_val;
		}
		raw_keyvals.clear();
	}
}

Config::Config() {
	this->n_pairs = 0;
}

Config::~Config() {
	for (size_t i = 0; i < this->values.size(); i++) {
		delete this->values[i];
	}
}

void Config::split_string(std::vector<std::string>& processed, std::string& buffer, char delimiter) {
	int base = 0;
	std::string split;
	for (unsigned int i = 0; i < buffer.length(); i++) {
		if (buffer.at(i) == delimiter) {
			split = buffer.substr(base, i - base);
			if (split.length() != 0) {
				processed.push_back(split);
			}
			base = i + 1;
		}
		else if (i == buffer.length() - 1) {
			split = buffer.substr(base, i + 1 - base);
			if (split.length() != 0) {
				processed.push_back(split);
			}
			base = i + 1;
		}
	}
}

void Config::remove_side_spaces(std::string& raw_str) {
	size_t left_idx = 0;
	size_t right_idx = 0;
	for (unsigned int i = 0; i < raw_str.length(); i++) {
		if (raw_str.at(i) != ' ') {
			left_idx = i;
			break;
		}
	}
	raw_str = raw_str.substr(left_idx, raw_str.length());
	for (long long i = raw_str.length() - 1; i >= 0; i--) {
		if (raw_str.at(i) != ' ') {
			(i == raw_str.length() - 1) ? right_idx = raw_str.length() : right_idx = i + 1;
			break;
		}
	}
	raw_str = raw_str.substr(0, right_idx);
}

int Config::get_n_entries() {
	return this->n_pairs;
}

std::vector<std::string> Config::get_all_keys() {
	std::vector<std::string> ret;
	ret.resize(this->n_pairs);
	for (std::map<std::string, int>::iterator it = this->keys_index.begin(); it != this->keys_index.end(); it++) {
		ret[it->second] = it->first;
	}
	return ret;
}

Value* Config::get_value(std::string key) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	return this->values[it->second];
}

std::vector<std::pair<std::string, Value*>> Config::get_all_key_values() {
	std::vector<std::pair<std::string, Value*>> ret;
	ret.resize(this->n_pairs);
	for (std::map<std::string, int>::iterator it = this->keys_index.begin(); it != this->keys_index.end(); it++) {
		ret[it->second] = std::make_pair(it->first, this->get_value(it->first));
	}
	return ret;
}

void Config::add_entry(std::string key, int value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it != this->keys_index.end()) {
		CL_Error ex(CLErrorCode::ADD_KEY_REPEAT);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	this->keys_index.insert(std::make_pair(key, this->n_pairs));
	this->values.push_back(new_val);
	this->n_pairs++;
}

void Config::add_entry(std::string key, double value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it != this->keys_index.end()) {
		CL_Error ex(CLErrorCode::ADD_KEY_REPEAT);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	this->keys_index.insert(std::make_pair(key, this->n_pairs));
	this->values.push_back(new_val);
	this->n_pairs++;
}

void Config::add_entry(std::string key, std::string value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it != this->keys_index.end()) {
		CL_Error ex(CLErrorCode::ADD_KEY_REPEAT);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	this->keys_index.insert(std::make_pair(key, this->n_pairs));
	this->values.push_back(new_val);
	this->n_pairs++;
}

void Config::add_entry(std::string key, const char* value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it != this->keys_index.end()) {
		CL_Error ex(CLErrorCode::ADD_KEY_REPEAT);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	this->keys_index.insert(std::make_pair(key, this->n_pairs));
	this->values.push_back(new_val);
	this->n_pairs++;
}

void Config::add_entry(std::string key, List value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it != this->keys_index.end()) {
		CL_Error ex(CLErrorCode::ADD_KEY_REPEAT);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	this->keys_index.insert(std::make_pair(key, this->n_pairs));
	this->values.push_back(new_val);
	this->n_pairs++;
}

void Config::edit_value(std::string key, int value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	int idx = it->second;
	delete this->values[idx];
	this->values[idx] = new_val;
}

void Config::edit_value(std::string key, double value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	int idx = it->second;
	delete this->values[idx];
	this->values[idx] = new_val;
}

void Config::edit_value(std::string key, std::string value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	int idx = it->second;
	delete this->values[idx];
	this->values[idx] = new_val;
}

void Config::edit_value(std::string key, const char* value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	int idx = it->second;
	delete this->values[idx];
	this->values[idx] = new_val;
}

void Config::edit_value(std::string key, List value) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	if (it == this->keys_index.end()) {
		CL_Error ex(CLErrorCode::KEY_NOT_FOUND);
		std::cerr << ex.what() << std::endl;
		throw ex;
	}
	Value* new_val = new Value(value);
	int idx = it->second;
	delete this->values[idx];
	this->values[idx] = new_val;
}
}
