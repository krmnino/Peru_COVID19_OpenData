#include "Value.hpp"

namespace cl {
Value::Value() {
	this->type = ValueType::UNDEF;
	this->single_data = 0;
}

Value::Value(const Value& src) {
	this->type = src.type;
	List list_ret_data;
	switch (this->type) {
	case ValueType::INT_NUM:
	case ValueType::DBL_NUM:
	case ValueType::STRING:
		this->single_data = src.single_data;
		break;
	case ValueType::LIST:
		break;
	case ValueType::UNDEF:
		this->single_data = 0;
		break;
	default:
		break;
	}
}

Value::~Value() {}

Value::Value(std::string& raw_value) {
	if (raw_value.at(0) == '[' && raw_value.at(raw_value.length() - 1) == ']') {
		this->type = ValueType::LIST;
		this->parse_list(raw_value);
	}
	else {
		switch (check_data_type(raw_value))
		{
		case 0:
			this->type = ValueType::STRING;
			this->single_data = raw_value;
			break;
		case 1:
			this->type = ValueType::INT_NUM;
			#ifdef LINUX
			this->single_data = std::atoi(raw_value.c_str());
			#else
			this->single_data = std::stoi(raw_value);
			#endif
			//this->single_data = std::stoi(raw_value);
			break;
		case 2:
			this->type = ValueType::DBL_NUM;
			#ifdef LINUX
			this->single_data = std::atof(raw_value.c_str());
			#else
			this->single_data = std::stod(raw_value);
			#endif
			//this->single_data = std::stod(raw_value);
			break;
		default:
			break;
		}
	}
}

Value::Value(int data) {
	this->type = ValueType::INT_NUM;
	this->single_data = data;
}

Value::Value(double data) {
	this->type = ValueType::DBL_NUM;
	this->single_data = data;
}

Value::Value(const char* data) {
	this->type = ValueType::STRING;
	this->single_data = std::string(data);
}

Value::Value(List data_list) {
	this->type = ValueType::LIST;
	this->list_data = data_list;
}

int Value::check_data_type(std::string& data) {
	std::string::const_iterator it = data.begin();
	bool integer_type = false;
	bool decimal_point = false;
	bool string_type = true;
	while (it != data.end()) {
		if (*it == '.' && !decimal_point) {
			// If decimal point appears for the first time, then it may be a double
			decimal_point = true;
			it++;
			continue;
		}
		else if (*it == '.' && decimal_point) {
			// Otherwise cannot be a double, it is a string
			return 0;
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

void Value::parse_list(std::string& raw_str) {
	// Remove front and trailing square brackets
	raw_str = raw_str.substr(1, raw_str.length());
	raw_str = raw_str.substr(0, raw_str.length() - 1);
	std::vector<std::string> split_raw_list;
	this->split_string(split_raw_list, raw_str, ',');
	this->list_data.resize(split_raw_list.size());
	for (unsigned int i = 0; i < split_raw_list.size(); i++) {
		split_raw_list[i].erase(std::remove(split_raw_list[i].begin(), split_raw_list[i].end(), '\t'), split_raw_list[i].end());
		this->remove_side_spaces(split_raw_list[i]);
		Variant list_elem;
		switch (check_data_type(split_raw_list[i])) {
		case 0:
			list_elem = split_raw_list[i];
			this->list_data[i] = list_elem;
			break;
		case 1:
			list_elem = std::stoi(split_raw_list[i]);
			this->list_data[i] = list_elem;
			break;
		case 2:
			list_elem = std::stod(split_raw_list[i]);
			this->list_data[i] = list_elem;
			break;
		default:
			break;
		}
	}
}

void Value::split_string(std::vector<std::string>& processed, std::string& buffer, char delimiter) {
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

void Value::remove_side_spaces(std::string& raw_str) {
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

bool Value::operator<(const Value& other) {
	Value tmp = other;
	switch (this->type) {
	case ValueType::INT_NUM:
	case ValueType::DBL_NUM:
		return this->single_data < other.single_data;
		break;
	case ValueType::STRING:
		return this->single_data.get_data<std::string>() < tmp.single_data.get_data<std::string>();
		break;
	case ValueType::LIST:
		return this->list_data.size() < other.list_data.size();
		break;
	case ValueType::UNDEF:
	default:
		break;
	}
	return false;
}

ValueType Value::get_type() {
	return this->type;
}
}
