#Packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re #re stands for Regular Expression

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#This loop allows the user to input URLs repeatedly.
while True:
    #Takes the user input.
    URL = input("Enter URL:")

    #A Request object is initialized using the URL and the header.
    request = Request(URL, data=None, headers={'User-Agent': HEADER})

    #BeautifulSoup object is intilized and the webpage is accessed here.
    soup = BeautifulSoup(urlopen(request), 'html.parser')

    #bool return either true or false. True if Damage Dealt is found, false if otherwise. The soup is the webpage, which is converted into string. Converting it to a string allows regex to read it.
    result = bool(re.search('Damage Dealt', str(soup)))

    #If the result is true, then the title of the webpage that contains Damage Dealt strange part would be displayed. Else, nothing will be displayed to the user.
    if result:
        print(soup.title.string)