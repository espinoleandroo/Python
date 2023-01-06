user_option = input("piedra, papel o tijera => ")
computer_option = "tijera"

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