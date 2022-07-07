# Set up working environment
working_dir <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf"
setwd(working_dir)

# Include dependencies
library("tabulizer")
source("../utilities/ConfigLoader/ConfigLoader.R")

# Set up environment for ConfigLoader
ConfigLoader_set_env(working_dir)

################################################################################

# Load configuration files
Main_Config <- ConfigLoader_init("config/ParsePDFConfig.cl")
Areas_Config <- ConfigLoader_init("config/AreasPDF.cl")

# Extract and concatenate PDF report absolute path
report_path <- ConfigLoader_get_value(Areas_Config, "ReportPath")
report_name <- ConfigLoader_get_value(Areas_Config, "ReportFilename")
report_abs_path <- paste(report_path, report_name, sep="")

################################################################################

# Pruebas acumuladas por departamento
i <- 1
sprintf("%d -> Pruebas acumuladas por departamento", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "PADepto_PDFPage")
# Extract areas from PDF
Areas_PADepto <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_PADepto[[1]][["top"]]),
           as.character(Areas_PADepto[[1]][["left"]]),
           as.character(Areas_PADepto[[1]][["bottom"]]),
           as.character(Areas_PADepto[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_PADepto",
                                        list_value)

################################################################################

# Casos acumulados por departamento
i <- 2
sprintf("%d -> Casos acumulados por departamento", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CADepto_PDFPage")
# Extract areas from PDF
Areas_CADepto <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CADepto[[1]][["top"]]),
           as.character(Areas_CADepto[[1]][["left"]]),
           as.character(Areas_CADepto[[1]][["bottom"]]),
           as.character(Areas_CADepto[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CADepto",
                                        list_value)

################################################################################

# Casos acumulados por edades
i <- 3
sprintf("%d -> Casos acumulados por edades", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CPEdades_PDFPage")
# Extract areas from PDF
Areas_CPEdades <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CPEdades[[1]][["top"]]),
           as.character(Areas_CPEdades[[1]][["left"]]),
           as.character(Areas_CPEdades[[1]][["bottom"]]),
           as.character(Areas_CPEdades[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CPEdades",
                                        list_value)

################################################################################

# Muertes acumuladas por departamento
i <- 4
sprintf("%d -> Muertes acumuladas por departamento", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "MADepto_PDFPage")
# Extract areas from PDF
Areas_MADepto <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_MADepto[[1]][["top"]]),
           as.character(Areas_MADepto[[1]][["left"]]),
           as.character(Areas_MADepto[[1]][["bottom"]]),
           as.character(Areas_MADepto[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_MADepto",
                                        list_value)

################################################################################

# Casos acumulados por distrito 2020 pt.1
i <- 5
sprintf("%d -> Casos acumulados por distrito 2020 pt.1", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr20P1_PDFPage")
# Extract areas from PDF
Areas_CADistr20P1 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CADistr20P1[[1]][["top"]]),
           as.character(Areas_CADistr20P1[[1]][["left"]]),
           as.character(Areas_CADistr20P1[[1]][["bottom"]]),
           as.character(Areas_CADistr20P1[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CADistr20P1",
                                        list_value)

################################################################################

# Casos acumulados por distrito 2020 pt.2
i <- 6
sprintf("%d -> Casos acumulados por distrito 2020 pt.2", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr20P2_PDFPage")
# Extract areas from PDF
Areas_CADistr20P2 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CADistr20P2[[1]][["top"]]),
           as.character(Areas_CADistr20P2[[1]][["left"]]),
           as.character(Areas_CADistr20P2[[1]][["bottom"]]),
           as.character(Areas_CADistr20P2[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CADistr20P2",
                                        list_value)

################################################################################

# Casos acumulados por distrito 2021 pt.1
i <- 7
sprintf("%d -> Casos acumulados por distrito 2021 pt.1", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr21P1_PDFPage")
# Extract areas from PDF
Areas_CADistr21P1 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CADistr21P1[[1]][["top"]]),
           as.character(Areas_CADistr21P1[[1]][["left"]]),
           as.character(Areas_CADistr21P1[[1]][["bottom"]]),
           as.character(Areas_CADistr21P1[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CADistr21P1",
                                        list_value)

################################################################################

# Casos acumulados por distrito 2021 pt.2
i <- 8
sprintf("%d -> Casos acumulados por distrito 2021 pt.2", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "CADistr21P2_PDFPage")
# Extract areas from PDF
Areas_CADistr21P2 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_CADistr21P2[[1]][["top"]]),
           as.character(Areas_CADistr21P2[[1]][["left"]]),
           as.character(Areas_CADistr21P2[[1]][["bottom"]]),
           as.character(Areas_CADistr21P2[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_CADistr21P2",
                                        list_value)

################################################################################

# Muertes acumuladas por distrito pt.1
i <- 9
sprintf("%d -> Muertes acumuladas por distrito pt.1", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "MADistrP1_PDFPage")
# Extract areas from PDF
Areas_MADistrP1 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_MADistrP1[[1]][["top"]]),
           as.character(Areas_MADistrP1[[1]][["left"]]),
           as.character(Areas_MADistrP1[[1]][["bottom"]]),
           as.character(Areas_MADistrP1[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_MADistrP1",
                                        list_value)

################################################################################

# Muertes acumuladas por distrito pt.2
i <- 10
sprintf("%d -> Muertes acumuladas por distrito pt.2", i)
# Get PDF page
page <- ConfigLoader_get_value(Main_Config, "MADistrP2_PDFPage")
# Extract areas from PDF
Areas_MADistrP2 <- locate_areas(report_abs_path, page)
# Convert Named nums to characters
to_str = c(as.character(Areas_MADistrP2[[1]][["top"]]),
           as.character(Areas_MADistrP2[[1]][["left"]]),
           as.character(Areas_MADistrP2[[1]][["bottom"]]),
           as.character(Areas_MADistrP2[[1]][["right"]]))
# Convert list value to string
list_value <- "["
for(j in 1:length(to_str)){
  if(j != length(to_str)){
    list_value <- paste(list_value, to_str[j], ",", sep="")  
  }
  else{
    list_value <- paste(list_value, to_str[j], sep="")
  }
}
list_value <- paste(list_value, "]", sep="")
# Update coordinate list value 
Areas_Config <- ConfigLoader_edit_value(Areas_Config,
                                        "Areas_MADistrP2",
                                        list_value)

################################################################################

ConfigLoader_save_file(Areas_Config, "config/AreasPDF.cl")