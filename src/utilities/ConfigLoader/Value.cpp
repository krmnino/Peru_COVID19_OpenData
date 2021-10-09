#include "Value.hpp"

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
			this->num_str_data = raw_value;
			break;
		case 1:
			this->type = ValueType::NUMBER;
			this->num_str_data = std::stoi(raw_value);
			break;
		case 2:
			this->type = ValueType::NUMBER;
			this->num_str_data = std::stod(raw_value);
			break;
		default:
			break;
		}
	}
}

Value::Value() {
	this->type = ValueType::UNDEF;
	this->num_str_data = 0;
}

Value::Value(const Value& src) {
	this->type = src.type;
	std::vector<Variant> list_ret_data;
	switch (this->type) {
	case ValueType::NUMBER:
	case ValueType::STRING:
		this->num_str_data = src.num_str_data;
		break;
	case ValueType::LIST:
		break;
	case ValueType::UNDEF:
		this->num_str_data = 0;
		break;
	default:
		break;
	}
}

Value::~Value() {}

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
		else if (*it == '.' && decimal_point){
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
	raw_str = raw_str.substr(0, raw_str.length()-1);
	std::vector<std::string> split_raw_list;
	std::vector<Variant> variant_list;
	this->split_string(split_raw_list, raw_str, ',');
	for (unsigned int i = 0; i < split_raw_list.size(); i++) {
		split_raw_list[i].erase(std::remove(split_raw_list[i].begin(), split_raw_list[i].end(), '\t'), split_raw_list[i].end());
		this->remove_side_spaces(split_raw_list[i]);
		Variant list_elem;
		switch (check_data_type(split_raw_list[i])) {
		case 0:
			list_elem = split_raw_list[i];
			variant_list.push_back(list_elem);
			break;
		case 1:
			list_elem = std::stoi(split_raw_list[i]);
			variant_list.push_back(list_elem);
			break;
		case 2:
			list_elem = std::stod(split_raw_list[i]);
			variant_list.push_back(list_elem);
			break;
		default:
			break;
		}
	}
	this->list_data = variant_list;
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
	case ValueType::NUMBER:
		return this->num_str_data < other.num_str_data;
		break;
	case ValueType::STRING:
		return *(std::string*)this->num_str_data.get_data() < *(std::string*)tmp.num_str_data.get_data();
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

Variant Value::get_num_str_data() {
	Variant ret;
	if (this->type == ValueType::LIST) {
		return ret;
	}
	return this->num_str_data;
}

std::vector<Variant> Value::get_list_data() {
	std::vector<Variant> ret;
	if (this->type != ValueType::LIST) {
		return ret;
	}
	return this->list_data;
}

ValueType Value::get_type() {
	return this->type;
}