import random
def roll():
    r = random.randint(1,6)
    return r
r = roll()
while r != 6:
    print(r)
    r = roll()
print(r)