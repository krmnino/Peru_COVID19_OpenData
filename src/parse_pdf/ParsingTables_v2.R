# Set up working environment
working_dir <- "C:/Users/kurt_/github/Peru_COVID19_Stats/"
setwd(working_dir)

# Include dependencies
library("tabulizer")
source("src/utilities/ConfigLoader/ConfigLoader.R")

# Set up environment for ConfigLoader
ConfigLoader_set_env(working_dir)

################################################################################

# Load configuration files
Main_Config <- ConfigLoader_init("src/parse_pdf/config/ParsePDFConfig.cl")
areas_config_path <- ConfigLoader_get_value(Main_Config, "AreasPDFCL")
Areas_Config <- ConfigLoader_init(paste(working_dir, areas_config_path, sep=""))

# Extract and concatenate PDF report absolute path
report_path <- ConfigLoader_get_value(Areas_Config, "ReportPath")
report_name <- ConfigLoader_get_value(Areas_Config, "ReportFilename")
report_abs_path <- paste(report_path, report_name, sep="")

# Extract repository top level path
top_level_path <- ConfigLoader_get_value(Main_Config, "WindowsTopLevel")

################################################################################

# Pruebas acumuladas por departamento

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "PADepto_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_PADepto")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "PADepto_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "PADepto_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por departamento

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CADepto_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CADepto")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CADepto_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CADepto_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por edades

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CPEdades_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CPEdades")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CPEdades_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CPEdades_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Muertes acumuladas por departamento

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "MADepto_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_MADepto")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "MADepto_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "MADepto_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por distrito 2020 pt.1

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr20P1_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CADistr20P1")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CADistr20P1_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CADistr20P1_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por distrito 2020 pt.2

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr20P2_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CADistr20P2")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CADistr20P2_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CADistr20P2_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por distrito 2021 pt.1

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr21P1_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CADistr21P1")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CADistr21P1_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CADistr21P1_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Casos acumulados por distrito 2021 pt.2

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr21P2_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_CADistr21P2")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "CADistr21P2_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "CADistr21P2_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Muertes acumuladas por distrito pt.1

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "MADistrP1_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_MADistrP1")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "MADistrP1_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "MADistrP1_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)

################################################################################

# Muertes acumuladas por distrito pt.2

# Extract PDF page
page <- ConfigLoader_get_value(Main_Config, "MADistrP2_PDFPage")

# Extract and covert PDF area
area_list <- ConfigLoader_get_value(Areas_Config, "Areas_MADistrP2")
to_double <- c()
for(i in 1:length(area_list)){
  to_double <- append(to_double, as.double(area_list[i]))
}

# Extract PDF table
data <- extract_tables(report_abs_path,
                       area=list(to_double),
                       guess=FALSE, pages=page)

# Extract table header and convert to list
header <- ConfigLoader_get_value(Main_Config, "MADistrP2_RTHdr")
header_list <- list()
for(i in 1:length(header)){
  header_list <- append(header_list, header[i])
}

# Build raw table path
raw_table_path <- ConfigLoader_get_value(Main_Config, "MADistrP2_RT")
raw_table_path <- paste(top_level_path, raw_table_path, sep="")

# Write data to table 
write.table(data,
            raw_table_path, sep=";",
            row.names=FALSE,
            col.names=header_list,
            quote=FALSE)