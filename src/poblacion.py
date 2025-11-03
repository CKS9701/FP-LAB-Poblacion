import csv

from collections import namedtuple
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

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
    
