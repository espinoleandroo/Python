import random

options = ("piedra", "papel", "tijera")

user_option = input("piedra, papel o tijera => ")

if not user_option in options:
    print("Opcion invalida")
else :
    user_option = user_option.lower()
    computer_option = random.choice(options)

    print("User option => ", user_option)
    print("Computer option => ", computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("User gano!")
        else:
            print("Computer gano!")
    elif user_option == "papel":
        if computer_option == "piedra":
            print("User gano!")
        else:
            print("Computer gano!")
    elif user_option == "tijera":
        if computer_option == "papel":
            print("User gano!")
        else:
            print("Computer gano!")