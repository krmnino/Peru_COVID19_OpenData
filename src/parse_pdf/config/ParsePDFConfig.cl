# Paths to directories
ParsePDFDir = C:/Users/kurt_/github/Peru_COVID19_Stats/src/parse_pdf;
RawTablesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/raw_tables;
ConfigFilesDir = C:/Users/kurt_/github/Peru_COVID19_Stats/res/config_files;
PADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/PruebasAcumuladasDepto;
CADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuladosDepto;
CPEdades_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosPositivosEdades;
MADepto_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumuladasDepto;
MADeptoSM_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumuladasDepto_SINADEF-MINSA;
CADistr20_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuDistrito2020;
CADistr21_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/CasosAcumuDistrito2021;
MADistr_Dir = C:/Users/kurt_/github/Peru_COVID19_Stats/data/MuertesAcumulaDistrito;
CPEdades_PTName = CasosPositivosEdades.csv;

# PDF Area config and csv files
PDFAreasCSV = config/PDFAreas.csv;
PDFAreasCL = config/PDFAreas.cl;

# Config files with information about departments and districts
DepartmentsAreas = ../../res/config_files/DepartmentsAreas.cl;
DepartmentsIndex = ../../res/config_files/DepartmentsIndex.cl;
DepartmentsMacroregions = ../../res/config_files/DepartmentsMacroregions.cl;
DepartmentsPopulation = ../../res/config_files/DepartmentsPopulation.cl;
DistrictsIndex = ../../res/config_files/DistrictsIndex.cl;
DistrictsZones = ../../res/config_files/DistrictsZones.cl;
AgeGroupsIndex = ../../res/config_files/AgeGroupsIndex.cl;

# Headers for processing raw rables
PADepto_RTHdr = [Depto, PCR, PR, AG, Total];
CADepto_RTHdr = [Depto, PCR, PR, AG, Total];
CPEdades_RTHdr = [Grupo, Total, Tasa_Ataque, Razon_Tasas];
MADepto_RTHdr = [Depto, Muertes_Total, Muertes_Dia];
MADeptoSM_RTHdr = [Depto, Muertes_Conf, Muertes_Sosp, Total_Muertes_SisVig, Muertes_SINADEF];
CADistr20P1_RTHdr = [Distrito, Casos_Totales, Tasa_Ataque];
CADistr20P2_RTHdr = [Distrito, Casos_Totales, Tasa_Ataque];
CADistr21P1_RTHdr = [Distrito, Casos_Totales, Tasa_Ataque];
CADistr21P2_RTHdr = [Distrito, Casos_Totales, Tasa_Ataque];
MADistrP1_RTHdr = [Distrito, Defunciones, Tasa_Mortalidad];
MADistrP2_RTHdr = [Distrito, Defunciones, Tasa_Mortalidad];

# Number of departments and districts
DeptoNum = 26;
DistrNum = 43;

# Headers for processed tables
PADepto_PTHdr = [Dia, PCR, PR, AG, Pruebas_Totales];
CADepto_PTHdr = [Dia, PCR, PR, AG, Casos_Totales];
CPEdades_PTHdr = [Dia, Nino_Total, Nino_TAtaq, Nino_RazonT,
                Adolescente_Total, Adolescente_TAtaq, Adolescente_RazonT,
                Joven_Total, Joven_TAtaq, Joven_RazonT,
                Adulto_Total, Adulto_TAtaq, Adulto_RazonT,
                AdultoMay_Total, AdultoMay_TAtaq, AdultoMay_RazonT];
MADepto_PTHdr = [Dia, Muertes_Totales, Muertes_Dia];
MADeptoSM_PTHdr = [Dia, Muertes_Confirmadas, Muertes_Sospechosas,
                 Total_Muertes_SisVig, Total_Muertes_SINADEF];
CADistr20_PTHdr = [Dia, Casos_Totales, Tasa_Ataque];
CADistr21_PTHdr = [Dia, Casos_Totales, Tasa_Ataque];
MADistr_PTHdr = [Dia, Muertes_Totales, Tasa_Mortalidad];

# Fields to be erased from raw tables
EraseFieldsCADistr20 = [Porcentaje];
EraseFieldsCADistr21 = [Porcentaje];

# ExtractPDFText and DetectPDFText Constants
WindowWidth = 1760;
WindowHeight = 990;
DatosResumen = 2;
PADepto_RTRows = 26;
CADepto_RTRows = 26;
CPEdades_RTRows = 5;
MADepto_RTRows = 26;
MADeptoSM_RTRows = 26;
CADistr20P1_RTRows = 22;
CADistr20P2_RTRows = 22;
CADistr21P1_RTRows = 22;
CADistr21P2_RTRows = 22;
MADistrP1_RTRows = 22;
MADistrP2_RTRows = 22;
PADepto_RTCols = 5;
CADepto_RTCols = 5;
CPEdades_RTCols = 4;
MADepto_RTCols = 3;
CADistr20P1_RTCols = 3;
CADistr20P2_RTCols = 3;
CADistr21P1_RTCols = 3;
CADistr21P2_RTCols = 3;
MADistrP1_RTCols = 3;
MADistrP2_RTCols = 3;