def main():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3    
    }

    print(mi_diccionario)

    poblacion_paises = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }
    
    print("Keys")
    for pais in poblacion_paises.keys():
        print(pais)
    
    print("Values")
    for pais in poblacion_paises.values():
        print(pais)

    print("Values")
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    main()
