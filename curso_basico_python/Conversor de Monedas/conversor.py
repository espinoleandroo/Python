pesos = input("¿Cuandos pesos mexicanos tienes? ")
pesos = float(pesos)
valor_dolar = 20.35
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")