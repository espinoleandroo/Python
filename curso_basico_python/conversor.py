menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos

Elige la opción:
"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuandos pesos mexicanos tienes? ")
    pesos = float(pesos)
    valor_dolar = 20.35
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = input("¿Cuandos pesos argentinos tienes? ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = input("¿Cuandos pesos colombianos tienes? ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print("Ingresa una opción correcta por favor")

