import random

def randomNumbers():
    value = ""
    for x in range(4):
        res = random.randint(0, 1)
        value += str(res)

    return int(value, 2)

print(randomNumbers())
