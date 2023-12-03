print("6.1")
import random
def roll():
    r = random.randint(1,6)
    return r
r = roll()
while r != 6:
    print(r)
    r = roll()
print(r)

print("6.2")
import random
def roll(no):
    r = random.randint(1,no)
    return r
s = int(input("number of sides: "))
r = roll(s)
while r != s:
    print(r)
    r = roll(s)
print(r)

print("6.3")
def conv(g):
    l = 3.785*g
    return l
g = float(input("how many gallons: "))
while g > 0:
    l = conv(g)
    print(f"amount of liters is: {l:.2f}")
    g = float(input("how many gallons: "))
print("ends")

print("6.4")
def all(nos):
    total = 0
    for i in nos:
        total += i
    return total
list = (int(i) for i in input("enter interger numbers: ").split())
print("sum of all numbers is: ",all(list))

print("6.5")
def div(nos):
    even = []
    for i in nos:
        if i%2==0:
            even.append(i)
    return even
list = [int(i) for i in input("enter interger numbers: ").split()]
print("the original list is: ",list)
print("the reduced list is: ",div(list))

print("6.6")
import math
def com(size,price):
    area = 0.5*size*size*math.pi/10000
    rate = price/area
    return rate
a, b = (int(a) for a in input("enter first pizza diamenter in cm and price in euro: ").split())
c, d = (int(a) for a in input("enter second pizza diamenter in cm and price in euro: ").split())
rate1 = com(a,b)
rate2 = com(c,d)
print(f"first pizza price per square meter: {rate1:.2f}")
print(f"second pizza price per square meter: {rate2:.2f}")
if rate1 > rate2:
    print("second pizza provides better value for money")
else:
    print("first pizza provides better value for money")
