#ifndef RTP
#define RTP

#include "../../../utilities/DataVariant/Variant.hpp"
#include "../../../utilities/TableLoader/Table.hpp"
#include "../../../utilities/ConfigLoader/ConfigLoader.hpp"

#include <string>
#include <vector>

int check_data_type(std::string&);
Variant convert_to_number(int, std::vector<std::vector<Variant>>&);
void set_proper_col_names(Config&, Table&);

int process_pa_depto(Table*&, Config*, Config*, Config*);
int process_ca_depto(Table*&, Config*, Config*, Config*);
int process_cp_edades(Table*&, Config*, Config*, Config*);
int process_ma_depto(Table*&, Config*, Config*, Config*);
int process_ca_distr_20(Table*&, Table*&, Config*, Config*, Config*);
int process_ca_distr_21(Table*&, Table*&, Config*, Config*, Config*);
int process_ma_distr(Table*&, Table*&, Config*, Config*, Config*);

int append_end_pa_depto(Table*&, Config*, Config*, Config*);
int append_end_ca_depto(Table*&, Config*, Config*, Config*);
int append_end_cp_edades(Table*&, Config*, Config*, Config*);
//int process_ma_depto(Table*&, Config*, Config*, Config*);
//int process_ca_distr_20(Table*&, Table*&, Config*, Config*, Config*);
//int process_ca_distr_21(Table*&, Table*&, Config*, Config*, Config*);
//int process_ma_distr(Table*&, Table*&, Config*, Config*, Config*);



#endif // !RTP

