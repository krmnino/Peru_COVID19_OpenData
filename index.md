---
layout: default
---

## ¿Que es esto?

Este proyecto empezo como un simple programa para graficar el numero de casos de coronavirus en Peru. Actualmente el principal objetivo es preservar y extrapolar los datos publicados por el Ministerio de Salud del Peru acerca del la pandemia del COVID-19. Los datos estan disponibles de manera gratuita y segura.

## Formato de Datos

Datos disponibles en .csv y .json.

* PER_data.csv (Usando Excel u OpenOffice Calc)

| Columna      | Nombre                    | Tipo    | Descripcion                                                |
|:-------------|:--------------------------|:--------|:-----------------------------------------------------------|
| A            | Fecha                     | string  | Año-Mes-Dia de la estadistica                              |
| B            | Casos                     | int     | Numero de casos confirmados acumulado a la fecha           |
| C            | Deaths                    | int     | Numero de fallecidos a la fecha                            |
| D            | Tests                     | int     | Numero de pruebas (PM + PR) a la fecha                     |
| E            | Recovered                 | int     | Numero de personas recuperadas a la fecha                  |
| F            | Hospitalized              | int     | Numero de personas hospitalizadas a la fecha               |

* PER_full_data.csv (Usando Excel u OpenOffice Calc)

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
| K            | TasaMortalidad            | float   | Tasa de moratlidad acumulada                               |
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

* PER_data.json



* PER_full_data.json



## Change Log