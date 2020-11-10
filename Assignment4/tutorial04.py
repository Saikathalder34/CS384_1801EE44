import csv
import os
import pandas as pd
import re
print(os.getcwd())
os.chdir(r'c:\Users\saikat\Desktop\CS384_1801EE44\Assignment 4 Acad Results')
print(os.getcwd())
sem = []
sub = []
str = False
with open("acad_res_stud_grades.csv", 'r')as fi:
    reader = csv.reader(fi)

    i = 0

    pattern = re.compile(r'^\d+[A-Z]+\d+')
    for row in reader:
        for w in row:
            if re.match(pattern, w):
                if i == 0:
                    str = w
                break
        if row[1] == w:

            if w == str:
                with open(str+".csv", 'w', newline='') as fio:
                    writer = csv.writer(fio)
                    writer.writerow([row[4], row[5], row[8], row[6], row[2]])
            else:

                with open(str+".csv", 'w', newline='') as fio:
                    writer = csv.writer(fio)
                    writer.writerow(
                        [row[4], row[5], row[8], row[6], row[2], i])
            print(str)
        str = w
        i += 1
        if(i > 60):
            break
