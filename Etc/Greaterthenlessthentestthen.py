import random
x = random.randint(1,100)
y = random.randint(1,100)
z = random.randint(1,100)
while True:
    if x < y > z:
        print("x:", x, "y:", y, "z:", z)
        print("True")
        input()
        exit()
