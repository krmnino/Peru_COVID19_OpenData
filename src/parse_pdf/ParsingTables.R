library("tabulizer")

report_path <- "D:/temporary/reports/May_2021/coronavirus010521.pdf"
output_path <- "D:/temporary/output.csv"

area_pdf <- locate_areas(report_path, pages = 3)

#data <- extract_areas(report_path, 3)
data <- extract_tables(report_path, area=area_pdf, guess=FALSE, 3)


write.csv(data, output_path, row.names=FALSE, header=FALSE)