# Paths to directories
ParsePDFDir = C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf;
RawTablesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables;
ConfigFilesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/config_files;
PADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/PruebasAcumuladasDepto;

# PDF Area config and csv files
PDFAreasCSV = PDFAreas.csv;
PDFAreasCL = PDFAreas.cl;

# Config files with information about departments and districts
DepartmentsAreas = DepartmentsAreas.cl;
DepartmentsIndex = DepartmentsIndex.cl;
DepartmentsMacroregions = DepartmentsMacroregions.cl;
DepartmentsPopulation = DepartmentsPopulation.cl;
DistrictsIndex = DistrictsIndex.cl;
DistrictsZones = DistrictsZones.cl;
AgeGroupsIndex = AgeGroupsIndex.cl;

# Headers for processing raw rables
PruebasAcumuladasDepto_Hdr = [Depto, PCR, PR, AG, Total];
CasosAcumuladosDepto_Hdr = [Depto, PCR, PR, AG, Total];
CasosPositivosEdades_Hdr = [Grupo, Total, Tasa_Ataque, Razon_Tasas];
MuertesAcumuladasDepto_Hdr = [Depto, Muertes_Total, Muertes_Dia];
CasosAcumuDistrito2020P1_Hdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CasosAcumuDistrito2020P2_Hdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CasosAcumuDistrito2021P1_Hdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CasosAcumuDistrito2021P2_Hdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
MuertesAcumulaDistritoP1_Hdr = [Distrito, Defunciones, Tasa_Mortalidad];
MuertesAcumulaDistritoP2_Hdr = [Distrito, Defunciones, Tasa_Mortalidad];

# Number of departments and districts
DeptoNum = 26;
DistrNum = 44;

# Headers for final tables
PADepto_Hdr = [Dia, PCR, PR, AG, Pruebas_Totales];
CADepto_Hdr = [Dia, PCR, PR, AG, Casos_Totales];
CAEdades_Hdr = [Nino_Total, Adolescente_Total, Joven_Total, Adulto_Total, AdultoMay_Total,
                Nino_TAtaq, Adolescente_TAtaq, Joven_TAtaq, Adulto_TAtaq, AdultoMay_TAtaq,
                Nino_RazonT, Adolescente_RazonT, Joven_RazonT, Adulto_RazonT, AdultoMay_RazonT];
CADistr20_Hdr = [Dia, Casos_Totales, Tasa_Ataque];
CADistr21_Hdr = [Dia, Casos_Totales, Tasa_Ataque];
MADistr_Hdr = [Dia, Muertes_Totales, Tasa_Mortalidad];
