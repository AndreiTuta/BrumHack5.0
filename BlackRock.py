import requests
from random import *

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance")
x=randint(1,28)
y=randint(1,12)
w=randint(2000,2000)
startDate = str(str(x)+"-"+str(y)+"-2012")
z=y + 5
endDate = str(str(x)+"-"+str(z)+"-2016")
print("Hello Costumer , here are you information for today : ")
print("Current balance : " + str(w) +" GBP")
print("Valid from : " + startDate)
print("Valid until: " + endDate)
print("Have a wonderful day!")
portfolioAnalysisRequest.text # get in text string format
portfolioAnalysisRequest.json # get as json object
