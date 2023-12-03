print("7.1")
seasons = ("spring","summer","autumn","winter")
month = input("Enter month number: ")
if month in ["12","1","2"]:
    print(f"Month {month} is in {seasons[3]}")
elif month in ["3","4","5"]:
    print(f"Month {month} is in {seasons[0]}")
elif month in ["6","7","8"]:
    print(f"Month {month} is in {seasons[1]}")
elif month in ["9","10","11"]:
    print(f"Month {month} is in {seasons[2]}")
else:
    print("Not a month")

print("7.2")
list = set()
name = input("give a name: ")
while name != "":
    if name in list:
        print("existing name")
    if not name in list:
        print("new name")
        list.add(name)
    name = input("give a name:")
print("list of names is: ")
for n, i in enumerate(list,start=1):
    print(f"{n}. {i}")

print("7.3")
list = {}
command = input("to add, type 1. to retrieve, type 2. to quit, type 3: ")
while command != "3":
    if command == "1":
        code = input("code of airport: ")
        name = input("name of airport: ")
        list[code]=name
        print("information has been added")
    if command == "2":
        c = input("whats the code: ")
        if not c in list:
            print("code is not found")
        else:
            print(f"{c} is {list[c]} airport")
    print(f"current list is {list}")
    command = input("to add, type 1. to retrieve, type 2. to quit, type 3: ")
print("program ends")