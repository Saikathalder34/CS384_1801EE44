import os
import re
import csv
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path = os.path.join(os.getcwd(), 'studentinfo_cs384.csv')


def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    pass


def country():
    try:
        os.mkdir(
            r"C:\Users\saikat\Desktop\CS384_1801EE44\Assignment\Assignment_3\analytics\country")
    except:
        pass
    with open("studentinfo_cs384.csv", 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                with open("analytics/country/"+row[2]+".csv",  'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
            i += 1
            # if i > 4:
            #     break


def course():
    pass


def email_domain_extract():
    try:
        os.mkdir(
            r"C:\Users\saikat\Desktop\CS384_1801EE44\Assignment\Assignment_3\analytics\email_domain")
    except:
        pass
    with open("studentinfo_cs384.csv", 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                mail = re.split('@', row[3])
                mail1 = re.split('\.', mail[1])
                email = mail1[0]
                with open("analytics/email_domain/"+email+".csv",  'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
            i += 1


def gender():
    try:
        os.mkdir(
            r"C:\Users\saikat\Desktop\CS384_1801EE44\Assignment\Assignment_3\analytics\gender")
    except:
        pass
    with open("studentinfo_cs384.csv", 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                with open("analytics/gender/"+row[4]+".csv",  'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
            i += 1
            # if i > 4:
            #     break


def dob():
    # Read csv and process
    pass


def state():
    try:
        os.mkdir(
            r"C:\Users\saikat\Desktop\CS384_1801EE44\Assignment\Assignment_3\analytics\state")
    except:
        pass
    with open("studentinfo_cs384.csv", 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                with open("analytics/state/"+row[7]+".csv",  'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
            i += 1
            # if i > 4:
            #     break


def blood_group():
    try:
        os.mkdir(
            r"C:\Users\saikat\Desktop\CS384_1801EE44\Assignment\Assignment_3\analytics\blood_group")
    except:
        pass
    with open("studentinfo_cs384.csv", 'r') as file:
        reader = csv.reader(file)
        i = 0
        for row in reader:
            if i != 0:
                with open("analytics/blood_group/"+(row[6])+".csv",  'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)
            i += 1
            # if i > 4:
            #     break


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass


country()
state()
blood_group()
gender()
email_domain_extract()
