#include <iostream>
#include <fstream>
#include <string>
#include <vector>

std::vector<std::string> split_row_commas(std::string &str_row){
    std::vector<std::string> parsed_row;
    int comma = str_row.find(',');
    while(comma != -1){
        parsed_row.push_back(str_row.substr(0, comma));
        str_row = str_row.substr(comma + 1, str_row.length());
        comma = str_row.find(',');
    }
    parsed_row.push_back(str_row);
    return parsed_row;
}

std::vector<std::string> get_header(std::ifstream &file){
    std::string str_row;
    if (file.good()) {
        getline(file, str_row);
    }
	return split_row_commas(str_row);
}

bool is_number(std::string &value){
    for(int i = 0; i < value.length(); i++){
        if(!isdigit(value[i])){
            if(value[i] != '.'){
                return false;
            }
        }
    }
    return true;
}

void converter(std::ifstream &infile, std::ofstream &outfile, std::vector<std::string> &header){
    std::string json_contents = "[\n";
    std::string str_row;
    bool header_check = false;
    while(getline(infile, str_row)){
        if(!header_check){
            header_check = true;
            continue;
        }
        std::vector<std::string> parsed_row = split_row_commas(str_row);
        json_contents.append("\t{\n");
        for(int i = 0; i < header.size(); i++){
            json_contents.append("\t\t\"" + header[i] + "\": ");
            if(is_number(parsed_row[i])){
                json_contents.append(parsed_row[i]);
            }
            else{
                json_contents.append("\"" + parsed_row[i] + "\"");
            }
            if(i != header.size() - 1){
                json_contents.append(",\n");
            }
            else{
                json_contents.append("\n");
            }
        }
        json_contents.append("\t},\n");
    }
    json_contents = json_contents.substr(0, json_contents.length()-2);
    json_contents.append("\n]");
    outfile << json_contents;
    std::cout << "JSON file successfully generated." << std::endl;
}

int main(int argc, char *argv[]){
    if(argc != 3){
        std::cout << "usage: ./CSVtoJSON [IN FILE PATH] [OUT DIR PATH]" << std::endl;
        return 1;
    }
    std::ifstream infile;
    std::ofstream outfile;
	infile.open(argv[1]);
    outfile.open(std::string(argv[2]));
    if(!infile.good()){
        std::cout << "Input file path is invalid." << std::endl;
        return 1;
    }
    if(!outfile.good()){
        std::cout << "Output file location is invalid." << std::endl;
        return 1;
    }
    std::vector<std::string> header = get_header(infile);
    converter(infile, outfile, header);
    return 0;
}