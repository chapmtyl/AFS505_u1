from sys import exit

def boring():
    print("I don't know what that means")
    exit(0)


def contestant():
    print("WHoever guesses the closest wins the car")
    print("Contestant 1: $1200")
    print("Contestant 2: $35000")
    print("Contestant 3: $35001")
    print("What is your guess?")

    num = input("> $")
    if "0" in num or "1" in num:
        guess = int(num)
    else:
        print("Try again with only numbers please(No comas).")
        exit(0)
    if guess < 35001:
        print("The price is 74399!")
        leave("Contestant 3 wins!")
    else:
        leave("Congrats, you won!!!")


def no():
    leave("Cars are overrated anyways")


def leave(x):
    print(x, "Thanks for playing!")
    exit(0)

def start():
    print("Congrats!")
    print("You are a contestant on the price is right!.")
    print("Before you is a brand new car!")
    print("Do you want a chance to win?")

    choice = input("> ")

    if choice == "Yes" or "yes":
        contestant()
    elif choice == "No" or "no":
        No()
    else:
        boring("You stumble around the room until you starve.")


start()
