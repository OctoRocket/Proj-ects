import time
x = 0
a = 0
while True:
    print(x)
    b = x
    if x == 0:
        x = 1
    elif a == 0:
        a = 1
    elif a == 1:
        y = x
        z = b
        x = y + z
    time.sleep(0.5)