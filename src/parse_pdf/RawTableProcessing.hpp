#ifndef RTP
#define RTP

#include "../utilities/DataVariant/Variant.hpp"
#include "../utilities/TableLoader/Table.hpp"
#include "../utilities/ConfigLoader/ConfigLoader.hpp"

#include <string>
#include <vector>
#include <exception>

int check_data_type(std::string&);
Variant convert2integer(int, std::vector<std::vector<Variant>>&);
Variant convert2double(int, std::vector<std::vector<Variant>>&);
void set_proper_col_names(cl::Config&, tl::Table&);
std::string get_report_date(cl::Config*);

int process_pa_depto(tl::Table*&, cl::Config*, cl::Config*);
int process_ca_depto(tl::Table*&, cl::Config*, cl::Config*);
int process_cp_edades(tl::Table*&, cl::Config*, cl::Config*);
int process_ma_depto(tl::Table*&, cl::Config*, cl::Config*);
int process_ma_deptosm(tl::Table*&, cl::Config*, cl::Config*);
int process_ca_distr_20(tl::Table*&, tl::Table*&, cl::Config*, cl::Config*);
int process_ca_distr_21(tl::Table*&, tl::Table*&, cl::Config*, cl::Config*);
int process_ma_distr(tl::Table*&, tl::Table*&, cl::Config*, cl::Config*, cl::Config*);

int append_begin_pa_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_ca_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_cp_edades(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_ma_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_ma_deptosm(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_ca_distr_20(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_begin_ca_distr_21(tl::Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ma_distr(tl::Table*&, cl::Config*, std::string, cl::Config*);

int append_end_pa_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ca_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_cp_edades(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ma_depto(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ma_deptosm(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ca_distr_20(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ca_distr_21(tl::Table*&, cl::Config*, std::string, cl::Config*);
int append_end_ma_distr(tl::Table*&, cl::Config*, cl::Config*, cl::Config*);

#endif // !RTP
