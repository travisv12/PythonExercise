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
