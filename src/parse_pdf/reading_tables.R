f <- "D:/temporary/coronavirus260321.pdf"
data <- extract_areas(f, 3)

for (i in data){
  for (j in i){
    print(j)
  }
}