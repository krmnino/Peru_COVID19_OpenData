library("tabulizer")
f <- "D:/temporary/reports/May_2021/coronavirus010521.pdf"
data <- extract_areas(f, 3)

for (i in data){
  for (j in i){
    print(j)
  }
}