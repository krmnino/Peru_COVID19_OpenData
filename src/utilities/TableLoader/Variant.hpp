#ifndef VARIANT
#define VARIANT

#include <string>
#include <iostream>

enum DataType { INTEGER, DOUBLE, STRING, BOOLEAN, CHARACTER, UNDEFINED };

class Variant {
private:
	DataType type;
	union {
		int int_data;
		double double_data;
		std::string* string_data;
		bool bool_data;
		char char_data;
	};
public:
	Variant();
	Variant(const Variant&);
	Variant(int);
	Variant(double);
	Variant(std::string);
	Variant(bool);
	Variant(char);
	~Variant();

	int get_type();

	Variant& operator= (int);
	Variant& operator= (double);
	Variant& operator= (std::string&);
	Variant& operator= (bool);
	Variant& operator= (char);
	Variant& operator= (const Variant&);
	
	Variant operator+ (int);
	Variant operator+ (double);
	Variant operator+ (std::string&);
	Variant operator+ (const Variant&);

	Variant operator- (int);
	Variant operator- (double);
	Variant operator- (const Variant&);

	Variant operator* (int);
	Variant operator* (double);
	Variant operator* (const Variant&);

	Variant operator/ (int);
	Variant operator/ (double);
	Variant operator/ (const Variant&);

	Variant& operator++ ();
	Variant& operator++ (int);

	Variant& operator-- ();
	Variant& operator-- (int);

	Variant& operator+= (int);
	Variant& operator+= (double);
	Variant& operator+= (std::string&);
	Variant& operator+= (const Variant&);

	Variant& operator-= (int);
	Variant& operator-= (double);
	Variant& operator-= (const Variant&);

	Variant& operator*= (int);
	Variant& operator*= (double);
	Variant& operator*= (const Variant&);

	Variant& operator/= (int);
	Variant& operator/= (double);
	Variant& operator/= (const Variant&);

	bool operator< (const Variant&);

	void* operator&();

	friend std::ostream& operator<<(std::ostream& os, const Variant& var) {
		switch (var.type) {
		case INTEGER:
			os << var.int_data;
			break;
		case DOUBLE:
			os << var.double_data;
			break;
		case STRING:
			os << *var.string_data;
			break;
		case BOOLEAN:
			os << var.bool_data;
			break;
		case CHARACTER:
			os << var.char_data;
			break;
		default:
			break;
		}
		return os;
	}
};

#endif