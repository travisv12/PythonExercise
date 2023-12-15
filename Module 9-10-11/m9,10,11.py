print("9.1 and 9.2 and 9.3 and 9.4 and 10.4 and 11.2")
#Because these exercises all related to Car theme so I put them together
import random


class Car:
    def __init__(self, registration_number: str, maximum_speed: int):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change: int):
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

# This part is for 9.4
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

cars = [Car(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

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

# This part is for 10.4
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
            print(
                "{:<10} {:<15} {:<15} {:<15}".format(car.registration_number, car.current_speed, car.travelled_distance,
                                                     "Finished" if car.travelled_distance >= self.distance else "In Progress"))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    car_list = [Car(f"Car {i + 1}", random.randint(100, 200)) for i in range(10)]

    race = Race("Grand Demolition Derby", 8000, car_list)

    hour = 1
    while not race.race_finished():
        if hour % 10 == 0:
            print("The race has lasted for", hour, "hours")
            race.print_status()
        race.hour_passes()
        hour += 1

    print("The race finished at", hour, "hours")
    race.print_status()

# This part is for 11.2
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



print("10.1 and 10.2 and 10.3")
class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = self.bottom_floor

    def floor_up(self, target_floor: int):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Moving up to floor {self.current_floor}.")
        print(f"Elevator has reached floor {self.current_floor}")

    def floor_down(self, target_floor: int):
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Moving down to floor {self.current_floor}.")
        print(f"Elevator has reached floor {self.current_floor}")

    def go_to_floor(self, target_floor: int):
        if target_floor < self.current_floor:
            self.floor_down(target_floor)
        elif target_floor > self.current_floor:
            self.floor_up(target_floor)
        else:
            print(f"Elevator is already on floor {target_floor}.")


elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(1, num_elevators + 1)]

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


building = Building(1, 10, 3)

building.run_elevator(1, 7)
building.run_elevator(2, 2)

building.fire_alarm()

print("11.1")


class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        pass


class Book(Publication):
    def __init__(self, name, page, author):
        self.page = page
        self.author = author
        super().__init__(name)

    def print_info(self):
        print(f"The book {self.name} has {self.page} pages and was written by {self.author}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        print(f"The magazine {self.name} was edited by {self.editor}")


magazine1 = Magazine("Donald Duck", "Aki Hyyppa")
book1 = Book("Compartment No.6", 192, "Rosa Liksom")
magazine1.print_info()
book1.print_info()
