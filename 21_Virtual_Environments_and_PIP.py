# Lesson 21: Virtual Environment and PIP

# To install a package using PIP, do this in your Git Bash Terminal:
# py -m pip install package-you-want-to-install

# To install a specific version of a package, do this in your Git Bash Terminal:
# py -m pip install package-you-want-to-install==1.0.0 or whichever version you want to install

# ? Virtual Environment are used to install packages in your project without affecting your installed packages.
# Do this in your Git Bash Terminal: py -m venv .venv
# ? This will create a .venv folder

# ? Always active your virtual environment before working on your project
# To activate it, do this in your Git Bash Terminal: source .venv/Scripts/activate
# To deactivate it, do this in your Git Bash Terminal: deactivate

# To search for packages to install in your project, go to https://pypi.org

# To create a list of requirements, do this in your Git Bash Terminal:
# py -m pip freeze > requirements.txt

# To exclude .venv folder in your Github repository, create a .gitignore file in your root directory.

# ! NOTE: ACTIVATE .VENV FIRST BEFORE RUNNING THIS CODE
# Weather Project
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_currect_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    print(
        f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')

if __name__ == "__main__":
    get_currect_weather()
