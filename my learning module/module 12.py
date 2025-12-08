import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["value"])
    else:
        print("Failed to fetch joke.")


get_chuck_norris_joke()


# Question 2
import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Could not fetch weather data. Check city name or API key.")
        return

    data = response.json()

    # Weather description
    description = data["weather"][0]["description"]

    # Temperature in Kelvin -> Celsius
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}:")
    print(f"  Condition: {description}")
    print(f"  Temperature: {temp_celsius:.1f} °C")


# --------------------------
# Main program
# --------------------------

city = input("Enter the name of a municipality: ")
get_weather(city)

