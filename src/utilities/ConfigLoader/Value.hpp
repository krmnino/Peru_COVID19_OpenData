#ifndef VALUE
#define VALUE

#include "../DataVariant/Variant.hpp"
#include <string>
#include <vector>
#include <algorithm>

namespace cl {
typedef std::vector<Variant> List;

enum class ValueType {UNDEF, INT_NUM, DBL_NUM, STRING, LIST};

class Value {
private:
	List list_data;
	Variant single_data;
	ValueType type;

	void parse_list(std::string&);
	void split_string(std::vector<std::string>&, std::string&, char);
	void remove_side_spaces(std::string&);
	int check_data_type(std::string&);

public:
	Value();
	Value(const Value&);
	~Value();
	Value(std::string&);
	Value(int);
	Value(double);
	Value(const char*);
	Value(List);
	bool operator< (const Value&);
	ValueType get_type();

	template<typename T>
	T get_data() {
		if constexpr (std::is_integral<T>::value) {
			if (this->type == ValueType::INT_NUM) {
				return this->single_data.get_data<int>();
			}
			else {
				return { 0 };
			}
		}
		else if constexpr (std::is_floating_point<T>::value) {
			if (this->type == ValueType::DBL_NUM) {
				return this->single_data.get_data<double>();
			}
			else {
				return { 0 };
			}
		}
		else if constexpr (std::is_base_of<std::string, T>::value) {
			if (this->type == ValueType::STRING) {
				return this->single_data.get_data<std::string>();
			}
			else {
				return { 0 };
			}
		}
		else if constexpr (std::is_object<T>::value) {
			if (this->type == ValueType::LIST) {
				return this->list_data;
			}
			else {
				return { 0 };
			}
		}
		else {
			return { 0 };
		}
	}
};
}

#endif // !VALUE
