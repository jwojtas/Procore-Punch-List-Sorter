import csv  
import output
from tkinter import *

fill = input("Enter File name:")
f = open(fill)
csv_f = csv.reader(f)
c = open('data.csv', "w")
m = csv.writer(c)
dict_out = {}
next(csv_f, None)
for row in csv_f:
 if row[1] in dict_out:
     dict_out[row[1]].append(row[3])
 else:
     dict_out[row[1]] = [row[3]]

for title, value in dict_out.items():
    m.writerow([title] + value)

c.close()
output.toxlsx()