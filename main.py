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

print("8.1")
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='travis',
    password='database123',
    autocommit=True
)

def getairport(code):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport: {row[0]},is located in {row[1]}.")
    return

code = input("enter airport code: ")
getairport(code)

print("8.2")
def getcountry(code):
    sql = "SELECT country.name FROM country"
    sql += " WHERE country.iso_country='" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The country {row[0]} has: ")
    return

def groupairport(code):
    sql = "SELECT type, count(*) FROM airport"
    sql += " WHERE airport.iso_country='" + code + "'"
    sql += " group by type order by type asc "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"{row[0]}: {row[1]} ")
    return

code = input("input country code: ")
getcountry(code)
groupairport(code)

print("8.3")
from geopy.distance import geodesic
def distance(a,b):
    dist=geodesic(a,b).kilometers
    return dist

def coor(code):
    sql = "select longitude_deg, latitude_deg from airport"
    sql += " where airport.ident = '" + code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            cord = (row[1],row[0])
    return cord
code1 = input("first airport code: ")
code2 = input("second airport code: ")
coor1 = coor(code1)
coor2 = coor(code2)
print("distance is: ",distance(coor1,coor2))

print("9.1 and 9.2 and 9.3 and 9.4 and 10.4 and 11.2")
import random
class Car:
    def __init__(self, registration_number:str, maximum_speed:int):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change:int):
        new_speed = self.current_speed + speed_change
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

    def __str__(self):
        return f"The car has:\nRegistration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"
#This part is for 11.2
class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity
        self.current_speed = 0
        self.travelled_distance = 0
class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume
        self.current_speed = 0
        self.travelled_distance = 0

electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)
electric_car.accelerate(100)
gasoline_car.accelerate(120)
electric_car.drive(3)
gasoline_car.drive(3)
print(electric_car.travelled_distance)
print(gasoline_car.travelled_distance)

#This part is for 10.4
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"Race: {self.name}")
        print("{:<10} {:<15} {:<15} {:<15}".format("Car", "Current Speed", "Distance", "Status"))
        for car in self.cars:
            print("{:<10} {:<15} {:<15} {:<15}".format(car.registration_number, car.current_speed, car.travelled_distance, "Finished" if car.travelled_distance >= self.distance else "In Progress"))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

if __name__ == "__main__":
    car_list = [Car(f"Car {i+1}", random.randint(100, 200)) for i in range(10)]

    race = Race("Grand Demolition Derby", 8000, car_list)

    hour = 1
    while not race.race_finished():
        if hour % 10 == 0:
            print("The race has lasted for",hour,"hours")
            race.print_status()
        race.hour_passes()
        hour += 1

    print("The race finished at",hour,"hours")
    race.print_status()
    
#This part is for 9.4
new_car = Car("ABC-123", 142)
print(new_car)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print("Current Speed after acceleration:", new_car.current_speed, "km/h")

new_car.accelerate(-200)

print("Final Speed after emergency brake:", new_car.current_speed, "km/h")

new_car.accelerate(60)

new_car.drive(1.5)

print(new_car)

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

race_finished = False
hour = 0
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

    for car in cars:
        if car.travelled_distance >= 10000:
            race_finished = True

    hour += 1

print("Car\t\tMaximum Speed\tCurrent Speed\tTravelled Distance")
for car in cars:
    print(f"{car.registration_number}\t{car.maximum_speed}\t\t\t\t{car.current_speed}\t\t\t\t{car.travelled_distance}")

print(f"The race finished after {hour} hours.")

print("10.1 and 10.2 and 10.3")
class Elevator:
    def __init__(self, bottom_floor:int, top_floor:int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self, target_floor:int):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Moving up to floor {self.current_floor}.")
        print(f"Elevator has reached floor {self.current_floor}")

    def floor_down(self, target_floor:int):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Moving down to floor {self.current_floor}.")
        print(f"Elevator has reached floor {self.current_floor}")

    def go_to_floor(self, target_floor:int):
        if target_floor < self.current_floor:
            self.floor_down(target_floor)
        elif target_floor > self.current_floor:
            self.floor_up(target_floor)
        else:
            print(f"Elevator is already on floor {target_floor}.")


elevator = Elevator(1,10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(1,num_elevators+1)]

    def run_elevator(self, elevator_num, destination_floor):
        if 0 <= elevator_num < len(self.elevators):
            elevator = self.elevators[elevator_num]
            print(f"The elevator number {elevator_num} is moving to floor {destination_floor}")
            elevator.go_to_floor(destination_floor)
        else:
            print(f"Elevator number {elevator_num} does not exist in this building.")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)
        print("All elevators have gone to bottom floor.")

building = Building(1,10, 3)

building.run_elevator(1, 7)
building.run_elevator(2, 2)

building.fire_alarm()

print("11.1")
class Publication:
    def __init__(self,name):
        self.name = name
    def print_info(self):
        pass
class Book(Publication):
    def __init__(self,name,page,author):
        self.page = page
        self.author = author
        super().__init__(name)
    def print_info(self):
        print(f"The book {self.name} has {self.page} pages and was written by {self.author}")
class Magazine(Publication):
    def __init__(self,name,editor):
        self.editor = editor
        super().__init__(name)
    def print_info(self):
        print(f"The magazine {self.name} was edited by {self.editor}")

magazine1 = Magazine("Donald Duck","Aki Hyyppa")
book1 = Book("Compartment No.6",192,"Rosa Liksom")
magazine1.print_info()
book1.print_info()

print("12.1 and 12.2")
import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

def changetemp(no:float):
    result = no - 273.15
    return result
location = input("Enter a location: ")
request = "https://api.openweathermap.org/data/2.5/weather?q=" + location +"&APPID=11ee7c722aa45c4592cb485d3fb2d9dd"
try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        kelvin = json_response["main"]["temp"]
        temperature = changetemp(kelvin)
        print(f"At the location {location}, the temperature is {temperature:.2f} Celcius")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

"""
import time
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='travis',
    password='database123',
    autocommit=True
)

from geopy.distance import geodesic

def story():
    while True:
        choice = input("Do you want to read a story? (yes/no): ").lower()

        if choice == 'yes':
            time.sleep(1)
            print("Once upon a time, there lives a world where everyone is living peacefully and thriving. ")
            time.sleep(1)
            print("Suddenly an airborne disease has quickly spread through Earth, threatened to destroy civilization.")
            time.sleep(1)
            print("Luckily scientists has built a safe zone in Helsinki Vantaa Airport that protects people from the deadly disease")
            time.sleep(1)
            print("You were rescued by a group of people from the safe zone, now it is your turn to do the same.")
            time.sleep(1)
            print("You were a pilot for Finnair before the disease, now you will fly to rescue people worldwide.")
            time.sleep(1)
            print("Your mission is to rescue 100 people from at least 5 countries.")
            time.sleep(1)
            print("You will get some money and fuel and you will earn more money by saving people along the way.")
            time.sleep(1)
            print("Remember to refuel before taking off and be mindful of the plane capacity.")
            time.sleep(1)
            print("If you rescue more than 150 people, the plane will crash.")
            time.sleep(1)
            print("Each airport has 20% chance of having robbers and 20% chance of having treasure chest.")
            time.sleep(1)
            print("Good luck and have fun!")
            break
        elif choice == 'no':
            print("Alright, maybe next time.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
def distance(a,b):
    dist=geodesic(a,b).kilometers
    return dist

def get_coordinate_by_name(name):
    sql = "select longitude_deg, latitude_deg from airport"
    sql += " where airport.name = '" + name + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            coord = (row[1],row[0])
    return coord

def get_coordinate_by_ident(username):
    sql = "select longitude_deg, latitude_deg from airport"
    sql += " where airport.ident = (select location from game where username ='" + username + "')"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            coord = (row[1],row[0])
    return coord

def register_new_user(connection,username,password):

    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO game (username, password, money, fuel, people_saved, municipality_visited, fuel_efficiency, location) VALUES (%s, %s, 3000, 1000, 0, 0, 0.8, 'EFHK')"
        cursor.execute(insert_query, (username, password))
        connection.commit()
        cursor.close()
        print("New user registered successfully!")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

def login_existing_user(connection,username,password):

    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM game WHERE username = %s AND password = %s"
        cursor.execute(select_query, (username, password))
        if cursor.fetchone() is not None:
            print("Login successful! Welcome, existing user.")
            return True
        else:
            print("Login failed. Username or password is incorrect.")
            return False
        cursor.close()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

def select_five_random_airports(connection, country_name):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name, people, fuel_price, probability FROM airport WHERE iso_country = (select iso_country from country where name = %s) ORDER BY RAND() LIMIT 5",
            (country_name,)
        )
        airports = cursor.fetchall()
        cursor.close()
        return airports
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def get_status(connection,username):
    try:
        cursor = connection.cursor()
        query = "SELECT money, fuel, people_saved, municipality_visited, fuel_efficiency, airport.name, fuel_price, country.name FROM game, airport, country WHERE location = ident and airport.iso_country=country.iso_country and username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        print(f"You currently have {result[0]} money and {result[1]} fuel.")
        time.sleep(1)
        print(f"You have saved {result[2]} people, visited {result[3]} countries.")
        time.sleep(1)
        print(f"Fuel efficiency is {result[4]}, and current location at {result[5]}, {result[7]}.")
        time.sleep(1)
        return result
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def get_status_without_printing(connection,username):
    try:
        cursor = connection.cursor()
        query = "SELECT money, fuel, people_saved, municipality_visited, fuel_efficiency, name, fuel_price FROM game, airport WHERE location = ident and username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None

def get_airport_status_without_printing(connection,airport_name):
    try:
        cursor = connection.cursor()
        query = ("SELECT name, people, fuel_price, probability FROM airport WHERE name = %s")
        cursor.execute(query, (airport_name,))
        result = cursor.fetchone()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None
def buy_fuel(connection,username):
    result = get_status_without_printing(connection,username)
    money = result[0]
    fuel = result[1]
    fuel_price = result[6]
    print(f"At your current location, 1 money equals to {result[6]} fuel. You now have {result[0]} money.")
    time.sleep(1)
    while True:
        spending = input("How much money you want to spend?, enter integer number:")
        if spending.isdigit():
            spending = int(spending)
            if money >= spending:
                fuel += spending * fuel_price
                money -= spending
                print(f"Your total fuel now is {fuel}, and you have {money} money left.")
            else:
                print("You don't have enough money to buy fuel.")
            try:
                cursor = connection.cursor()
                update_query = "UPDATE game SET money = %s, fuel = %s WHERE username = %s"
                cursor.execute(update_query, (money, fuel, username))
                connection.commit()
                cursor.close()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))
            break
        else:
            print("Invalid input, please enter integer.")

def travel(connection, airport_name, username):
    destination=get_coordinate_by_name(airport_name)
    departure=get_coordinate_by_ident(username)
    dist=int(distance(destination,departure))
    status=get_status_without_printing(connection,username)
    efficiency = status[4]
    current_fuel = status[1]
    fuel_needed = dist/efficiency
    fuel_left = current_fuel - fuel_needed
    try:
        cursor = connection.cursor()
        update_query = "UPDATE game SET fuel = %s, location = (select distinct ident from airport where name = %s), people_saved = people_saved + (select distinct people from airport where name = %s), municipality_visited = municipality_visited + 1 WHERE username = %s"
        cursor.execute(update_query, (fuel_left, airport_name, airport_name, username))
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    get_status(connection,username)

def select_three_random_countries(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM country ORDER BY RAND() LIMIT 3")
        countries = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return countries
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None
def user_choose_country(chosen_countries):
    while True:
        countries = select_three_random_countries(connection)
        available_countries = [country for country in countries if country not in chosen_countries]

        if len(available_countries) < 3:
            continue
        print("Choose one of the following countries:")
        for i, country in enumerate(available_countries, start=1):
            print(f"{i}. {country}")
            time.sleep(1)
        print("0. Refresh the list")
        try:
            choice = int(input("Enter the number of your choice (1, 2, or 3) or 0 to refresh the list: "))
            if choice == 0:
                countries = select_three_random_countries(connection)
                continue

            if 1 <= choice <= 3:
                print("You chose: ", countries[choice - 1])
                return countries[choice - 1]
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 0.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, 3, or 0).")

def user_choose_airport(airports, country_name, username):
    while True:
        print("Choose one of the following airports:")
        count = 1
        for name, people, fuel_price, probability in airports:
            destination = get_coordinate_by_name(airports[count - 1][0])
            departure = get_coordinate_by_ident(username)
            dist = distance(departure, destination)
            print(f"{count}. {airports[count-1][0]} has {airports[count-1][1]} people, 1 money = {airports[count-1][2]} fuel, {dist:.2f} km from your current location.{airports[count-1][3]}")
            count += 1
            time.sleep(1)
        print("0. Refresh the list.")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 0:
                airports = select_five_random_airports(connection, country_name)
                continue

            if 1 <= choice <= 5:
                print("You chose: ",airports[choice - 1][0])
                cursor = connection.cursor()
                update_query = "UPDATE game SET money = money + 10*%s WHERE username = %s"
                cursor.execute(update_query, (airports[choice-1][1], username))
                connection.commit()
                cursor.close()
                return airports[choice - 1][0]
            else:
                print("Invalid choice. Please enter the number according to airport name.")
        except ValueError:
            print("Invalid input. Please enter an integer number.")

def rob(connection, airport_name, username):
    airport_status = get_airport_status_without_printing(connection, airport_name)
    probability = airport_status[3]

    if probability == 1 or probability == 10:
        print("You've entered an evil airport. You are about to be robbed!")
        time.sleep(1)

        while True:
            print("Choose a debuff:")
            time.sleep(1)
            print("1. Lose half of your money")
            time.sleep(1)
            print("2. Decrease fuel efficiency by 0.2")
            time.sleep(1)

            choice = input("Enter 1 or 2: ")

            if choice == "1":
                player_status = get_status_without_printing(connection, username)
                money = player_status[0]
                money /= 2
                print(f"You've lost half of your money. Your new money value is {money}")
                time.sleep(1)
                try:
                    cursor = connection.cursor()
                    update_query = "UPDATE game SET money = %s WHERE username = %s"
                    cursor.execute(update_query, (money, username))
                    connection.commit()
                    cursor.close()
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                get_status(connection, username)

                break

            elif choice == "2":
                player_status = get_status_without_printing(connection, username)
                fuel_efficiency = player_status[4]
                fuel_efficiency -= 0.2
                print(f"Your fuel efficiency has decreased by 0.2. It's now {fuel_efficiency:.1f}")
                time.sleep(1)
                try:
                    cursor = connection.cursor()
                    update_query = "UPDATE game SET fuel_efficiency = %s WHERE username = %s"
                    cursor.execute(update_query, (fuel_efficiency, username))
                    connection.commit()
                    cursor.close()
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                get_status(connection, username)
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")
def reward(connection, airport_name, username):
    airport_status = get_airport_status_without_printing(connection, airport_name)
    probability = airport_status[3]

    if probability == 11 or probability == 20:
        print("You've entered a blessed airport. You are about to be rewarded!")
        time.sleep(1)

        while True:
            print("Choose a buff:")
            time.sleep(1)
            print("1. Gain 2000 money.")
            time.sleep(1)
            print("2. Increase fuel efficiency by 0.2")
            time.sleep(1)

            choice = input("Enter 1 or 2: ")

            if choice == "1":
                player_status = get_status_without_printing(connection, username)
                money = player_status[0]
                money += 2000
                print(f"You've gained 2000 money. Your new money value is {money}")
                time.sleep(1)
                try:
                    cursor = connection.cursor()
                    update_query = "UPDATE game SET money = %s WHERE username = %s"
                    cursor.execute(update_query, (money, username))
                    connection.commit()
                    cursor.close()
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                get_status(connection, username)

                break

            elif choice == "2":
                player_status = get_status_without_printing(connection, username)
                fuel_efficiency = player_status[4]
                fuel_efficiency += 0.2
                print(f"Your fuel efficiency has increased by 0.2. It's now {fuel_efficiency}")
                time.sleep(1)
                try:
                    cursor = connection.cursor()
                    update_query = "UPDATE game SET fuel_efficiency = %s WHERE username = %s"
                    cursor.execute(update_query, (fuel_efficiency, username))
                    connection.commit()
                    cursor.close()
                except mysql.connector.Error as err:
                    print("Error: {}".format(err))
                get_status(connection, username)
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")


def main():
    story()
    time.sleep(1)
    while True:
        choice = input("Are you a new user (n) or an existing user (e)? Enter 'q' to quit: ")
        if choice == 'q':
            break
        elif choice == 'n':
            username = input("Enter a new username: ")
            password = input("Enter a new password: ")
            register_new_user(connection,username,password)
            break
        elif choice == 'e':
            for i in range(0, 3):
                username = input("Enter your name here: ")
                password = input("Enter your password here: ")
                credentials = login_existing_user(connection,username,password)
                if credentials:
                    break
                else:
                    if i == 2:
                        print("You have entered wrong credentials for 3 times. Access denied")
                        return
            break
        else:
            print("Invalid choice. Please enter 'n', 'e', or 'q'.")
    get_status(connection,username)

    chosen_countries = []
    while True:
        status_list = get_status_without_printing(connection, username)
        current_people = status_list[2]
        current_visit = status_list[3]
        fuel = status_list[1]

        if fuel < 0 or current_people > 150:
            time.sleep(1)
            print("You crashed the plane! Game over.")
            break

        if current_people >= 100 and current_visit >= 5:
            time.sleep(1)
            print("Congratulations! You've won the game.")
            break

        else:
            buy_fuel(connection, username)
            time.sleep(1)
            chosen_country = user_choose_country(chosen_countries)
            chosen_countries.append(chosen_country)
            airports = select_five_random_airports(connection, chosen_country)
            chosen_airport = user_choose_airport(airports, chosen_country, username)
            time.sleep(1)
            travel(connection, chosen_airport, username)
            time.sleep(1)
            rob(connection,chosen_airport,username)
            reward(connection,chosen_airport,username)

    connection.close()

if __name__ == "__main__":
    main()
"""