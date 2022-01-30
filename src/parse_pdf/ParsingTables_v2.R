library("tabulizer")

report_path <- ""
pdf_areas_path <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFAreas.csv" 
PDF_pages_num_dict <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFTablePages.cl"
output_abs_path <- "C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables/"

################################################################################

PDF_table_num_pages <- file(PDF_pages_num_dict, "r")
pg_c <- 1
ln_c <- 1

while(ln_c <= n_pages){
  line = readLines(PDF_table_num_pages, n=1)
  print(line)
  if(length(line) == 0){
    break
  }
  line_split = strsplit(line, '=')
  if(pg_c > 10){
    report_path <- paste(report_path, substr(line_split[[1]][2], 1, nchar(line_split[[1]][2])-1), sep="")
  }
  pg_c <- pg_c + 1
  ln_c <- ln_c + 1
}

close(PDF_table_num_pages)

################################################################################

# Load csv file with PDF areas to be scanned
pdf_areas <- read.csv(pdf_areas_path)

# Pruebas acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[1,2:5]), guess=FALSE, pdf_areas[1,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
out_file_path <- paste(output_abs_path, pdf_areas[1,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por departamento
data <- extract_tables(report_path, area=list(pdf_areas[2,2:5]), guess=FALSE, pdf_areas[2,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
out_file_path <- paste(output_abs_path, pdf_areas[2,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por edades
data <- extract_tables(report_path, area=list(pdf_areas[3,2:5]), guess=FALSE, pdf_areas[3,6])
header <- list("Grupo", "Total", "Tasa_Ataque", "Razon_Tasas")
out_file_path <- paste(output_abs_path, pdf_areas[3,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[4,2:5]), guess=FALSE, pdf_areas[4,6])
header <- list("Depto", "Muertes_Total", "Muertes_Dia")
out_file_path <- paste(output_abs_path, pdf_areas[4,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2020 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[5,2:5]), guess=FALSE, pdf_areas[5,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[5,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2020 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[6,2:5]), guess=FALSE, pdf_areas[6,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[6,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2021 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[7,2:5]), guess=FALSE, pdf_areas[7,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[7,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2021 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[8,2:5]), guess=FALSE, pdf_areas[8,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[8,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por distrito pt.1
data <- extract_tables(report_path, area=list(pdf_areas[9,2:5]), guess=FALSE, pdf_areas[9,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
out_file_path <- paste(output_abs_path, pdf_areas[9,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por distrito pt.2
data <- extract_tables(report_path, area=list(pdf_areas[10,2:5]), guess=FALSE, pdf_areas[10,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
out_file_path <- paste(output_abs_path, pdf_areas[10,7], sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)


