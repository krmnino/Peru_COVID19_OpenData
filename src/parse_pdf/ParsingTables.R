library("tabulizer")

pdf_areas_path <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFAreas.csv" 
report_path <- "D:/temporary/DGE-MINSA_Reports/June_2021/coronavirus010621.pdf"
output_path <- "D:/temporary/output.csv"

# Load csv file with PDF areas to be scanned
pdf_areas <- read.csv(pdf_areas_path)

# Pruebas acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[1,2:5]), guess=FALSE, pdf_areas[1,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por departamento
data <- extract_tables(report_path, area=list(pdf_areas[2,2:5]), guess=FALSE, pdf_areas[2,6])
header <- list("Depto", "PCR", "PR", "AG", "Total")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por edades
data <- extract_tables(report_path, area=list(pdf_areas[3,2:5]), guess=FALSE, pdf_areas[3,6])
header <- list("Grupo", "Total", "Tasa_Ataque", "Razon_Tasas")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Muertes acumuladas por departamento
data <- extract_tables(report_path, area=list(pdf_areas[4,2:5]), guess=FALSE, pdf_areas[4,6])
header <- list("Depto", "Muertes_Total", "Muertes_Dia")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por distrito 2020 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[5,2:5]), guess=FALSE, pdf_areas[5,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por distrito 2020 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[6,2:5]), guess=FALSE, pdf_areas[6,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por distrito 2021 pt.1
data <- extract_tables(report_path, area=list(pdf_areas[7,2:5]), guess=FALSE, pdf_areas[7,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Casos acumulados por distrito 2021 pt.2
data <- extract_tables(report_path, area=list(pdf_areas[8,2:5]), guess=FALSE, pdf_areas[8,6])
header <- list("Distrito", "Casos_Totales", "Porcentaje", "Tasa_Ataque")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Muertes acumuladas por distrito pt.1
data <- extract_tables(report_path, area=list(pdf_areas[9,2:5]), guess=FALSE, pdf_areas[9,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)

# Muertes acumuladas por distrito pt.2
data <- extract_tables(report_path, area=list(pdf_areas[10,2:5]), guess=FALSE, pdf_areas[10,6])
header <- list("Distrito", "Defunciones", "Tasa_Mortalidad")
write.table(data, output_path, sep=",", row.names=FALSE, col.names=header)


