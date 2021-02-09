print("""You enter a dark room with two doors.
Do you go through door #1, door #2, or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your lefs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your etes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You stumble into your highschool math class, late for a test.")
    print("What do you do?")
    print("1. Start taking the test.")
    print("2. Leave, definetly not worth it.")

    decision = input("> ")

    if decision == "1":
        print("Yay you got a 94%, not bad not bad.")
    elif decision == "2":
        print("You go and get some food instead.")
    else:
        print(f"You {decision} instead.")

else:
    print("You stumble around and fall on a knife and die.  Good job!")
