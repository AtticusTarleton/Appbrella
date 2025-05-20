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
season_dict = {
    'winter': ['11-21', '02-13'],
    'spring': ['02-14', '05-31'],
    'summer': ['06-01','08-01'],
    'fall': ['08-01', '11-20']
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
season = 'NA'

## now on to the functions
def weather_generator():
    guess = 'we at appbrella '
    if random_number1 > 1:
        guess += 'believe somethings wrong with our program'
    elif random_number1 > .9999:
        guess += 'predict cloudy with a chance of meatballs'
    elif random_number1 > .9998:
        guess = 'error, weather phenomena too chaotic to predict'
    elif random_number1 > .5:
        guess += 'love a good sunny day, just like the day we predict you will have today'
    elif random_number1 > .3:
        guess += "hope you love rain, because that's all that's on the forcast. But don't despair, who knows what tommorrow holds"

    else:
        guess += 'believe somethings wrong with our program'

    return guess


# computers public ip address
def get_public_ip():
    public_IPAddr = ip.get()
    return public_IPAddr


# getting the date
def get_the_date():
    today = datetime.date.today()
    return str(today)
print("Current date:", get_the_date())

# getting the location
def get_the_details(public_ip):
    public_ip = public_ip
    access_token = input('please enter your ipinfo access token: ')
    handler = ipinfo.getHandler(access_token=access_token)
    details = handler.getDetails(ip_address=public_ip)
    return details

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

def get_the_climate(latitude):
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

def is_between(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

def get_the_season(is_north, date):
    climate = ''
    month = date[5] + date[6]
    day = date[8] + date[9]
    month = int(month)
    day = int(day)





    if not is_north:
        if climate == "winter":
            climate = 'summer'
        if climate == "summer":
            climate = 'winter'
        if climate == "spring":
            climate = 'fall'
        if climate == "fall":
            climate = 'spring'
    return climate

# print(get_the_location(get_the_details(get_public_ip()))) # printing out the location as a test
