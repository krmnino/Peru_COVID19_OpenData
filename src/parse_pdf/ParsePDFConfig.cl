# Paths to directories
ParsePDFDir = C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf;
RawTablesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables;
ConfigFilesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/config_files;
PADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/PruebasAcumuladasDepto;
CADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuladosDepto;
CAEdades_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosPositivosEdades;
MADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumuladasDepto;
MADeptoSM_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumuladasDepto_SINADEF-MINSA;
CADistr20_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuDistrito2020;
CADistr21_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuDistrito2021;
MADistr_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumulaDistrito;


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
MuertesAcumuladasDeptoSM_Hdr = [Depto, Muertes_Conf, Muertes_Sosp, Total_Muertes_SisVig, Muertes_SINADEF];
CasosAcumuDistrito2020P1_Hdr = [Distrito, Casos_Totales, Tasa_Ataque];
CasosAcumuDistrito2020P2_Hdr = [Distrito, Casos_Totales, Tasa_Ataque];
CasosAcumuDistrito2021P1_Hdr = [Distrito, Casos_Totales, Tasa_Ataque];
CasosAcumuDistrito2021P2_Hdr = [Distrito, Casos_Totales, Tasa_Ataque];
MuertesAcumulaDistritoP1_Hdr = [Distrito, Defunciones, Tasa_Mortalidad];
MuertesAcumulaDistritoP2_Hdr = [Distrito, Defunciones, Tasa_Mortalidad];

# Number of departments and districts
DeptoNum = 26;
DistrNum = 43;

# Headers for final tables
PADepto_Hdr = [Dia, PCR, PR, AG, Pruebas_Totales];
CADepto_Hdr = [Dia, PCR, PR, AG, Casos_Totales];
CAEdades_Hdr = [Dia, Nino_Total, Nino_TAtaq, Nino_RazonT,
                Adolescente_Total, Adolescente_TAtaq, Adolescente_RazonT,
                Joven_Total, Joven_TAtaq, Joven_RazonT,
                Adulto_Total, Adulto_TAtaq, Adulto_RazonT,
                AdultoMay_Total, AdultoMay_TAtaq, AdultoMay_RazonT];
MADepto_Hdr = [Dia, Muertes_Totales, Muertes_Dia];
MADeptoSM_Hdr = [Dia, Muertes_Confirmadas, Muertes_Sospechosas,
                 Total_Muertes_SisVig, Total_Muertes_SINADEF];
CADistr20_Hdr = [Dia, Casos_Totales, Tasa_Ataque];
CADistr21_Hdr = [Dia, Casos_Totales, Tasa_Ataque];
MADistr_Hdr = [Dia, Muertes_Totales, Tasa_Mortalidad];

EraseCADistr20Fields = [Porcentaje];
EraseCADistr21Fields = [Porcentaje];

# Additional final table names
CAEdades_Table = CasosPositivosEdades.csv;

# DetectPDFText Constants
WindowWidth = 1760;
WindowHeight = 990;
PADepto_RawRows = 26;
CADepto_RawRows = 26;
CAEdades_RawRows = 5;
MADepto_RawRows = 26;
MADeptoSM_RawRows = 26;
CADistr20P1_RawRows = 22;
CADistr20P2_RawRows = 22;
CADistr21P1_RawRows = 22;
CADistr21P2_RawRows = 22;
MADistrP1_RawRows = 22;
MADistrP2_RawRows = 22;
