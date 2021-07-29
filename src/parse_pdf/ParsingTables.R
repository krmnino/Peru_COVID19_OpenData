library("tabulizer")

pdf_areas_path <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFAreas.csv" 
report_path <- "D:/temporary/DGE-MINSA_Reports/June_2021/coronavirus010621.pdf"
output_abs_path <- "C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables/"

# Load csv file with PDF areas to be scanned
pdf_areas <- read.csv(pdf_areas_path)

# Pruebas acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[1,2:5]), guess=FALSE, pdf_areas[1,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
out_file_path <- paste(output_abs_path, pdf_areas[1,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por departamento
data <- extract_tables(report_path, area=list(pdf_areas[2,2:5]), guess=FALSE, pdf_areas[2,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
out_file_path <- paste(output_abs_path, pdf_areas[2,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por edades
data <- extract_tables(report_path, area=list(pdf_areas[3,2:5]), guess=FALSE, pdf_areas[3,6])
header <- list("Grupo", "Total", "Tasa_Ataque", "Razon_Tasas")
out_file_path <- paste(output_abs_path, pdf_areas[3,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[4,2:5]), guess=FALSE, pdf_areas[4,6])
header <- list("Depto", "Muertes_Total", "Muertes_Dia")
out_file_path <- paste(output_abs_path, pdf_areas[4,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2020 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[5,2:5]), guess=FALSE, pdf_areas[5,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[5,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2020 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[6,2:5]), guess=FALSE, pdf_areas[6,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[6,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2021 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[7,2:5]), guess=FALSE, pdf_areas[7,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[7,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Casos acumulados por distrito 2021 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[8,2:5]), guess=FALSE, pdf_areas[8,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
out_file_path <- paste(output_abs_path, pdf_areas[8,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por distrito pt.1
data <- extract_tables(report_path, area=list(pdf_areas[9,2:5]), guess=FALSE, pdf_areas[9,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
out_file_path <- paste(output_abs_path, pdf_areas[9,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)

# Muertes acumuladas por distrito pt.2
data <- extract_tables(report_path, area=list(pdf_areas[10,2:5]), guess=FALSE, pdf_areas[10,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
out_file_path <- paste(output_abs_path, pdf_areas[10,1], ".csv", sep="")
write.table(data, out_file_path, sep=";", row.names=FALSE, col.names=header, quote=FALSE)


