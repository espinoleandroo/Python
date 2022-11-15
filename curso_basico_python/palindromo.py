def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if(es_palindromo):
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__":
    main()


