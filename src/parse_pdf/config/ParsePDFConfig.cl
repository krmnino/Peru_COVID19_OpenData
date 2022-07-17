# Top Level Paths
WindowsTopLevel = C:/Users/kurt_/github/Peru_COVID19_Stats/;
LinuxTopLevel = /home/kurt/remote/github/Peru_COVID_Stats/;

# Paths to raw tables
PADepto_RT = res/raw_tables/PruebasAcumuladoDepto.csv;
CADepto_RT = res/raw_tables/CasosAcumuladoDepto.csv;
CPEdades_RT = res/raw_tables/CasosPositivosEdades.csv;
MADepto_RT = res/raw_tables/MuertesAcumuladoDepto.csv;
MADeptoSM_RT = res/raw_tables/MuertesAcumuladoDeptoSM.csv;
CADistr20P1_RT = res/raw_tables/CasosAcumuladoDistrito2020P1.csv;
CADistr20P2_RT = res/raw_tables/CasosAcumuladoDistrito2020P2.csv;
CADistr21P1_RT = res/raw_tables/CasosAcumuladoDistrito2021P1.csv;
CADistr21P2_RT = res/raw_tables/CasosAcumuladoDistrito2021P2.csv;
MADistrP1_RT = res/raw_tables/MuertesAcumuladoDistritoP1.csv;
MADistrP2_RT = res/raw_tables/MuertesAcumuladoDistritoP2.csv;

# Paths to directories
PADepto_Dir = data/PruebasAcumuladasDepto/;
CADepto_Dir = data/CasosAcumuladosDepto/;
CPEdades_PTF = data/CasosPositivosEdades/CasosPositivosEdades.csv;
MADepto_Dir = data/MuertesAcumuladasDepto/;
MADeptoSM_Dir = data/MuertesAcumuladasDepto_SINADEF-MINSA/;
CADistr20_Dir = data/CasosAcumuDistrito2020/;
CADistr21_Dir = data/CasosAcumuDistrito2021/;
MADistr_Dir = data/MuertesAcumulaDistrito/;

# PDF Area config file
AreasPDFCL = src/parse_pdf/config/AreasPDF.cl;

# Config files with information about departments and districts
DepartmentsAreas = res/config_files/DepartmentsAreas.cl;
DepartmentsIndex = res/config_files/DepartmentsIndex.cl;
DepartmentsMacroregions = res/config_files/DepartmentsMacroregions.cl;
DepartmentsPopulation = res/config_files/DepartmentsPopulation.cl;
DistrictsIndex = res/config_files/DistrictsIndex.cl;
DistrictsZones = res/config_files/DistrictsZones.cl;
AgeGroupsIndex = res/config_files/AgeGroupsIndex.cl;

# Headers for processing raw rables
PADepto_RTHdr = [Depto, PCR, PR, AG, Total];
CADepto_RTHdr = [Depto, PCR, PR, AG, Total];
CPEdades_RTHdr = [Grupo, Total, Tasa_Ataque, Razon_Tasas];
MADepto_RTHdr = [Depto, Muertes_Total, Muertes_Dia];
MADeptoSM_RTHdr = [Depto, Muertes_Conf, Muertes_Sosp, Total_Muertes_SisVig, Muertes_SINADEF];
CADistr20P1_RTHdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CADistr20P2_RTHdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CADistr21P1_RTHdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
CADistr21P2_RTHdr = [Distrito, Casos_Totales, Porcentaje, Tasa_Ataque];
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
CADistr20_EraseFields = [Porcentaje];
CADistr21_EraseFields = [Porcentaje];

# Global Constants
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

PADepto_PDFPage = 3;
CADepto_PDFPage = 3;
CPEdades_PDFPage = 14;
MADepto_PDFPage = 22;
CADistr20P1_PDFPage = 77;
CADistr20P2_PDFPage = 77;
CADistr21P1_PDFPage = 78;
CADistr21P2_PDFPage = 78;
MADistrP1_PDFPage = 81;
MADistrP2_PDFPage = 81;