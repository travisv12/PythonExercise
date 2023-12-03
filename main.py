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
