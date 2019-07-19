"""
This is another code I created whilst playing around with the urllib module in the standard library. 
This time playing around with import to shorten the very long method names, and module specific error handling. 
"""

# Import libraries
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from random import choice 

urls =["https://www.google.co.uk", "https://www.npr.org/404page", "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20%3D%22msft%22&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"]
    
req = Request(choice(urls)) 

try: 
    response = urlopen(req)
    print("The url opened!\nPrinting info...\n") 
    print(response.info())
    
except HTTPError as e: 
    print("Could not fulfill the request") 
    print("Error code:", e.code)
    print("Reason:", e.reason)
except URLError as e: 
    print("Failed to reach the server")
    print("Reason:", e.reason)
