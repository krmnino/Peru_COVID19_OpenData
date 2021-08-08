library("tabulizer")

report_path <- "D:/temporary/DGE-MINSA_Reports/June_2021/coronavirus010621.pdf"

PDF_pages_dict <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFTablePages.dat"
table_fnames_dict <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/RawTableFileNames.dat"

PDF_areas_out <- "C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf/PDFAreas.csv"

tables = 10
areas <- data.frame(name=rep("",tables),
                    top=rep(-1,tables),
                    left=rep(-1,tables),
                    bottom=rep(-1,tables),
                    right=rep(-1,tables),
                    pages=rep(1,tables),
                    fnames=rep(1,tables))

pdf_table_pages <- file(PDF_pages_dict, "r")
pg_c <- 1

while(TRUE){
  line = readLines(pdf_table_pages, n=1)
  if(length(line) == 0){
    break
  }
  line_split = strsplit(line, '=')
  areas[pg_c,1] = line_split[[1]][1]
  areas[pg_c,6] = line_split[[1]][2]
  pg_c <- pg_c + 1
}

close(pdf_table_pages)

table_fnames <- file(table_fnames_dict, "r")
tb_c <- 1

while(TRUE){
  line = readLines(table_fnames, n=1)
  if(length(line) == 0){
    break
  }
  line_split = strsplit(line, '=')
  areas[tb_c,7] = line_split[[1]][2]
  tb_c <- tb_c + 1
}

close(table_fnames)

i <- 1

# Pruebas acumuladas por departamento
sprintf("%d -> Pruebas acumuladas por departamento", i)
area_pruebas_depto   <- locate_areas(report_path, areas[i,6])
vec_area_pruebas_depto <- c()
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["top"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["left"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["bottom"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["right"]])
areas[i,2] <- vec_area_pruebas_depto[1]
areas[i,3] <- vec_area_pruebas_depto[2]
areas[i,4] <- vec_area_pruebas_depto[3]
areas[i,5] <- vec_area_pruebas_depto[4]
i <- i + 1

# Casos acumulados por departamento
sprintf("%d -> Casos acumulados por departamento", i)
area_casos_depto     <- locate_areas(report_path, areas[i,6])
vec_area_casos_depto <- c()
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["top"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["left"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["bottom"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["right"]])
areas[i,2] <- vec_area_casos_depto[1]
areas[i,3] <- vec_area_casos_depto[2]
areas[i,4] <- vec_area_casos_depto[3]
areas[i,5] <- vec_area_casos_depto[4]
i <- i + 1

# Casos acumulados por edades
sprintf("%d -> Casos acumulados por edades", i)
area_casos_edades    <- locate_areas(report_path, areas[i,6])
vec_area_casos_edades <- c()
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["top"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["left"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["bottom"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["right"]])
areas[i,2] <- vec_area_casos_edades[1]
areas[i,3] <- vec_area_casos_edades[2]
areas[i,4] <- vec_area_casos_edades[3]
areas[i,5] <- vec_area_casos_edades[4]
i <- i + 1

# Muertes acumuladas por departamento
sprintf("%d -> Muertes acumuladas por departamento", i)
area_muertes_depto   <- locate_areas(report_path, areas[i,6])
vec_area_muertes_depto <- c()
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["top"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["left"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["bottom"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["right"]])
areas[i,2] <- vec_area_muertes_depto[1]
areas[i,3] <- vec_area_muertes_depto[2]
areas[i,4] <- vec_area_muertes_depto[3]
areas[i,5] <- vec_area_muertes_depto[4]
i <- i + 1

# Casos acumulados por distrito 2020 pt.1
sprintf("%d -> Casos acumulados por distrito 2020 pt.1", i)
area_casos_distr20_1 <- locate_areas(report_path, areas[i,6])
vec_area_casos_distr20_1 <- c()
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["top"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["left"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["bottom"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["right"]])
areas[i,2] <- vec_area_casos_distr20_1[1]
areas[i,3] <- vec_area_casos_distr20_1[2]
areas[i,4] <- vec_area_casos_distr20_1[3]
areas[i,5] <- vec_area_casos_distr20_1[4]
i <- i + 1

# Casos acumulados por distrito 2020 pt.2
sprintf("%d -> Casos acumulados por distrito 2020 pt.2", i)
area_casos_distr20_2 <- locate_areas(report_path, areas[i,6])
vec_area_casos_distr20_2 <- c()
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["top"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["left"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["bottom"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["right"]])
areas[i,2] <- vec_area_casos_distr20_2[1]
areas[i,3] <- vec_area_casos_distr20_2[2]
areas[i,4] <- vec_area_casos_distr20_2[3]
areas[i,5] <- vec_area_casos_distr20_2[4]
i <- i + 1

# Casos acumulados por distrito 2021 pt.1
sprintf("%d -> Casos acumulados por distrito 2021 pt.1", i)
area_casos_distr21_1 <- locate_areas(report_path, areas[i,6])
vec_area_casos_distr21_1 <- c()
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["top"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["left"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["bottom"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["right"]])
areas[i,2] <- vec_area_casos_distr21_1[1]
areas[i,3] <- vec_area_casos_distr21_1[2]
areas[i,4] <- vec_area_casos_distr21_1[3]
areas[i,5] <- vec_area_casos_distr21_1[4]
i <- i + 1

# Casos acumulados por distrito 2021 pt.2
sprintf("%d -> Casos acumulados por distrito 2021 pt.2", i)
area_casos_distr21_2 <- locate_areas(report_path, areas[i,6])
vec_area_casos_distr21_2 <- c()
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["top"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["left"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["bottom"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["right"]])
areas[i,2] <- vec_area_casos_distr21_2[1]
areas[i,3] <- vec_area_casos_distr21_2[2]
areas[i,4] <- vec_area_casos_distr21_2[3]
areas[i,5] <- vec_area_casos_distr21_2[4]
i <- i + 1

# Muertes acumuladas por distrito pt.1
sprintf("%d -> Muertes acumuladas por distrito pt.1", i)
area_muertes_distr_1 <- locate_areas(report_path, areas[i,6])
vec_area_muertes_distr_1 <- c()
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["top"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["left"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["bottom"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["right"]])
areas[i,2] <- vec_area_muertes_distr_1[1]
areas[i,3] <- vec_area_muertes_distr_1[2]
areas[i,4] <- vec_area_muertes_distr_1[3]
areas[i,5] <- vec_area_muertes_distr_1[4]
i <- i + 1

# Muertes acumuladas por distrito pt.2
sprintf("%d -> Muertes acumuladas por distrito pt.2", i)
area_muertes_distr_2 <- locate_areas(report_path, areas[i,6])
vec_area_muertes_distr_2 <- c()
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["top"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["left"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["bottom"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["right"]])
areas[i,2] <- vec_area_muertes_distr_2[1]
areas[i,3] <- vec_area_muertes_distr_2[2]
areas[i,4] <- vec_area_muertes_distr_2[3]
areas[i,5] <- vec_area_muertes_distr_2[4]
i <- i + 1

write.table(areas, PDF_areas_out, sep = ",", row.names=FALSE, quote=FALSE)
