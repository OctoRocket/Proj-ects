import os
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
def madlibs():
    Name = input("Name: ")
    Verb = input("Verb: ")
    Noun = input("Noun: ")
    Place = input("Place: ")
    print("One day,", Name, Verb, "to", Place, "to see the", Noun)
    print("Press enter to end the program")
    input()
def element_choice():
    print("(0) Exit program")
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
    choice = input("Enter option")
    if choice == 0:
        exit("Ended")
    elif choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
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
        pass
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
while True:
    element_choice()
    clear()