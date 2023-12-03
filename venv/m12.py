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
