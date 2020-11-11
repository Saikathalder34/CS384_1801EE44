import csv
import os
import pandas as pd
import re
print(os.getcwd())
os.chdir(r'c:\Users\saikat\Desktop\CS384_1801EE44\Assignment4')
print(os.getcwd())

with open("acad_res_stud_grades.csv", 'r')as fi:
    reader = csv.reader(fi)
    i = 0
    pattern = re.compile(r'^\d+[A-Z]+\d+')
    for row in reader:
        for w in row:
            if re.match(pattern, w):
                if i != 0:     # no point if this not there
                    str = w
                    break      # next for loop for break

        for w in row:
            if re.match(pattern, w):
                if row[1] == str:
                    if w != old_str:
                        with open("grades/"+w + "_individual.csv", 'a', newline='') as fi:
                            writer = csv.writer(fi)
                            writer.writerow(["Roll:"+w, '', '', '', ''])
                            writer.writerow(
                                ["Semester Wise Details", '', '', '', ''])
                            writer.writerow(
                                ["Subject", "Credits", "Type", "Grade", "Sem"])
                    with open("grades/"+w + "_individual.csv", 'a', newline='') as fio:
                        writer = csv.writer(fio)
                        writer.writerow(
                            [row[4], row[5], row[8], row[6], row[2]])
                        str = row[1]
        old_str = str
        i += 1
