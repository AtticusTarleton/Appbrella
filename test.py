import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

import public_ip as ip

print(ip.get())
public_IPAddr = ip.get()





access_token = input('please enter your ipinfo access token: ') # to get your own access token, go to
#https://ipinfo.io/dashboard and sign up. you get 50,000 requests on the free plan each month

ip_address = public_IPAddr  # Replace with the desired IP address


import ipinfo
handler = ipinfo.getHandler(access_token=access_token)
details = handler.getDetails(ip_address = public_IPAddr)
print(details.all)
print(details.city)
print(details.country_name)
print(details.loc)
