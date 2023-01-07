import random

options = ("piedra", "papel", "tijera")

round = 1
user_wins = 0
computer_wins = 0

while True:

    print("* " * 10 )
    print("Round ", round )
    print("* " * 10 )
    print("computer", computer_wins )
    print("user", user_wins )
    print("* " * 10 )

    user_option = input("piedra, papel o tijera => ")
    round += 1
    
    if not user_option in options:
        print("Opcion invalida")
        continue
    user_option = user_option.lower()
    computer_option = random.choice(options)

    print("User option => ", user_option)
    print("Computer option => ", computer_option)

    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("User gano!")
            user_wins += 1
        else:
            print("Computer gano!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("User gano!")
            user_wins += 1
        else:
            print("Computer gano!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("User gano!")
            user_wins += 1
        else:
            print("Computer gano!")
            computer_wins += 1
    
    if computer_wins == 2:
        print("El ganador es la computadora")
        break
    if user_wins == 2:
        print("El ganador es el usuario")
        break

    round += 1