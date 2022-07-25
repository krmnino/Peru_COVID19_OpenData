#ifndef CONFIG
#define CONFIG

#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include "CLErrorHandler.hpp"
#include "Value.hpp"

namespace cl {
class Config {
private:
	int n_pairs;
	std::map<std::string, int> keys_index;
	std::vector<Value*> values;

	void split_string(std::vector<std::string>&, std::string&, char);
	void remove_side_spaces(std::string&);

public:
	Config(std::string);
	Config();
	~Config();
	int get_n_entries(void);
	std::vector<std::string> get_all_keys();
	Value* get_value(std::string);
	std::vector<std::pair<std::string, Value*>> get_all_key_values();
	void add_entry(std::string, int);
	void add_entry(std::string, double);
	void add_entry(std::string, std::string);
	void add_entry(std::string, const char*);
	void add_entry(std::string, List);
	void edit_value(std::string, int);
	void edit_value(std::string, double);
	void edit_value(std::string, std::string);
	void edit_value(std::string, const char*);
	void edit_value(std::string, List);
	void save_config(std::string);
};
}

#endif // !CONFIG
