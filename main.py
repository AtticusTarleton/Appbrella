import sqlite3
from ipaddress import ip_address

import public_ip as ip
import ipinfo
import datetime


# computers public ip address
def get_public_ip():
    public_IPAddr = ip.get()
    return public_IPAddr


# getting the date
def get_the_date():
    today = datetime.date.today()
    return today
# print("Current date:", today)


# getting the location
def get_the_location():
    public_ip = get_public_ip()
    access_token = input('please enter your ipinfo access token: ')
    handler = ipinfo.getHandler(access_token=access_token)
    details = handler.getDetails(ip_address=public_ip).all
    return details

print(get_the_location())