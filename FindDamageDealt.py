#Packages
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re #re stands for Regular Expression

#Takes the user input.
print("Enter URL:")
URL = input()

#Some websites do not allow crawlers or web scrapping. This header is a workaround and it prevents the 403 HTTP forbidden issue.
HEADER = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

#A Request object is initialized using the URL and the header.
request = Request(URL, data=None, headers={'User-Agent': HEADER})

#BeautifulSoup object is intilized and the webpage is accessed here.
soup = BeautifulSoup(urlopen(request), 'html.parser')

#Look for text that matches the string below EXACTLY.
result = soup.findAll("span", string='Strange Part: Damage Dealt')

print(soup)
print(result)