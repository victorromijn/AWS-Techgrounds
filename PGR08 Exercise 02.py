# We hebben data naar een csv bestand te schrijven
# Eerst module csv activeren
# het schrijven/formuleren van een header met list -> header list
# Header eenmalig in output, daarna verwijderen uit script
# dan via functie from typing import Tuple data naar (een) bestand schrijven
# dan input genereren via de functie input, met variabele a tm d maken
# csv-bestand openen
# data in bestand schrijven in nieuwe vrije lijn (append -> "a")


import csv
from typing import Tuple

header = ['first name: ', 'last name: ', 'job title: ', 'company: ']
a = input('first name: ')
b = input('last name: ')
c = input('job title: ')
d = input('company: ')
data = [a,b,c,d]

with open('opdracht82.csv', 'a', encoding='UTF8', newline='') as q:
    writer = csv.writer(q)

    #write the header
    #writer.writerow(header)

    # write the data
    writer.writerow(data)
