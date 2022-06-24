#ifndef VARIANT
#define VARIANT

#include <string>
#include <iostream>
#include <sstream>

#ifdef LINUX
typedef long INT;
#else
typedef long long INT;
#endif

enum class DataType { INTEGER, DOUBLE, STRING, BOOLEAN, CHARACTER, UNDEFINED };

class Variant {
private:
	DataType type;
	union {
		INT int_data;
		double double_data;
		std::string* string_data;
		bool bool_data;
		char char_data;
	};
public:
	Variant();
	Variant(const Variant&);
	Variant(int);
	Variant(INT);
	Variant(double);
	Variant(std::string);
	Variant(const char*);
	Variant(bool);
	Variant(char);
	~Variant();

	DataType get_type();

	template<typename T>
	T get_data() {
		if constexpr (std::is_integral<T>::value) {
			switch (this->type) {
			case DataType::INTEGER:
				return this->int_data;
			case DataType::CHARACTER:
				return this->char_data;
			case DataType::BOOLEAN:
				return this->bool_data;
			default:
				return { 0 };
			}
		}
		else if constexpr (std::is_floating_point<T>::value) {
			if (this->type == DataType::DOUBLE) {
				return this->double_data;
			}
			else {
				return { 0 };
			}
		}
		else if constexpr (std::is_base_of<std::string, T>::value) {
			if (this->type == DataType::STRING) {
				return *(std::string*)this->string_data;
			}
			else {
				return { 0 };
			}
		}
		else {
			return { 0 };
		}
	}

	Variant& operator= (int);
	Variant& operator= (INT);
	Variant& operator= (double);
	Variant& operator= (std::string&);
	Variant& operator= (const char*);
	Variant& operator= (bool);
	Variant& operator= (char);
	Variant& operator= (const Variant&);
	
	Variant operator+ (int);
	Variant operator+ (INT);
	Variant operator+ (double);
	Variant operator+ (std::string&);
	Variant operator+ (const Variant&);

	Variant operator- (int);
	Variant operator- (INT);
	Variant operator- (double);
	Variant operator- (const Variant&);

	Variant operator* (int);
	Variant operator* (INT);
	Variant operator* (double);
	Variant operator* (const Variant&);

	Variant operator/ (int);
	Variant operator/ (INT);
	Variant operator/ (double);
	Variant operator/ (const Variant&);

	Variant& operator++ ();
	Variant& operator++ (int);

	Variant& operator-- ();
	Variant& operator-- (int);

	Variant& operator+= (int);
	Variant& operator+= (INT);
	Variant& operator+= (double);
	Variant& operator+= (const char*);
	Variant& operator+= (std::string&);
	Variant& operator+= (const Variant&);

	Variant& operator-= (int);
	Variant& operator-= (INT);
	Variant& operator-= (double);
	Variant& operator-= (const Variant&);

	Variant& operator*= (int);
	Variant& operator*= (INT);
	Variant& operator*= (double);
	Variant& operator*= (const Variant&);

	Variant& operator/= (int);
	Variant& operator/= (INT);
	Variant& operator/= (double);
	Variant& operator/= (const Variant&);

	bool operator< (const Variant&);

	void* operator&();

	friend std::ostream& operator<<(std::ostream& os, const Variant& var) {
		switch (var.type) {
		case DataType::INTEGER:
			os << var.int_data;
			break;
		case DataType::DOUBLE:
			os << var.double_data;
			break;
		case DataType::STRING:
			os << *var.string_data;
			break;
		case DataType::BOOLEAN:
			os << var.bool_data;
			break;
		case DataType::CHARACTER:
			os << var.char_data;
			break;
		default:
			break;
		}
		return os;
	}
};

#endif
