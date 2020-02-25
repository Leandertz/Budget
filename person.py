import math
import os
import sys

import requests

name = input("Your name please: ")

# print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello " + who_to_greet
    return greeting


print(greet(name))
print(greet("Martin"))

r = requests.get("http://www.leandertz.se")
print(r.status_code)
