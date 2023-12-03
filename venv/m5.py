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