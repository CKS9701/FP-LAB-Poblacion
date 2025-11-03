import csv

from collections import namedtuple
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

from matplotlib import pyplot as plt

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