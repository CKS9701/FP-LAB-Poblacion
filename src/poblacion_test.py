from poblacion import *
def test_lee_poblaciones(fichero: str) -> list[RegistroPoblacion]:
    print("Probando lee_poblaciones()...")

    poblaciones = lee_poblaciones(fichero)
    
    print(f"Se han leído {len(poblaciones)} datos")
    print(f"Los tres primeros son {poblaciones[:3]}")
    print(f"Los tres últimos son {poblaciones[-3:]}")






if __name__ == '__main__':
    poblaciones = test_lee_poblaciones('../data/population.csv')