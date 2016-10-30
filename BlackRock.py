import requests
from random import *

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

def blackrock():
    portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/hackathon/performance")
    x=randint(1,28)
    y=randint(1,7)
    w=randint(2000,210000)
    startDate = str(str(x)+"-"+str(y)+"-2014")
    z=y + 5
    p=x + randint(0,21)
    endDate = str(str(p)+"-"+str(z)+"-2019")
    temp ="Hello Costumer ,\n here is your information for today : \n Current balance : " + str(w) +" GBP  \n  Valid from : " + startDate +" \n Valid until: " + endDate
    return temp
    CapitalOne()

def CapitalOne():
    url = ("http://api.reimaginebanking.com/enterprise/bills?key=099313bf21c0ee46db36cd859769cf01")
    data = {"Id": str(randint(100,158)) + "azy"+str(randint(100,999)) +"b069" + str(randint(1,99)), "Status :": "valid"}
    response = requests.get(url, data)
    Id=str(randint(100,158)) + "ughy"+str(randint(100,999)) +"b069" + str(randint(1,99))
    print("Id :" + str(Id))
    print("Status : valid")
    print("Have a wonderful day!")

blackrock()
