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
