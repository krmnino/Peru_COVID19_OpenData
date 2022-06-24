#ifndef RTP
#define RTP

#include "../../../utilities/DataVariant/Variant.hpp"
#include "../../../utilities/TableLoader/Table.hpp"
#include "../../../utilities/ConfigLoader/ConfigLoader.hpp"

#include <string>
#include <vector>
#include <exception>

int check_data_type(std::string&);
Variant convert_to_number(int, std::vector<std::vector<Variant>>&);
void set_proper_col_names(cl::Config&, Table&);

int process_pa_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ca_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_cp_edades(Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ma_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ma_deptosm(Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ca_distr_20(Table*&, Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ca_distr_21(Table*&, Table*&, cl::Config*, cl::Config*, cl::Config*);
int process_ma_distr(Table*&, Table*&, cl::Config*, cl::Config*, cl::Config*);

int append_begin_pa_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ca_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_cp_edades(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ma_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ma_deptosm(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ca_distr_20(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ca_distr_21(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_begin_ma_distr(Table*&, cl::Config*, cl::Config*, cl::Config*);

int append_end_pa_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ca_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_cp_edades(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ma_depto(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ma_deptosm(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ca_distr_20(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ca_distr_21(Table*&, cl::Config*, cl::Config*, cl::Config*);
int append_end_ma_distr(Table*&, cl::Config*, cl::Config*, cl::Config*);

#endif // !RTP
