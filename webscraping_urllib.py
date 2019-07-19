"""
I have written this code to request data from a webpage (Science Daily in this case), then parse it and save any weblinks on the page to a list. 
To do it on Sololearn I've had to use the standard library, which as it turns out is quite complicated. 

I have learnt a lot figuring this out so from that point of view it has been very valuable. 
If I wasnt using the standard library I would have just used the requests and beautiful soup modules which would have made life much easier!

Any feedback or comments are welcome.
Thanks,
Rob

=============================================
NB: For some reason on Sololearn, some of the parsed web address change to the one for the Sololearn playground. This does not happen when I tried it on Pydroid. If you know why this is happening then I would be intrigued to know.
"""

# Import libraries
from urllib.request import urlopen, Request
from html.parser import HTMLParser

# Create a subclass of HTMLParser and initialise it. Then add or modify any attributes or methods you require
class MyHTMLParser(HTMLParser):
    def __init__(self):      
        HTMLParser.__init__(self)
        self.data_list = []
    
# Modify the module 'handle_starttag' method to look the 'anchor' tag. Then check the defined attributes (a dictionary) and if 'href' is defined, append to class attribute 'data_list'
    def handle_starttag(self, tag, attrs): 
        if tag == "a": 
            for name, value in attrs: 
                if name == "href": 
                     self.data_list.append(value)
       

# Create a header and define user agent as a dictionary key. This is so that the url we are trying to access does not detect us as a python program and auto reject, but instead thinks we are accessing from a browser
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}

# Send a request to the url with the user agent header included. Then open the request object and save the response as a variable (url)
req = Request('https://www.sciencedaily.com/news/top/science/', headers = headers)
res = urlopen(req)

# Read the data from the HTTPResonse object and decode from bytes to unicode string
data = res.read().decode('UTF-8')

# Create an instance of the modified HTMLParser class
parser = MyHTMLParser()

# Call the feed method to add data which is fed into object and processed based on the methods you defined or modified in the HTMLParser class
parser.feed(data)

# Then call the data_list class attribute to see the parsed data
print(parser.data_list[:10])
