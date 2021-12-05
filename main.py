# DSC510-T301
# Week 11
# Programming Assignment Week 12: Final Project
# Author Kaylar Fullington
# 11/15/2021

# Requirements:
# Create a header for your program just as you have in the past.
# Create a Python Application which asks the user for their zip code or city (Your program must perform both a city and a zip lookup).
# You must ask the user which they want to perform with each iteration of the program.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.
# You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
# Use comments within the application where appropriate in order to document what the program is doing.
# Comments should add value to the program and describe important elements of the program.
# Use functions including a main function and a properly defined call to main. You should have multiple functions.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should never crash with bad user input.
# Use the Requests library in order to request data from the webservice.
# Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
# Use Python 3
# Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
# You must have proper coding convention including proper variable names (See PEP8).
# Deliverables:
#   Final Program in a .py file (Due week 12)

# Project Notes
# Here an example of what I'm looking for, for your output. Notice the fields. You should have at least the current temp, high temp, low temp,
#   pressure, humidity, and cloud cover elements in your output.
# Think about the type of data a normal person would want when they look up weather. Odds are they want more than just the current temp.
# Do not display temp in Kelvin, this would be considered unreadable right? I don't know anyone who looks at kelvin temps.
# Do make this pretty, this is a big project and something you could showcase to others
# Make sure you're not rigid with the input from a user. If a user types in y and you wanted Y that should be ok. Think about the user experience.
# Think about punctuation and grammar for your prompts.
# Have nicely defined try blocks (these are required). DO NOT put huge blocks of code in a try block.
# Make sure your main is properly defined.
# If you're unsure about something ask.
# Make sure you allow the user to enter in a zip code and a city name. (it's ok to hard code the country to us.
# Make sure that if a user enters in Omaha it evaluates to the right Omaha.
# Have fun with this assignment.


import requests


def get_city():
    while True:
        city_name = input("Please enter the name of the city you wish to look up: ").upper()
        if all(x.isalpha() or x.isspace() for x in city_name):
            return city_name
        else:
            print("Invalid input. Please enter letters and spaces only - no numbers or punctuation.")


# this function retrieves the city name from the user in a loop - it makes sure that the only characters are alphabetical or a space (to cover cities such as New York)
# the else section catches any other characters (punctuation, numbers, mixes of all, etc), prints an error and starts over


def get_state():
    while True:
        state_name = input("Please enter the abbreviation for the state the city is in (2 letters): ").upper()
        if not state_name.isalpha():
            print("Invalid input. Please enter only alphabetic characters.")
        elif len(state_name) != 2:
            print("You have entered more than 2 characters. Please try again.")
        else:
            return state_name


# this function retrieves the state name from the user ina  loop - it first checks if the input is alphabetic. If not, it prints an error and starts the loop over
# then it checks to see if the length of the alphabetic characters is 2 - if not, it prints an error and starts the loop over
# if the input is two alphabetic characters, it returns the input as the state name

def get_zip():
    while True:
        zip_code = input("Please enter the United States zip code of the place you wish to look up: ")
        if len(zip_code) != 5:
            print("Invalid zip code. Please enter a zip code with five digits. No letters or punctuation.")
        elif zip_code.isnumeric() is True:
            return zip_code
        else:
            print("Invalid input. Please enter a zip code with five digits. No letters or punctuation.")


# this function retrieves the zip code from the user in a loop - it first checks to see if the length of the zip code is five - if not, it prints an error and starts the loop over
# then, it checks to see if the five characters are numbers - if so, it returns the numbers as the zip code
# the else function catches any punctuation that might have been entered


def f_temp(current_temp, min_temp, max_temp, feels_like_temp):
    f_current_temp = int((current_temp - 273.15) * 9 / 5 + 32)
    f_min_temp = int((min_temp - 273.15) * 9 / 5 + 32)
    f_max_temp = int((max_temp - 273.15) * 9 / 5 + 32)
    f_feels_like_temp = int((feels_like_temp - 273.15) * 9 / 5 + 32)
    print("Current Temperature: ", f_current_temp, "degrees")
    print("Low Temperature: ", f_min_temp, "degrees")
    print("High Temperature: ", f_max_temp, "degrees")
    print("Feels Like: ", f_feels_like_temp, "degrees")


# this function calculates the temperatures from Kelvin (the default that the website provides) to fahrenheit and prints the results


def c_temp(current_temp, min_temp, max_temp, feels_like_temp):
    c_current_temp = int(current_temp - 273.15)
    c_min_temp = int(min_temp - 273.15)
    c_max_temp = int(max_temp - 273.15)
    c_feels_like_temp = int(feels_like_temp - 273.15)
    print("Current Temperature: ", c_current_temp, "degrees")
    print("Low Temperature: ", c_min_temp, "degrees")
    print("High Temperature: ", c_max_temp, "degrees")
    print("Feels Like: ", c_feels_like_temp, "degrees")


# this function calculates the temperatures from Kelvin (the default that the website provides) to celsius and prints the results


def decide_temp(current_temp, min_temp, max_temp, feels_like_temp):
    while True:
        user_temp = input(
            "How would you like to view the temperatures? Enter K for Kelvin, F for Fahrenheit, or C for Celsius: ")
        if user_temp.isalpha() is True:
            if user_temp.lower() == 'k':
                print("Current Temperature: ", int(current_temp), "degrees")
                print("Low Temperature: ", int(min_temp), "degrees")
                print("High Temperature: ", int(max_temp), "degrees")
                print("Feels Like: ", int(feels_like_temp), "degrees")
                break
            elif user_temp.lower() == 'f':
                return f_temp(current_temp, min_temp, max_temp, feels_like_temp)
            elif user_temp.lower() == 'c':
                return c_temp(current_temp, min_temp, max_temp, feels_like_temp)
            else:
                print("Invalid input. Please enter 'K' for Kelvin, 'F' for Fahrenheit, or 'C' for Celsius.")
        else:
            print("Invalid input. Please enter 'K' for Kelvin, 'F' for Fahrenheit, or 'C' for Celsius.")


# the function decide_temp allows the user to select which temperature measurement they would like to view
# if they enter an uppercase letter, it defaults to lowercase because of .lower()
# if the input is alphabetical it enters an if/else loop
# if they select 'k' for Kelvin it prints what the website provides (since that's the default)
# if they select 'f' for Fahrenheit it calls the f_temp function (to calculate the website provided temps into fahrenheit and prints the results
# if they select 'c' for Celsius it calls the c_temp function (to calculate the website provided temps into celsius and prints the results
# if they select any other letter it prints an error and starts the loop over
# if the input is not alphabetical, it prints an error and starts the loop over


def call_zip_weather(zip_code):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    querystring = {"zip": zip_code, "APPID": "66fe071a879387838f44ded14568fd4d"}
    headers = {'cache-control': 'no-cache'}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("There was an http error: ", repr(e))
    except requests.exceptions.ConnectionError as e:
        print("There was an problem connecting to the API: ", repr(e))
    except requests.exceptions.Timeout as e:
        print("There was a timeout error: ", repr(e))
    except requests.exceptions.RequestException as e:
        print("An unknown error occurred: ", repr(e))
    else:
        zip_weather = response.json()
        return zip_weather


# the function call_zip_weather performs the api call based on the user input zip code
# it includes error handling try/except blocks to print errors in the case of typos in the web address or connection errors
# if all goes well, it returns json data of the weather from the website


def call_city_weather(city_name, state_name):
    url = "http://api.openweathermap.org/data/2.5/weather?q={},{},US&appid={}".format(city_name, state_name, "66fe071a879387838f44ded14568fd4d")
    payload = {}
    headers = {}
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("There was an http error: ", repr(e))
    except requests.exceptions.ConnectionError as e:
        print("There was a problem connecting to the API: ", repr(e))
    except requests.exceptions.Timeout as e:
        print("There was a timeout error: ", repr(e))
    except requests.exceptions.RequestException as e:
        print("An unknown error occurred: ", repr(e))
    else:
        city_weather = response.json()
        return city_weather


# the function call_city_weather performs the api call based on the user input city and state
# it includes error handling try/except blocks to print errors in the case of typos in the web address or connection errors
# if all goes well, it returns json data of the weather from the website

def get_weather_city(city_name, city_weather, state_name):
    print("Here is the weather for", city_name, state_name, ": ")
    cloud_cover_city = city_weather['weather'][0]['description'].title()
    current_temp = city_weather['main']['temp']
    feels_like_temp = city_weather['main']['feels_like']
    min_temp = city_weather['main']['temp_min']
    max_temp = city_weather['main']['temp_max']
    pressure_city = city_weather['main']['pressure']
    humidity_city = city_weather['main']['humidity']
    wind_speed_city = city_weather['wind']['speed']
    wind_gust_city = city_weather['wind']['gust']
    decide_temp(current_temp, min_temp, max_temp, feels_like_temp)
    print("Cloud Cover: ", cloud_cover_city)
    print("Humidity: ", humidity_city, "%")
    print("Wind Speed: ", wind_speed_city, "mph")
    print("Wind Gusts: ", wind_gust_city, "mph")
    print("Pressure: ", pressure_city, "atm")

# the function get_weather_city takes the information from the get_city, get_state, and call_city_weather functions to print out the weather in a readable format for the user
# it reads the json file (named city_weather) and variables are created for cloud cover and so on, which are then printed


def get_weather_zip(zip_weather, zip_code):
    cloud_cover_zip = zip_weather['weather'][0]['description'].title()
    current_temp = zip_weather['main']['temp']
    feels_like_temp = zip_weather['main']['feels_like']
    min_temp = zip_weather['main']['temp_min']
    max_temp = zip_weather['main']['temp_max']
    pressure_zip = zip_weather['main']['pressure']
    humidity_zip = zip_weather['main']['humidity']
    wind_speed_zip = zip_weather['wind']['speed']
    wind_gust_zip = zip_weather['wind']['gust']
    print("Here is the weather for", zip_code, ": ")
    decide_temp(current_temp, min_temp, max_temp, feels_like_temp)
    print("Cloud Cover: ", cloud_cover_zip)
    print("Humidity: ", humidity_zip, "%")
    print("Wind Speed: ", wind_speed_zip, "mph")
    print("Wind Gusts: ", wind_gust_zip, "mph")
    print("Pressure: ", pressure_zip, "atm")

# the function get_weather_city takes the information from the get_zip and call_zip_weather functions to print out the weather in a readable format for the user
# it reads the json file (named zip_weather) and variables are created for cloud cover and so on, which are then printed


def main():
    print(
        "Welcome to United States Weather Lookup! You can look up the weather anywhere in the United States - let's begin!")
    while True:
        try:
            user_selection = input(
                "Would you like to look up the weather by city or zip code? Enter 'c' for city or 'z' for zip code. Enter 'x' to exit. ")
            if user_selection.isalpha() is False:
                print("Invalid input. Please enter 'c' for city or 'z' for zip code. Enter 'x' to exit. ")
        except ValueError:
            print("Invalid input. Please enter 'c' for city or 'z' for zip code. Enter 'x' to exit. ")
        else:
            if user_selection.lower() == 'c':
                city_name = get_city()
                state_name = get_state()
                call_city_weather(city_name, state_name)
                city_weather = call_city_weather(city_name, state_name)
                get_weather_city(city_name, city_weather, state_name)
            elif user_selection.lower() == 'z':
                zip_code = get_zip()
                call_zip_weather(zip_code)
                zip_weather = call_zip_weather(zip_code)
                get_weather_zip(zip_weather, zip_code)
            elif user_selection.lower() == 'x':
                print("Thank you for using Weather Lookup!")
                break
            else:
                print("Invalid input. Please enter 'c' for city, 'z' for zip code, or 'x' to exit.")

# in the main function the user is asked to select whether they would like to look up the weather by city or by zip code in a loop which checks for alphabetic characters
# then, if they select 'c' various city functions are called in order to print the weather
# if they select 'z' various zip code functions are called in order to print the weather
# and if they select 'x' the program exits and prints a farewell message


if __name__ == '__main__':
    main()
