# I HAVE NOT ENTIRELY WRITTEN WHOLE ROLL NO. DATA INTO MISC.CSV. I HAVE ONLY WRITTEN ROW NOT HAVING SEM_CREDITS
import csv
import os
import pandas as pd
import re
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path = os.path.join(os.getcwd(), 'acad_res_stud_grades.csv')


grade_cnvrt = {'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7,
               'CC': 6, 'CD': 5, 'DD': 4, 'F': 0, 'I': 0}

# OPENING ACAD_RES...FILE AND CREATING MISC.CSV
with open("acad_res_stud_grades.csv", 'r')as fi, open("grades/misc.csv", 'a', newline='')as misc:
    reader = csv.reader(fi)
    write_misc = csv.writer(misc)
    write_misc.writerow(["Roll", "Subject", "Credits", "Type", "Grade", "Sem"])

    i = 0
    pattern = re.compile(r'^\d+[A-Z]+\d+')  # pattern for roll no match
    pattern1 = re.compile(r'^\d')  # pattern for integer in SEM no.
    t_credits, t_cl_credits = 0, 0
    sem_credits = 0
    sem_clr_credits = 0
    sum1 = 0  # USED FOR SPI CALCULATION
    sum2 = 0  # USED FOR CPI CALCULATION

    # MAIN FOR LOOP
    for row in reader:

        # GETTING ROLL NUMBER
        for w in row:
            if re.match(pattern, w) and i != 0:
                str = w  # STR = CURRENT ROLL_NO
                break
        # WRITING ON FILE BEGIN
        for w in row:
            if re.match(pattern, w):
                if row[1] == str:
                    # I HAVE ONLY WRITTEN(MISC.CSV) ROW NOT HAVING SEM_CREDITS ,NOT ENTIRE ROLL NO.
                    if row[6] == '':
                        write_misc.writerow(
                            [row[1], row[4], row[5], row[8], row[6], row[2]])
                        break

                    if w != old_str:
                        # ROLL_INDIVIDUAL.CSV BASIC INFORMATION
                        with open("grades/"+w + "_individual.csv", 'a', newline='') as fi:
                            writer = csv.writer(fi)
                            writer.writerow(["Roll:"+w, '', '', '', ''])
                            writer.writerow(
                                ["Semester Wise Details", '', '', '', ''])
                            writer.writerow(
                                ["Subject", "Credits", "Type", "Grade", "Sem"])

                        # WRITING ON ROLL_OVERALL.CSV BASIC INFORMATION
                        with open("grades/"+w+"_overall.csv", 'a', newline='') as fi:
                            writer = csv.writer(fi)
                            writer.writerow(["Roll:"+w, '', '', '', ''])
                            writer.writerow(
                                ["Semester", 'Semester Credits', 'Semester Credits Cleared', 'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI'])

                    # WRITING ON ROLL_INDIVIDUAL.CSV
                    with open("grades/"+w + "_individual.csv", 'a', newline='') as fio:
                        writer = csv.writer(fio)
                        writer.writerow(
                            [row[4], row[5], row[8], row[6], row[2]])
                        str = row[1]

                    # WRITING ON ROLL_OVERALL.CSV FILE
                    if old_sem != row[2] and i != 0 and re.match(pattern1, old_sem):
                        with open("grades/" + old_str + "_overall.csv", "a", newline='') as g:
                            writer1 = csv.writer(g)

                            # CPI
                            sum2 += spi*sem_credits
                            writer1.writerow(
                                [old_sem, sem_credits, sem_clr_credits, round(spi, 2), t_credits, t_cl_credits, round(sum2/t_credits, 2)])
                            # FOR NEXT ROLL BELOW PARAMETER ASSIGN 0
                            sem_credits = 0
                            sem_clr_credits = 0
                            sum1 = 0

                    # CREDITS SUMMATION
                    if w != old_str:
                        t_credits, t_cl_credits, sum2 = 0, 0, 0
                    t_credits += int(row[5])
                    sem_credits += int(row[5])
                    sem_clr_credits = sem_credits
                    t_cl_credits = t_credits

                    # REDUCING CREDITS IF GETS "F"|"I"
                    if row[6] == 'F' or row[6] == 'I':
                        sem_clr_credits -= int(row[5])
                        t_cl_credits -= int(row[5])
                    # SPI
                    sum1 += int(row[5])*grade_cnvrt[row[6]]
                    spi = sum1/sem_credits

        old_str = str  # ASSIGNING CURRENT ROLL NO. FOR NEXT LOOP
        old_sem = row[2]  # ASSIGNING CURRENT SEMESTER NO. FOR NEXT LOOP

        i += 1

    # END OF MAIN FORLOOP

    # WRITE LAST ROW (OUTSIDE MAIN FORLOOP)
    with open("grades/"+old_str+"_overall.csv", "a", newline='') as g:
        writer = csv.writer(g)
        sum2 += spi*sem_credits

        writer.writerow([old_sem, sem_credits, sem_clr_credits, round(
            spi, 2), t_credits, t_cl_credits, round(sum2/t_credits, 2)])
