from poblacion import *
def test_lee_poblaciones(fichero: str) -> list[RegistroPoblacion]:
    print("Probando lee_poblaciones()...")

    poblaciones = lee_poblaciones(fichero)
    
    print(f"Se han leído {len(poblaciones)} datos")
    print(f"Los tres primeros son {poblaciones[:3]}")
    print(f"Los tres últimos son {poblaciones[-3:]}")

def test_calcula_paises(poblaciones: list[RegistroPoblacion]) -> None:
    print("Probando calcula_paises()...")

    paises = calcula_paises(poblaciones)
    print(f"Se tienen {len(paises)} paises")
    print(f"Los 10 primeros paises son {paises[:10]}")
    print(f"Los 10 últimos paises son {paises[-10:]}")

def test_filtra_por_pais(poblaciones:list[RegistroPoblacion], nombre_o_codigo: str) -> None:
    print("Probando filtra_por_pais()...")

    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(f"El país tiene {len(datos)} datos")
    print(f"Los 5 primeros datos son {datos[:5]}")
    print(f"Los 5 últimos datos son {datos[-5:]}")
    
def test_filtra_por_paises_y_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> None:
    print("Probando filtra_por_paises_y_anyo()...")

    datos = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    print(f"Se han encontrado {len(datos)} datos")
    print(f"Los 5 primeros son {datos[:5]}")
    print(f"Los 5 últimos son {datos[-5:]}")

def test_muestra_evolucion_poblacion(poblaciones: list[RegistroPoblacion], nombre_o_codigo: str) -> None:
    print("Probando muestra_evolucion_poblacion()...")
    muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)

def test_muestra_comparativa_paises_anyo(poblaciones: list[RegistroPoblacion], anyo: int, paises: set[str]) -> None:
    print("Probando muestra_comparativa_paises_anyo()...")
    muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

if __name__ == '__main__':
    # poblaciones = test_lee_poblaciones('data/population.csv')
    poblaciones = lee_poblaciones('data/population.csv')

    # test_calcula_paises(poblaciones)
    # test_filtra_por_pais(poblaciones, "EUU")
    # test_filtra_por_paises_y_anyo(poblaciones, 1970, {"Latin America & Caribbean", "European Union", "East Asia & Pacific (IDA & IBRD countries)"})
    # test_muestra_evolucion_poblacion(poblaciones, "EUU")
    test_muestra_comparativa_paises_anyo(poblaciones, 1970, {"Latin America & Caribbean", "European Union", "East Asia & Pacific (IDA & IBRD countries)"})
