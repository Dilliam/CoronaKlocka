# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#lolthis is really nice and i seem to like PYTHON :D <3

import requests
import socket
import lxml.html as lh
from datetime import datetime
import pandas as pd
import random
game = True
nbr = random.randrange(1, 100)

from http.server import HTTPServer, BaseHTTPRequestHandler




url='https://www.folkhalsomyndigheten.se/folkhalsorapportering-statistik/statistikdatabaser-och-visualisering/vaccinationsstatistik/statistik-for-vaccination-mot-covid-19/'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#Check the length of the first 12 rows
print([len(T) for T in tr_elements[:12]])

#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))

# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # If row is not of size 2, the //tr data is not from our table
    if len(T) != 2:
        break

    # i is the index of our column
    i = 0

    # Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # Check if row is empty
        if i > 0:
            # Convert any numerical value to integers
            try:
                data = int(data)
            except:
                pass
        # Append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1
test_date = col[0][1]

date_dt3 = datetime.strptime(test_date[0].strip(), '%Y-%m-%d')
date_dt4 = datetime.strptime(test_date[4].strip(), '%Y-%m-%d')

time = date_dt3 - date_dt4
print(date_dt3 - date_dt4)

vacr =col[1][1]

median = int(vacr[0].strip().replace(' ', '')) - int(vacr[4].strip().replace(' ', ''))
amount = int(vacr[0].strip().replace(' ', ''))
fff = int(median)

print(amount)



mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.bind((socket.gethostname(), 1234))
mysocket.listen(5)

while True:
    clientSocket, address = mysocket.accept()
    print(f"connection from {address} has been established")
    clientSocket.send(bytes(str(amount), "utf-8"))





