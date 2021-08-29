import random

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
        exit()
    total_coins = computer_turn(total_coins)
    total_coins = win_check_computer(total_coins)
    if total_coins == 0:
        exit()