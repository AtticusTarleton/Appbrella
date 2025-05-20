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
average_weather = {
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


# computers public ip address
def get_public_ip():
    public_IPAddr = ip.get()
    return public_IPAddr


# getting the date
def get_the_date():
    today = datetime.date.today()
    return today
# print("Current date:", get_the_date())


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
    country = details.country
    location.append(country)
    location.append(city)
    return location


# print(get_the_location().all) # printing out the location as a test
