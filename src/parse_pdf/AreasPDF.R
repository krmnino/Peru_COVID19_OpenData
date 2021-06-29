library("tabulizer")

report_path <- "D:/temporary/reports/June_2021/coronavirus010621.pdf"

# Pruebas acumulados por departamento
area_pruebas_depto   <- locate_areas(report_path, pages = 3)

# Casos acumulados por departamento
area_casos_depto     <- locate_areas(report_path, pages = 3)

# Casos acumulados por edades
area_casos_edades    <- locate_areas(report_path, pages = 14)

# Muertes acumuladas por departamento
area_muertes_depto   <- locate_areas(report_path, pages = 21)

# Casos acumulados por distrito 2020 pt.1
area_casos_distr20_1 <- locate_areas(report_path, pages = 76)

# Casos acumulados por distrito 2020 pt.2
area_casos_distr20_2 <- locate_areas(report_path, pages = 76)

# Casos acumulados por distrito 2021 pt.1
area_casos_distr21_1 <- locate_areas(report_path, pages = 77)

# Casos acumulados por distrito 2021 pt.2
area_casos_distr21_2 <- locate_areas(report_path, pages = 77)

# Muertes acumuladas por distrito pt.1
area_muertes_distr_1 <- locate_areas(report_path, pages = 80)

# Muertes acumuladas por distrito pt.2
area_muertes_distr_2 <- locate_areas(report_path, pages = 80)
