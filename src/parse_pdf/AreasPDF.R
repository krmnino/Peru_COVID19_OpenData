library("tabulizer")

setwd("C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf")
report_path <- "D:/temporary/DGE-MINSA_Reports/June_2021/coronavirus010621.pdf"
PDF_pages_dict <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFTablePages.dat"

tables = 10
areas <- data.frame(top=rep(-1,10),
                    left=rep(-1,10),
                    bottom=rep(-1,10),
                    right=rep(-1,10),
                    pages=rep(1,10))
area_col_names = c("top", "left", "bottom", "right") 

pdf_file <- file(PDF_pages_dict, "r")

while(TRUE){
  line = readLines(pdf_file, n=1)
  if(length(line) == 0){
    break
  }
  line_split = strsplit(line, '=')
  print(line_split)
}

close(pdf_file)

i <- 1

# Pruebas acumuladas por departamento
sprintf("%d -> Pruebas acumuladas por departamento", i)
area_pruebas_depto   <- locate_areas(report_path, pages = 3)
vec_area_pruebas_depto <- c()
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["top"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["left"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["bottom"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["right"]])
areas[1,1] <- vec_area_pruebas_depto[1]
areas[1,2] <- vec_area_pruebas_depto[2]
areas[1,3] <- vec_area_pruebas_depto[3]
areas[1,4] <- vec_area_pruebas_depto[4]
i <- i + 1

# Casos acumulados por departamento
sprintf("%d -> Casos acumulados por departamento", i)
area_casos_depto     <- locate_areas(report_path, pages = 3)
vec_area_casos_depto <- c()
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["top"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["left"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["bottom"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["right"]])
areas[2,1] <- vec_area_casos_depto[1]
areas[2,2] <- vec_area_casos_depto[2]
areas[2,3] <- vec_area_casos_depto[3]
areas[2,4] <- vec_area_casos_depto[4]
i <- i + 1

# Casos acumulados por edades
sprintf("%d -> Casos acumulados por edades", i)
area_casos_edades    <- locate_areas(report_path, pages = 14)
vec_area_casos_edades <- c()
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["top"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["left"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["bottom"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["right"]])
areas[3,1] <- vec_area_casos_edades[1]
areas[3,2] <- vec_area_casos_edades[2]
areas[3,3] <- vec_area_casos_edades[3]
areas[3,4] <- vec_area_casos_edades[4]
i <- i + 1

# Muertes acumuladas por departamento
sprintf("%d -> Muertes acumuladas por departamento", i)
area_muertes_depto   <- locate_areas(report_path, pages = 21)
vec_area_muertes_depto <- c()
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["top"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["left"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["bottom"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["right"]])
areas[4,1] <- vec_area_muertes_depto[1]
areas[4,2] <- vec_area_muertes_depto[2]
areas[4,3] <- vec_area_muertes_depto[3]
areas[4,4] <- vec_area_muertes_depto[4]
i <- i + 1

# Casos acumulados por distrito 2020 pt.1
sprintf("%d -> Casos acumulados por distrito 2020 pt.1", i)
area_casos_distr20_1 <- locate_areas(report_path, pages = 76)
vec_area_casos_distr20_1 <- c()
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["top"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["left"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["bottom"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["right"]])
areas[5,1] <- vec_area_casos_distr20_1[1]
areas[5,2] <- vec_area_casos_distr20_1[2]
areas[5,3] <- vec_area_casos_distr20_1[3]
areas[5,4] <- vec_area_casos_distr20_1[4]
i <- i + 1

# Casos acumulados por distrito 2020 pt.2
sprintf("%d -> Casos acumulados por distrito 2020 pt.2", i)
area_casos_distr20_2 <- locate_areas(report_path, pages = 76)
vec_area_casos_distr20_2 <- c()
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["top"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["left"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["bottom"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["right"]])
areas[6,1] <- vec_area_casos_distr20_2[1]
areas[6,2] <- vec_area_casos_distr20_2[2]
areas[6,3] <- vec_area_casos_distr20_2[3]
areas[6,4] <- vec_area_casos_distr20_2[4]
i <- i + 1

# Casos acumulados por distrito 2021 pt.1
sprintf("%d -> Casos acumulados por distrito 2021 pt.1", i)
area_casos_distr21_1 <- locate_areas(report_path, pages = 77)
vec_area_casos_distr21_1 <- c()
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["top"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["left"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["bottom"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["right"]])
areas[7,1] <- vec_area_casos_distr21_1[1]
areas[7,2] <- vec_area_casos_distr21_1[2]
areas[7,3] <- vec_area_casos_distr21_1[3]
areas[7,4] <- vec_area_casos_distr21_1[4]
i <- i + 1

# Casos acumulados por distrito 2021 pt.2
sprintf("%d -> Casos acumulados por distrito 2021 pt.1", i)
area_casos_distr21_2 <- locate_areas(report_path, pages = 77)
vec_area_casos_distr21_2 <- c()
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["top"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["left"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["bottom"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["right"]])
areas[8,1] <- vec_area_casos_distr21_2[1]
areas[8,2] <- vec_area_casos_distr21_2[2]
areas[8,3] <- vec_area_casos_distr21_2[3]
areas[8,4] <- vec_area_casos_distr21_2[4]
i <- i + 1

# Muertes acumuladas por distrito pt.1
sprintf("%d -> Muertes acumuladas por distrito pt.1", i)
area_muertes_distr_1 <- locate_areas(report_path, pages = 80)
vec_area_muertes_distr_1 <- c()
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["top"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["left"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["bottom"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["right"]])
areas[9,1] <- vec_area_muertes_distr_1[1]
areas[9,2] <- vec_area_muertes_distr_1[2]
areas[9,3] <- vec_area_muertes_distr_1[3]
areas[9,4] <- vec_area_muertes_distr_1[4]
i <- i + 1

# Muertes acumuladas por distrito pt.2
sprintf("%d -> Muertes acumuladas por distrito pt.2", i)
area_muertes_distr_2 <- locate_areas(report_path, pages = 80)
vec_area_muertes_distr_2 <- c()
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["top"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["left"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["bottom"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["right"]])
areas[10,1] <- vec_area_muertes_distr_2[1]
areas[10,2] <- vec_area_muertes_distr_2[2]
areas[10,3] <- vec_area_muertes_distr_2[3]
areas[10,4] <- vec_area_muertes_distr_2[4]
i <- i + 1

setwd("C:/Users/kurt_/github/Peru_COVID19_Stats/res")
write.table(areas, "areas.csv", sep = ",", row.names=FALSE, col.names=area_col_names)

setwd("C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf")


