import random

def main():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if(numero_elegido < numero_aleatorio):
            print("Busca un numero mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_elegido = int(input("Elige un numero del 1 al 100: "))
    print("Ganaste")


if __name__ == "__main__":
    main()