#ifndef PAIR
#define PAIR

#include "../DataVariant/Variant.hpp"
#include <string>
#include <vector>
#include <algorithm>

enum class ValueType {UNDEF, NUMBER, STRING, LIST, DICT};

class Value {
private:
	ValueType type;
	union {
		Variant num_str_data;
		std::vector<Variant> list_data;
	};
	void parse_list(std::string&);
	void split_string(std::vector<std::string>&, std::string&, char);
	void remove_side_spaces(std::string&);

public:
	int check_data_type(std::string&);
	Value(std::string&);
	Value();
	Value(const Value&);
	~Value();
	bool operator< (const Value&);
	Variant get_num_str_data();
	std::vector<Variant> get_list_data();
	ValueType get_type();
	
};

#endif // !PAIR

