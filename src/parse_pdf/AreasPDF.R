library("tabulizer")

report_path <- "D:/temporary/reports/June_2021/coronavirus010621.pdf"

areas <- data.frame()
area_col_names = c("top", "left", "bottom", "right") 

# Pruebas acumulados por departamento
area_pruebas_depto   <- locate_areas(report_path, pages = 3)
vec_area_pruebas_depto <- c()
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["top"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["left"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["bottom"]])
vec_area_pruebas_depto <- append(vec_area_pruebas_depto, area_pruebas_depto[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_pruebas_depto)))

# Casos acumulados por departamento
area_casos_depto     <- locate_areas(report_path, pages = 3)
vec_area_casos_depto <- c()
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["top"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["left"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["bottom"]])
vec_area_casos_depto <- append(vec_area_casos_depto, area_casos_depto[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_depto)))

# Casos acumulados por edades
area_casos_edades    <- locate_areas(report_path, pages = 14)
vec_area_casos_edades <- c()
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["top"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["left"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["bottom"]])
vec_area_casos_edades <- append(vec_area_casos_edades, area_casos_edades[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_edades)))

# Muertes acumuladas por departamento
area_muertes_depto   <- locate_areas(report_path, pages = 21)
vec_area_muertes_depto <- c()
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["top"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["left"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["bottom"]])
vec_area_muertes_depto <- append(vec_area_muertes_depto, area_muertes_depto[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_muertes_depto)))

# Casos acumulados por distrito 2020 pt.1
area_casos_distr20_1 <- locate_areas(report_path, pages = 76)
vec_area_casos_distr20_1 <- c()
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["top"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["left"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["bottom"]])
vec_area_casos_distr20_1 <- append(vec_area_casos_distr20_1, area_casos_distr20_1[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_distr20_1)))

# Casos acumulados por distrito 2020 pt.2
area_casos_distr20_2 <- locate_areas(report_path, pages = 76)
vec_area_casos_distr20_2 <- c()
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["top"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["left"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["bottom"]])
vec_area_casos_distr20_2 <- append(vec_area_casos_distr20_2, area_casos_distr20_2[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_distr20_2)))

# Casos acumulados por distrito 2021 pt.1
area_casos_distr21_1 <- locate_areas(report_path, pages = 77)
vec_area_casos_distr21_1 <- c()
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["top"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["left"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["bottom"]])
vec_area_casos_distr21_1 <- append(vec_area_casos_distr21_1, area_casos_distr21_1[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_distr21_1)))

# Casos acumulados por distrito 2021 pt.2
area_casos_distr21_2 <- locate_areas(report_path, pages = 77)
vec_area_casos_distr21_2 <- c()
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["top"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["left"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["bottom"]])
vec_area_casos_distr21_2 <- append(vec_area_casos_distr21_2, area_casos_distr21_2[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_casos_distr21_2)))

# Muertes acumuladas por distrito pt.1
area_muertes_distr_1 <- locate_areas(report_path, pages = 80)
vec_area_muertes_distr_1 <- c()
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["top"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["left"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["bottom"]])
vec_area_muertes_distr_1 <- append(vec_area_muertes_distr_1, area_muertes_distr_1[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_muertes_distr_1)))

# Muertes acumuladas por distrito pt.2
area_muertes_distr_2 <- locate_areas(report_path, pages = 80)
vec_area_muertes_distr_2 <- c()
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["top"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["left"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["bottom"]])
vec_area_muertes_distr_2 <- append(vec_area_muertes_distr_2, area_muertes_distr_2[[1]][["right"]])
areas <- rbind(areas, data.frame(t(vec_area_muertes_distr_2)))

write.table(areas, "areas.csv", sep = ",", row.names=FALSE, col.names=area_col_names)
