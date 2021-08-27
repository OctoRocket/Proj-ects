import time
number_1 = 0
number_2 = 1
while True:
    print(number_1)
    number_1_plus_number_2 = number_1 + number_2
    number_1 = number_2
    number_2 = number_1_plus_number_2
    time.sleep(1)