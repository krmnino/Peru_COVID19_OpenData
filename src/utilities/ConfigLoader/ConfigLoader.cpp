#include "ConfigLoader.hpp"

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
		buffer += line;
	}
	buffer.erase(std::remove(buffer.begin(), buffer.end(), '\t'), buffer.end());
	std::vector<std::string> raw_entries;
	split_string(raw_entries, buffer, ';');
	std::vector<std::string> raw_keyvals;
	for (unsigned int i = 0; i < raw_entries.size(); i++) {
		split_string(raw_keyvals, raw_entries[i], '=');
		remove_side_spaces(raw_keyvals[0]);
		remove_side_spaces(raw_keyvals[1]);
		Value* new_val = new Value(raw_keyvals[1]);
		this->keys_index.insert(std::make_pair(raw_keyvals[0], i));
		this->values.push_back(new_val);
		raw_keyvals.clear();
		n_pairs++;
	}
}

Config::Config() {
	this->n_pairs = 0;
}

Config::~Config() {
	for (size_t i = 0; i < this->values.size(); i++) {
		delete values[i];
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

int Config::get_n_pairs() {
	return this->n_pairs;
}

std::vector<std::string> Config::get_keys() {
	std::vector<std::string> ret;
	ret.resize(this->n_pairs);
	for (std::map<std::string, int>::iterator it = this->keys_index.begin(); it != this->keys_index.end(); it++) {
		ret.push_back(it->first);
	}
	return ret;
}

Value* Config::get_value(std::string key) {
	std::map<std::string, int>::const_iterator it = this->keys_index.find(key);
	return (it == this->keys_index.end()) ? nullptr : this->values[it->second];
}

