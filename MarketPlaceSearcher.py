#Packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re #re stands for Regular Expression

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#Open the text file that contain links to strange weapons.
txtFile = open("StrangeItemsLinks.txt", "r")

#Read all the links in the text file.
StrangeItemsLinks = txtFile.readlines()

#Take user input.
strangePart = input("What would you like to search for?")

#This loop allows the user to input URLs repeatedly.
for link in StrangeItemsLinks:
    #Read the link
    URL = link

    #A Request object is initialized using the URL and the header.
    request = Request(URL, data=None, headers={'User-Agent': HEADER})

    #BeautifulSoup object is intilized and the webpage is accessed here.
    soup = BeautifulSoup(urlopen(request), 'html.parser')

    #bool return either true or false. True if strange part is found, false if otherwise. The soup is the webpage, which is converted into string. Converting it to a string allows regex to read it.
    result = bool(re.search(strangePart, str(soup)))

    #If the result is true, then the title of the webpage that contains Damage Dealt strange part would be displayed. Else, nothing will be displayed to the user.
    if result:
        print(soup.title.string + ": " + link)