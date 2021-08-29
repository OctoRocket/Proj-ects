import time
import random
import os
from time import sleep
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
def madlibs_10():
    clear()
    Name = input("Name: ")
    Verb = input("Verb: ")
    Noun = input("Noun: ")
    Place = input("Place: ")
    print("One day,", Name, Verb, "to", Place, "to see the", Noun)
    print("Press enter to end the program")
    input()
def guess_my_number_4():
    clear()
    print("GUESS MY NUMBER")
    print("I'm picking a number between 1 and 100...")
    sleep(0.5)
    x = random.randint(1,100)
    while True:
        print("Your guess?")
        while True:
            try:
                y = int(input())
                break
            except ValueError:
                print("Try again!")
        if y > x:
            print("Too high")
        elif y < x:
            print("Too low")
        elif y == x:
            print("Got it!")
            return("Won")
        else:
            print("?REENTER")
def guess_your_number_5():
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
                return("Won")
def gosub_return_pop_emulation_1():
    clear()
    print("#110 GOSUB 150")
    print("#110 #150 RETURN")
    print("#150 GOSUB 160")
    print("GOSUB 190")
    print("POP")
    print("RETURN")
    print()
    print("Press enter:")
    input()
def fibbonocci_3():
    n1 = 0
    n2 = 1
    while True:
        print(n1)
        n1_plus_n2 = n1 + n2
        n1 = n2
        n2 = n1_plus_n2
        time.sleep(0.15)
def basic_io_2():
    clear()
    print("at line 200")
    try:
        A = input("Pick a number: ")
    except ValueError:
        print("?REENTER")
    print(A)
    if A==A:
        print("TRUE")
    elif A!=A:
        print("FALSE")
    print()
    input("Press ENTER:")
def blackjack_secret_1():
    start_loop = True
    while start_loop:
        start = input("Do you want to play blackjack? (y/n)")
        if start == "n":
            return("start == n")
        elif start == "y":
            print("Ok!")
            time.sleep(0.2)
            start_loop = False
        else:
            print("Thats invalid!")
            time.sleep(0.2)
    computer_cards = random.randint(17, 24)  # The computers total
    cards_part_a = random.randint(1,10)  # 2 parts of the "cards" var, used to auto check for aces
    cards_part_b = random.randint(1,10) 
    if cards_part_a == 1:
        if cards_part_b + 11 <= 21:
            cards_part_a = 11
    if cards_part_b == 1:
        if cards_part_a + 11 <= 21:
            cards_part_b = 11
    cards = cards_part_a + cards_part_b
    win_or_lose = False  # Is the game over?
    print("You have:", cards)
    while win_or_lose == False:
        hit_or_stay = input("Hit or stay? (h/s)")
        if hit_or_stay == "h":
            cards = cards + random.randint(1,10)
            if cards > 21:
                print("You lose! You were:", cards - 21, "over 21!")
                win_or_lose = True  # The game finished
            print("You have:", cards)
        elif hit_or_stay == "s":
            if cards > 21:
                print("You lose! You were:", cards - 21, "over21!")
                win_or_lose = True
            elif computer_cards > 21:
                print("You win! The computer was", computer_cards - 21, "over 21!")
                win_or_lose = True
            elif cards > computer_cards:
                print("You win! Your number was:", cards-computer_cards, "over the computer's number!")
                win_or_lose = True
            elif cards < computer_cards:
                print("You lose! You number was:", computer_cards-cards, "under the computer's number!")
                win_or_lose = True
            elif cards == computer_cards:
                print("Draw! Your number and the computer's number were both:", cards)
                win_or_lose = True
        else:
            print("Invalid!")
    print("Ending...")
    input("Press any button to end...")
    return(0)
def nim_secret_2():
    total_coins = 12
    print("Starting coins:", total_coins)
    def player_turn(total_coins):
        while True:
            while True:
                try:
                    coins_to_take_away = int(input("How many coins would you like to take away? "))
                    break
                except ValueError:
                    print("Try again!")
            if coins_to_take_away > 3:
                print("That is too many!")
            elif coins_to_take_away < 1:
                print("That is too few!")
            elif coins_to_take_away > total_coins:
                print("You are trying to take away more coins then there are left!")
            else:
                total_coins = total_coins - coins_to_take_away
                break
        return(total_coins)
    def computer_turn(total_coins):
        if total_coins < 4:
            coins_to_take_away = total_coins
            total_coins = total_coins - coins_to_take_away
        else:
            coins_to_take_away = random.randint(1,3)
            total_coins = total_coins - coins_to_take_away
        print("The computer took away", coins_to_take_away, "coins!")
        return(total_coins)
    def win_check_player(total_coins):
        if total_coins == 0:
            print("The player wins!")
            return(0)
        else:
            print("There are", total_coins, "total coins left.")
            return(total_coins)
    def win_check_computer(total_coins):
        if total_coins == 0:
            print("The computer wins!")
            return(0)
        else:
            print("There are", total_coins, "total coins left.")
            return(total_coins)
    while True:
        total_coins = player_turn(total_coins)
        total_coins = win_check_player(total_coins)
        if total_coins == 0:
            return()
        total_coins = computer_turn(total_coins)
        total_coins = win_check_computer(total_coins)
        if total_coins == 0:
            return()
def guess_your_number_5():
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
            if guess == number:
                should_win = True
            else:
                should_win = False
            response = input("Enter 1 for too high, -1 for too low, and 0 for got it ")
            if response == "1":
                if should_win == True:
                    print("You lied! I guessed your number!")
                    sleep(1)
                    return(0)
                else:
                    max_guess = guess-1
                    print("ok")
            elif response == "-1":
                if should_win == True:
                    print("You lied! I guessed your number!")
                    sleep(1)
                    return(0)
                else:
                    min_guess = guess+1
                    print("ok")
            elif response == "0":
                print("Yay!")
                input("Press ENTER")
                return("Won")
def element_choice():
    secret = 0
    print("(1) GOSUB/RETURN/POP")
    print("(2) Basic I/O, IF/THEN")
    print("(3) Fibbonacci Sequence")
    print("(4) Guess my number")
    print("(5) Guess your number")
    print("(6) Approximate Pi")
    print("(7) Function tests")
    print("(8) Error tests")
    print("(9) Cellular automata")
    print("(10) Madlibs")
    print("(11) Lissajous Figures")
    print("(12) Screen Test")
    print("(13) DOS Sequential Access")
    print("(14) Lores Drawing with Joystick")
    print("(15) Lores Colors")
    print("(16) Mandelbrot Set")
    print("(17) Light Cycles")
    print("(18) Hires Demo")
    print("(19) DOS WRITE/APPEND")
    print("(20) ONERR ... RESUME")
    print("(21) CHR$ Tests")
    try:
        choice = int(input("Enter option: "))
    except ValueError:
        return(ValueError)
    print("You chose:", choice)
    if choice == -1:
        print("You have unlocked the bonus demos! These aren't in the origional demo but we have decided to add it anyway!")
        print("(1) blackjack")
        print("(2) Nim")
        try:
            choice = int(input("Enter option: "))
        except ValueError:
            return(ValueError)
        print("You chose:", choice)
        if choice == 1:
            blackjack_secret_1()
            choice = "secret"
            secret = 1
            return(0)
        if choice == 2:
            nim_secret_2()
            choice = "secret"
            return(0)
        else:
            exit()
    if choice == 0:
        exit("Ended")
    elif choice == 1:
        gosub_return_pop_emulation_1()
    elif choice == 2:
        basic_io_2()
    elif choice == 3:
        fibbonocci_3()
    elif choice == 4:
        guess_my_number_4()
    elif choice == 5:
        guess_your_number_5()
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
    elif choice == 9:
        pass
    elif choice == 10:
        madlibs_10()
    elif choice == 11:
        pass
    elif choice == 12:
        pass
    elif choice == 13:
        pass
    elif choice == 14:
        pass
    elif choice == 15:
        pass
    elif choice == 16:
        pass
    elif choice == 17:
        pass
    elif choice == 18:
        pass
    elif choice == 19:
        pass
    elif choice == 20:
        pass
    elif choice == 21:
        pass
    elif choice == "secret":
        print("you are sus")
        return(0)
    else:
        if secret == 1:
            print("seecart unlokned")
            time.sleep(0.05)
        exit()
while True:
    element_choice()
    clear()
