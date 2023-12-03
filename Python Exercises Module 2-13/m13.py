print("13.1")
from flask import Flask

app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    result = {"Number": number, "isPrime": is_prime(number)}
    return result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

print("13.2")
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='travis',
    password='database123',
    autocommit=True
)
cursor = conn.cursor()

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    query = f"SELECT ident,name,municipality FROM airport WHERE ident = '{icao}'"
    cursor.execute(query)
    airport_info = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in airport_info:
            result = {"ICAO": row[0], "Name": row[1], "Location": row[2]}
            return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True, host='127.0.0.1', port=5000)

