import csv

from collections import namedtuple
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

from matplotlib import pyplot as plt

import math

def lee_poblaciones(fichero: str) -> list[RegistroPoblacion]:
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Saltar la cabecera
        poblaciones = []
        for pais, codigo, anyo, censo in lector:
            anyo = int(anyo)
            censo = int(censo)
            poblaciones.append(RegistroPoblacion(pais, codigo, anyo, censo))

        return poblaciones
    
def calcula_paises(poblaciones: list[RegistroPoblacion]) -> list[str]:
    paises = set()
    for x in poblaciones:
        paises.add(x.pais)

    return sorted(paises)

def filtra_por_pais(poblaciones:list[RegistroPoblacion], nombre_o_codigo: str) -> list[tuple]:
    ret = []
    for x in poblaciones:
        if nombre_o_codigo == x.pais or nombre_o_codigo == x.codigo:
            ret.append((x.año, x.censo))

    return ret

def filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> list[tuple]:
    ret = []
    for x in poblaciones:
        if x.pais in paises and x.año == anyo:
            ret.append((x.pais, x.censo))

    return ret

def muestra_evolucion_poblacion(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> None:
    lista_anyos = []
    lista_habitantes = []
    for x in poblaciones:
        if x.pais == nombre_o_codigo or x.codigo == nombre_o_codigo:
            lista_anyos.append(x.año)
            lista_habitantes.append(x.censo)
            nombre_pais = x.pais

    plt.title(f"Evolucion de la poblacion de {nombre_pais}")
    plt.plot(lista_anyos, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> None:
    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    lista_paises = []
    lista_habitantes = []
    for x in datos:
        lista_paises.append(x[0])
        lista_habitantes.append(x[1])

    plt.title(f"Población en el año {anyo}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()

def pais_menos_poblacion(poblaciones:list[RegistroPoblacion], anyo: int) -> str:
    poblacion = math.inf
    for x in poblaciones:
        if x.año == anyo:
            if poblacion > x.censo:
                poblacion = x.censo
                pais = x.pais

    return pais

def paises_mas_poblacion(poblaciones: list[RegistroPoblacion], anyo: int) -> list[str]:
    paises = filtra_por_paises_y_anyo(poblaciones, anyo, set(calcula_paises(poblaciones)))
    paises = [(pob, p) for (p, pob) in paises]
    paises.sort(reverse=True)
    ret = [paises[0][1], paises[1][1], paises[2][1]]
    return ret

def paises_superan_poblacion(poblaciones: list[RegistroPoblacion], minimo: int) -> list[str]:
    ret = set()
    for x in poblaciones:
        if x.censo >= minimo:
            ret.add(x.pais)

    return sorted(ret)
