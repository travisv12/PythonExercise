("2.1")
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
