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
def basic_io_2():
    clear()
    print("at line 200")
    A=input("Pick a number: ")
    print(A)
    if A==A:
        print("TRUE")
    elif A!=A:
        print("FALSE")
    print()
    input("Press ENTER to continue ")
def element_choice():
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
    if choice == 0:
        exit("Ended")
    elif choice == 1:
        gosub_return_pop_emulation_1()
    elif choice == 2:
        pass
    elif choice == 2:
        basic_io_2()
    elif choice == 3:
        pass
    elif choice == 4:
        guess_my_number_4()
    elif choice == 5:
        pass
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
    else:
        exit()
while True:
    element_choice()
    clear()