#ifndef CONFIG
#define CONFIG

#include <string>
#include <fstream>
#include <algorithm>
#include <map>
#include "Value.hpp"

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
	int get_n_pairs();
	std::vector<std::string> get_keys();
	Value* get_value(std::string);
	
};

#endif // !CONFIG
