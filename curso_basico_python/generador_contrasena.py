import random

def generate_password():
    mayus = ["A", "B", "C", "D"]
    minus = ["a", "b", "c", "d"]
    simbols = ["!", "#", "$", "%"]
    numbers = ["1", "2", "3", "4"]
    
    characters =  mayus + minus + simbols + numbers
    
    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)
    
    return password


def main():
    password = generate_password()
    print("Your new password is: " + password)


if __name__ == "__main__":
    main()