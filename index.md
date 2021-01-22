---
layout: default
---
<br/>
## ¿Que es esto?

Este proyecto empezo como un simple programa para graficar el numero de casos de coronavirus en Peru. Actualmente el principal objetivo es preservar y extrapolar los datos publicados por el [Ministerio de Salud del Peru en Twitter](https://twitter.com/Minsa_Peru) acerca de la pandemia del COVID-19. Los datos estan disponibles de manera **gratuita** y **segura**.

* * *

## Descargas

* [Formato .csv simple](https://raw.githubusercontent.com/krmnino/Peru_COVID19_OpenData/master/data/PER_data.csv)
* [Formato .csv completo](https://raw.githubusercontent.com/krmnino/Peru_COVID19_OpenData/master/data/PER_full_data.csv)
* [Formato .json simple](https://raw.githubusercontent.com/krmnino/Peru_COVID19_OpenData/master/data/PER_data.json)
* [Formato .json completo](https://raw.githubusercontent.com/krmnino/Peru_COVID19_OpenData/master/data/PER_full_data.json)

* * *

## Formato de Datos

Datos disponibles en **.csv** y **.json**.

### PER_data.csv (Usando Excel u OpenOffice Calc)

| Columna      | Nombre                    | Tipo    | Descripcion                                                |
|:-------------|:--------------------------|:--------|:-----------------------------------------------------------|
| A            | Date                      | string  | Año-Mes-Dia de la estadistica                              |
| B            | Cases                     | int     | Numero de casos confirmados acumulado a la fecha           |
| C            | Deaths                    | int     | Numero de fallecidos a la fecha                            |
| D            | Tests                     | int     | Numero de pruebas (PM + PR) a la fecha                     |
| E            | Recovered                 | int     | Numero de personas recuperadas a la fecha                  |
| F            | Hospitalized              | int     | Numero de personas hospitalizadas a la fecha               |

### PER_full_data.csv (Usando Excel u OpenOffice Calc)

| Columna      | Nombre                    | Tipo    | Descripcion                                                |
|:-------------|:--------------------------|:--------|:-----------------------------------------------------------|
| A            | Fecha                     | string  | Año-Mes-Dia de la estadistica                              |
| B            | Dia                       | int     | Indice del dia                                             |
| C            | Casos                     | int     | Numero de casos confirmados acumulado a la fecha           |
| D            | NuevosCasos               | int     | Incremento de casos confirmados añadidos a la fecha        |
| E            | %DifCases                 | float   | Tasa de crecimiento de casos confirmados a la fecha        |
| F            | CasosActivos              | int     | Numero de casos activos a la fecha                         |
| G            | NuevosCasesActivos        | int     | Diferencia de casos activos a la fecha                     |
| H            | Fallecidos                | int     | Numero de fallecidos a la fecha                            |
| I            | NuevosFallecidos          | int     | Incremento de fallecidos a la fecha                        |
| J            | %DifFallecidos            | float   | Tasa de crecimiento de fallecidos a la fecha               |
| K            | TasaLetalidad             | float   | Tasa de letalidad acumulada                                |
| L            | Pruebas                   | int     | Numero de pruebas (PM + PR) a la fecha                     |
| M            | NuevasPruebas             | int     | Incremento de pruebas (PM + PR) añadidas a la fecha        |
| N            | %DifTests                 | float   | Tasa de crecimiento de pruebas (PM + PR) a la fecha        |
| O            | %PruebasPositivasDiarias  | float   | Positividad diaria de pruebas (PM + PR)                    |
| P            | Recuperados               | int     | Numero de personas recuperadas a la fecha                  |
| Q            | NuevosRecuperados         | int     | Incremento de personas recuperadas a la fecha              |
| R            | %DifRecuperados           | float   | Tasa de crecimiento de personas recuperadas a la fecha     |
| S            | Hospitalizados            | int     | Numero de personas hospitalizadas a la fecha               |
| T            | NuevosHospitalizados      | int     | Diferencia de personas hospitalizadas a la fecha           |
| U            | %DiffHospitalized         | float   | Tasa de crecimiento de personas hospitalizadas a la fecha  |

### PER_data.json

| Indice       | Nombre                    | Tipo    | Descripcion                                                |
|:-------------|:--------------------------|:--------|:-----------------------------------------------------------|
| A            | Date                      | string  | Año-Mes-Dia de la estadistica                              |
| B            | Cases                     | int     | Numero de casos confirmados acumulado a la fecha           |
| C            | Deaths                    | int     | Numero de fallecidos a la fecha                            |
| D            | Tests                     | int     | Numero de pruebas (PM + PR) a la fecha                     |
| E            | Recovered                 | int     | Numero de personas recuperadas a la fecha                  |
| F            | Hospitalized              | int     | Numero de personas hospitalizadas a la fecha               |

### PER_full_data.json

| Columna      | Nombre                    | Tipo    | Descripcion                                                |
|:-------------|:--------------------------|:--------|:-----------------------------------------------------------|
| A            | Fecha                     | string  | Año-Mes-Dia de la estadistica                              |
| B            | Dia                       | number  | Indice del dia                                             |
| C            | Casos                     | number  | Numero de casos confirmados acumulado a la fecha           |
| D            | NuevosCasos               | number  | Incremento de casos confirmados añadidos a la fecha        |
| E            | %DifCases                 | number  | Tasa de crecimiento de casos confirmados a la fecha        |
| F            | CasosActivos              | number  | Numero de casos activos a la fecha                         |
| G            | NuevosCasesActivos        | number  | Diferencia de casos activos a la fecha                     |
| H            | Fallecidos                | number  | Numero de fallecidos a la fecha                            |
| I            | NuevosFallecidos          | number  | Incremento de fallecidos a la fecha                        |
| J            | %DifFallecidos            | number  | Tasa de crecimiento de fallecidos a la fecha               |
| K            | TasaLetalidad             | number  | Tasa de letalidad acumulada                                |
| L            | Pruebas                   | number  | Numero de pruebas (PM + PR) a la fecha                     |
| M            | NuevasPruebas             | number  | Incremento de pruebas (PM + PR) añadidas a la fecha        |
| N            | %DifTests                 | number  | Tasa de crecimiento de pruebas (PM + PR) a la fecha        |
| O            | %PruebasPositivasDiarias  | number  | Positividad diaria de pruebas (PM + PR)                    |
| P            | Recuperados               | number  | Numero de personas recuperadas a la fecha                  |
| Q            | NuevosRecuperados         | number  | Incremento de personas recuperadas a la fecha              |
| R            | %DifRecuperados           | number  | Tasa de crecimiento de personas recuperadas a la fecha     |
| S            | Hospitalizados            | number  | Numero de personas hospitalizadas a la fecha               |
| T            | NuevosHospitalizados      | number  | Diferencia de personas hospitalizadas a la fecha           |
| U            | %DiffHospitalized         | number  | Tasa de crecimiento de personas hospitalizadas a la fecha  |

## Contacto y Sugerencias

¡Sugerencias y reportes de errores son bienvenidos! Mi informacion de contacto es la siguiente:

<dd> Kurt Manrique-Nino </dd>
<dd> Email: kurt.manrique.n@gmail.com </dd>
<dd> <a href="https://twitter.com/krm_nino">Twitter</a> </dd>
<dd> <a href="https://www.linkedin.com/in/kurt-manrique-nino/">LinkedIn</a> </dd>
<dd> <a href="https://github.com/krmnino/">GitHub</a></dd>
<dd> New York, U.S.A. </dd>

