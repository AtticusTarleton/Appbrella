import sqlite3
from ipaddress import ip_address

import public_ip as ip
import ipinfo
import datetime
import random

from numpy.ma.extras import average

## creating the dictionaries
#it works such that the dictionary goes the smallest number, then the largest number for latitude
climate_dict = {
    'polar': [67,10000],
    'continental': [35, 67],
    'subtropic': [25,35],
    'tropic': [0,25]
}
#organized by month, day
#the dates chosen are completely arbitrary
season_dict = {
    'winter': [11,1, 1,31],
    'spring': [2,1, 4,30],
    'summer': [5,1,7,31],
    'fall': [8,1, 10,31]
}
average_temp = {
    'polar':{
        'winter': 31,
        'spring': 31,
        'summer': 30,
        'fall': 30  #change these numbers
    },
    'continental':{
        'winter': 31,
        'spring': 31,
        'summer': 30,
        'fall': 30  #change these numbers
    },
    'subtropic': {
        'winter': 31,
        'spring': 31,
        'summer': 30,
        'fall': 30  # change these numbers
    },
    'tropic': {
        'winter': 31,
        'spring': 31,
        'summer': 30,
        'fall': 30  # change these numbers
    }
}
# these numbers were decided  by my sister and dad based off of vibes
# their help was much appreciated

# need to absolute value the latitude to compare them. how to get values example: = climate_dict.get('polar')
# link to info https://scijinks.gov/climate-zones/ , https://mediaspace.msu.edu/media/Latitude+and+Global+CirculationA+Know+your+zones%21+/0_h896bb25

random_number1 = random.random() #weather random number
random_number2 = random.random() #temp random number

## now on to the functions
def weather_generator(random_number):
    guess = 'we at appbrella '
    if random_number > 1:
        guess += 'believe somethings wrong with our program'
    elif random_number > .9999:
        guess += 'predict cloudy with a chance of meatballs'
    elif random_number > .9998:
        guess = 'error, weather phenomena too chaotic to predict'
    elif random_number > .95 and season == 'winter' and climate_zone == "polar":
        guess += "predict SNOWSTORM!!!!!"
    elif random_number > .5:
        guess += 'love a good sunny day, just like the day we predict you will have today'
    elif random_number > .3:
        guess += "hope you love rain, because that's all that's on the forcast. But don't despair, who knows what tommorrow holds"
    elif random_number > 0:
        guess += "predict a boring, cloudy day"
    else:
        guess += 'believe somethings wrong with our program'

    return guess
# print(weather_generator())

# computers public ip address
def get_public_ip():
    public_IPAddr = ip.get()
    return public_IPAddr


# getting the date
def get_the_date():
    today = datetime.date.today()
    return str(today)

# print("Current date:", get_the_date())

# getting the location
def get_the_details(public_ip):
    public_ip = public_ip
    access_token = input('please enter your ipinfo access token: ')
    handler = ipinfo.getHandler(access_token=access_token)
    details = handler.getDetails(ip_address=public_ip)
    return details

# print(get_the_details(get_public_ip()))

def get_the_location(details):
    details = details
    location = []
    city = details.city
    country = details.country_name
    latitude = details.latitude
    location.append(country)
    location.append(city)
    location.append(latitude)
    return location

# print(get_the_location(get_the_details(get_public_ip()))) # printing out the location as a test



def get_the_climate(latitude):
    latitude = float(latitude)
    if latitude < 0:
        is_north = False
    else:
        is_north = True

    absolute_latitude = abs(latitude)
    climate = ''
    if absolute_latitude >= climate_dict['polar'][0]:
        climate = 'polar'
    elif absolute_latitude >= climate_dict['continental'][0]:
        climate = 'continental'
    elif absolute_latitude >= climate_dict['subtropic'][0]:
        climate = 'subtropic'
    elif absolute_latitude >= climate_dict['tropic'][0]:
        climate = 'tropic'
    return climate, is_north

# print(get_the_climate(get_the_location(get_the_details(get_public_ip()))[2]))


def is_between(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

def get_the_season(is_north, date):
    month = date[5] + date[6]
    day  = date[8] + date[9]
    month = int(month)
    day = int(day)
    if season_dict['spring'][0] <= month <= season_dict['spring'][2]:
        season = 'spring'
    elif season_dict['summer'][0] <= month <= season_dict['summer'][2]:
        season = 'summer'
    elif season_dict['fall'][0] <= month <= season_dict['fall'][2]:
        season = 'fall'
    else:
        season = 'winter'

    if not is_north:
        if season == "winter":
            season = 'summer'
        if season == "summer":
            season = 'winter'
        if season == "spring":
            season = 'fall'
        if season == "fall":
            season = 'spring'
    return season

# print(get_the_season(False, '2025-09-22'))

def add_to_database(current_date, prediction, city, country):
    con = sqlite3.connect('weather.db', isolation_level=None)
    cur = con.cursor()
    input_weather_pred = "INSERT INTO WeatherPredictions('date', 'guess_made', 'city', 'country') VALUES (?,?,?,?)"
    input_list = [current_date, prediction, city, country]
    cur.execute(input_weather_pred, input_list)
    con.close()

# add_to_database('1','333 333','1','1') # This is the test run

def check_date_location(current_date, current_city, current_country):
    con = sqlite3.connect('weather.db', isolation_level=None)
    cur = con.cursor()
    find_statement = f"SELECT guess_made FROM WeatherPredictions WHERE date = '{current_date}' AND city = '{current_city}' and country = '{current_country}'"
    found_statement = cur.execute(find_statement).fetchall()
    con.close()
    return found_statement

# print(check_date_location('1','1','1')) # this is a test run

if __name__ == "__main__":
    random_number1 = random.random()  # weather random number
    random_number2 = random.random()  # temp random number
    location = get_the_location(get_the_details(get_public_ip()))
    climate_zone = get_the_climate(location[2])
    date = get_the_date()
    season = get_the_season(climate_zone[1], date)
    weather_prediction = weather_generator(random_number1)
    past_pred = check_date_location(date, location[1], location[0])
    if len(past_pred) > 0:
        weather_prediction = past_pred[0][0]
    else:
        add_to_database(date, weather_prediction,location[1], location[0])
    print(weather_prediction)

    #need to add a temp predictor , then add the two predictions together


