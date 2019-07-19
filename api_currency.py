"""
This is a code I created whilst playing around with the urllib module in the standard library. 
It basically sends a request to the API, converts the result from json format and uses the result to calculate the conversion using the current rate. 

I didn't include input but if you change the input value to any currency in its 3 letter shorthand in caps (e.g. 'GBP') it should work. 
It is simplistic but any feedback is welcome.

+++++++++++++++++++++++++++++++++++++++++++
Here is a link to the API website:
https://www.currencyconverterapi.com/docs
"""

# Import libraries
import urllib.request
import json

def convert_currency(amount, convert_from, convert_to):
    
    query = f"{convert_from}_{convert_to}"
    
    url = urllib.request.urlopen(f"https://free.currencyconverterapi.com/api/v6/convert?q={query}&compact=ultra&apiKey=5d1694415f43d11e5f63")
    
    decode = json.load(url)
    value = decode[query]
    
    converted = round(value * amount, 2)
    print(str(amount) + " " + convert_from + " = " + str(converted) + " " + convert_to)
    
    
convert_currency(100, 'GBP', 'EUR')
convert_currency(1000, 'INR', 'USD')
convert_currency(10000, 'RUB', 'ZWL')
