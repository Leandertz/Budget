import math
import os
import sys

import requests

f_name = input("Your first name please: ")
l_name = input("Your last name please: ")

# print(sys.version)
# print(sys.executable)


def greet(f_name, l_name):
    greeting = f"Hej {f_name}! Jag har hört att du heter {l_name} i efternamn"
    return greeting


print(greet(f_name, l_name))
print("Hej då!")

r = requests.get("http://www.leandertz.se")
print(r.status_code)
