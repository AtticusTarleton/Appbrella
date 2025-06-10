# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname)
#
# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)
#
# import public_ip as ip
#
# print(ip.get())
# public_IPAddr = ip.get()
#
#
#
#
#
# access_token = input('please enter your ipinfo access token: ') # to get your own access token, go to
# #https://ipinfo.io/dashboard and sign up. you get 50,000 requests on the free plan each month
#
# ip_address = public_IPAddr  # Replace with the desired IP address
#
#
# import ipinfo
# handler = ipinfo.getHandler(access_token=access_token)
# details = handler.getDetails(ip_address = public_IPAddr)
# print(details.all)
# print(details.city)
# print(details.country_name)
# print(details.loc)

import random
import math
# #take 1
# i = 0
# while i < 10:
#     random_number = random.random()
#     random_number1 = random.random()
#     if random_number1 < .5:
#         temp_guess = 10 + math.log(random_number * 20, 1.5)
#     else:
#         temp_guess = 10 - math.log(random_number * 20, 1.5)
#     print(temp_guess)
#     i+=1

#take 2
j = 0
while j < 10:
    random_number = random.gauss(0,7)
    temp_guess = 10 + random_number
    print(temp_guess)
    j+=1

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#type flask --app test run  #copy paste this into the terminal to get a website

