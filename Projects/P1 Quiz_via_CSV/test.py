import os
import csv

with open('q1.csv', 'r') as q:
    writer1 = csv.writer(q)
    for row in writer1:
        print(row[1])
