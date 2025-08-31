import requests 
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city="Bellevue"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()
    return weather_data
    


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***")
    city = input("\nPlease enter a city name:\n")

    #check for empty string or only spaces
    if not bool(city.strip()):
        city = "bellevue"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)