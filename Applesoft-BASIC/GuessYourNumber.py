import random
min_guess = 1
max_guess = 100
while True:
    try:
        number = int(input("Pick a number from 1 to 100, then press Enter: "))
    except ValueError:
        print("?REENTER")
    while True:
        guess=random.randint(min_guess,max_guess)
        print("I guessed:",guess)
        response = input("Enter 1 for too high, -1 for too low, and 0 for got it ")
        if response == "1":
            max_guess = guess-1
            print("ok")
        elif response == "-1":
            min_guess = guess+1
            print("ok")
        elif response == "0":
            print("Yay!")
            input("Press ENTER")
            exit("Won")