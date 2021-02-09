print("""Let's play a completely (not) fair game of rock paper scissors!""")
print("We'll go on shoot.")
print("Rock...")
print("Paper...")
print("Scissors...")
print("Shoot!")

result = input("> ")

if result == "Rock" or "rock":
    print("Paper")
    print("Ah I win, better luck next time.")

elif result == "Paper" or "paper":
    print("Rock")
    print("Oh you won!")
    print("See it is fair.")

elif result == "Scissors" or "scissors":
    print("Scissors")
    print("Oh it's a tie, try again.")

    secondround == input("> ")

    if secondround == "Rock" or "rock":
        print("Paper")
        print("Ah I win, better luck next time.")

    elif secondround == "Paper" or "paper":
        print("Scissors")
        print("Ah I win, better luck next time.")

    elif secondround == "Scissors" or "scissors":
        print("Rock")
        print("Ah I win, better luck next time.")

else:
    print("You're not playing this right...")
