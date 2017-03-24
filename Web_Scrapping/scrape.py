'''
Description : Webscrapping : Importing web page and extracting table content and putting in csv file

Author : Saif Ansari

Date : 23/03/2017

Python Library Imported :
	1)BeautifulSoup : Extract html content from recieved response from requested url
	2)requests : gets the  response from url   
	3)csv : to use csv file
'''

import csv
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.espn.in/football/league/_/name/eng.1/'


response = requests.get(url)  #get response from url
html = response.content



soup = BeautifulSoup(html)   #extract html content from received response 
table = soup.find('table', attrs={'class': 'mod-data'})


list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./outputfile.csv", "wb")
writer = csv.writer(outfile)   //writing into csv file
writer.writerows(list_of_rows)
