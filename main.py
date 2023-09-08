print("2.1")
name = str(input("what is your name: "))
print("hello",name,"!")

print("2.2")
import math
radius = float(input("what is the radius of the circle: "))
pi = math.pi
area = radius*(pi**2)
print(f"the area of circle is: {area:.2f}")

print("2.3")
length = float(input("length of rectangle: "))
width = float(input("width of rectangle: "))
perimeter = 2*(length+width)
area = length*width
print(f"perimeter of rectangle is: {perimeter:.2f} \narea of rectangle is:{area:.2f}")

print("2.4")
a, b, c = (int(a) for a in input("enter 3 intergers: ").split())
sum = a+b+c
product = a*b*c
average = sum/3
print(f"Sum is {sum} \nProduct is {product} \nAverage is {average:.2f}")

print("2.5")
talent = float(input("how many talents: "))
pound = float(input("how many pounds: "))
lot = float(input("how many lots: "))
total = talent*20*32*13.3 + pound*32*13.3 + lot*13.3
kilo = total//1000
gram= total%1000
print(f"the weight in modern units is: {kilo:.2f} kilograms and {gram:.2f} grams")

print("2.6")
import random
mylist = (0,1,2,3,4,5,6,7,8,9)
print("3 digit code is: ",random.choice(mylist),random.choice(mylist),random.choice(mylist))
mylist = (1,2,3,4,5,6)
print("4 digit code is: ",random.choice(mylist),random.choice(mylist),random.choice(mylist),random.choice(mylist))

print("3 digit code is: ",random.randint(0,9),random.randint(0,9),random.randint(0,9))
print("4 digit code is: ",random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))

print("3.1")
l = float(input("Length of zander in centimeters: "))
n = 42 - l
if l >= 42:
    print("The fish has fulfilled the size limit.")
else:
    print(f"The fish needs to be {n:.2f} centimeters bigger, please release it back to the lake.")

print("3.2")
c = input("Please enter the cabin class of the cruise ship: ")
if c == "LUX":
    print("You have the upper-deck cabin with a balcony.")
elif c == "A":
    print("You have the above the car deck, equipped with a window.")
elif c == "B":
    print("You have the windowless cabin above the car deck.")
elif c == "C":
    print("You have the windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

print("3.3")
g = input("Provide your gender male/female: ")
h = float(input("Provide your hemoglobin value g/l: "))
if (g == "female" and 117 < h < 155) or (g == "male" and 134 < h < 167):
    print("Your hemoglobin value is normal.")
elif (g == "female" and h < 117) or (g == "male" and h < 134):
    print("Your hemoglobin value is low.")
elif (g == "female" and h > 155) or (g == "male" and h > 167):
    print("Your hemoblogin value is high.")
else:
    print("Not applicable.")

print("3.4")
y = int(input("Please enter a year: "))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")

print("4.1")
i = 1
while i<=1000:
    if i%3 == 0:
        print(i)
    i = i + 1

print("4.2")
while True:
    inch = float(input("how many inches: "))
    if inch<0:
        break
    cen = 2.54*inch
    print(f"{inch:.2f} inch equals to {cen:.2f} centimeters.")
print("Program ends.")

print("4.3")
no = input("enter a number: ")
largest = float(no)
smallest = float(no)
while no != "":
    no = float(no)
    if no > largest:
        largest = no
    if no < smallest:
        smallest = no
    no = input("enter a number: ")
print(f"the largest number is: {largest:.2f}\nthe smallest number is: {smallest:.2f}")

print("4.4")
import random
no = random.randint(1,10)
guess = int(input("guess the number from 1 to 10: "))
while guess != no:
    if guess < no:
        print("too low.")
    elif guess > no:
        print("too high")
    guess = int(input("guess again: "))
print("correct!")

print("4.5")
n = 1
while True:
    u1 = input("enter username: ")
    p1 = input("enter password: ")
    if u1 == "python" and p1 == "rules":
        print("welcome")
        break
    if n <= 4:
        print("try again")
    if n > 4:
        print("access denied")
        break
    else:
        n = n + 1

print("4.6")
import random
d = int(input("how many dots: "))
cp = 0
sp = 0
for i in range(d):
    randx = random.uniform(-1,1)
    randy = random.uniform(-1,1)
    distant = randx**2 + randy**2
    if distant <=1:
        cp = cp + 1
    sp = sp + 1
    pi = 4*cp/sp
print("The estimated value of pi is: ",pi)

print("4.6")
import random
d = int(input("how many dots: "))
cp = 0
sp = 0
d1 = 0
while d1 < d:
    randx = random.uniform(-1,1)
    randy = random.uniform(-1,1)
    distant = randx**2 + randy**2
    if distant <=1:
        cp = cp + 1
    d1 = d1 + 1
    sp = sp + 1
    pi = 4*cp/sp
print("The estimated value of pi is: ",pi)

print("5.1")
import random
rolls = []
roll = int(input("how many rolls: "))

for i in range(roll):
    n = random.randint(1,6)
    rolls.append(n)
print("the rolls in order are: ",rolls)
print("the sum of rolls are:",sum(rolls))

print("5.2")
no = input("enter a number: ")
list =[]
while True:
    if no == "":
        break
    no = float(no)
    list.append(no)
    no = input("enter a number: ")
reverse = sorted(list, reverse=True)
print("top 5 biggest numbers are: ",reverse[:5])

print("5.3")
no = int(input("enter an interger: "))
o = 0
for i in range(1,no):
    if no%i==0:
        o=o+1
    else:
        o = o
if o == 1:
    print("this is a prime number")
else:
    print("this is not a prime number")

print("5.4")
cities = []
city = input("add a city name: ")
for i in range(1,5):
    cities.append(city)
    city = input("add a city name: ")
cities.append(city)
print(cities)
for index,i in enumerate(cities, start=1):
    print(f"{index}. {i}")

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














