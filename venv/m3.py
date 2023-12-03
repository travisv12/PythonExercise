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