import time
n1 = 0
n2 = 1
while True:
    print(n1)
    n1_plus_n2 = n1 + n2
    n1 = n2
    n2 = n1_plus_n2
    time.sleep(0.25)