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

if __name__ == '__main__':
    # poblaciones = test_lee_poblaciones('data/population.csv')
    poblaciones = lee_poblaciones('data/population.csv')

    # test_calcula_paises(poblaciones)