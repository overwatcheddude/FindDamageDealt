#Packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re #re stands for Regular Expression

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#Open the text file that contain links to strange items including strange cosmetics and weapons.
txtFile = open("StrangeItemsLinks.txt", "r")

#Read all the links in the text file.
StrangeItemsLinks = txtFile.readlines()

#Take user input.
strangePart = input("What would you like to search for?")
txtStartNumber = input("At what item number would you like to start at?")

#Converts user input into a number
startNumber = int(txtStartNumber)

#This counter will help the user keep track of how many weapons have been searched so far. It is used in the for loop below.
counter = startNumber

#The {} are formatted in the for loop below.
progressBar = "{} items have been searched out of {}"

try:
    #This loop will go through every link in the text file. It start with a number assigned by the user.
    for link in StrangeItemsLinks[startNumber:]:
        #Read the link
        URL = link

        #A Request object is initialized using the URL and the header.
        request = Request(URL, data=None, headers={'User-Agent': HEADER})

        #BeautifulSoup object is intilized and the webpage is accessed here.
        soup = BeautifulSoup(urlopen(request), 'html.parser')

        #bool return either true or false. True if strange part is found, false if otherwise. The soup is the webpage, which is converted into string. Converting it to a string allows regex to read it.
        result = bool(re.search(strangePart, str(soup)))

        #Increases the counter by one.
        counter += 1

        #If the result is true, then the title of the webpage that contains text that matches the user input would be displayed, along with its link. end='' removes the newlines.
        if result:
            print(soup.title.string + ": " + link, end='')

        #Display to the user how many items have been searched so far. end="\r" will print on the same line.
        print(progressBar.format(counter, len(StrangeItemsLinks)), end="\r")
except:
    print("The program broke at item number: " + str(counter))