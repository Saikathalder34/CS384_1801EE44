import os
import re
import csv
import math

# FUNCTION STARTS


def group_allocation(filename, number_of_groups):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(
        os.getcwd(), filename)

    pattern = re.compile(r"\d{4}[A-Z]+")
    # for stats_grouping.csv's heading line
    stats_header_list = ["group", "total"]
    br_dict = {}  # Dict Having key=branch_name and value=student in each grp
    i = 0
    count = 0    # USE IN FOR LOOP
    total_grp = number_of_groups

    # OPENING MAIN WORKING FILE
    with open("Btech_2020_master_data.csv", 'r') as f:
        reader = csv.reader(f)
        prv_branch = ''  # PREVIOUS BRANCH VALUE

        # FOR LOOP ACCESSING EACH ROW OF MAIN FILE
        for row in reader:
            if re.search(pattern, row[0]):
                branch = row[0]
                m = branch[4]+branch[5]  # M=BRANCH NAME
                # CREATING FILE FOR EACH BRANCH
                with open("groups/"+m+".csv", 'a', newline='')as nf:
                    writer = csv.writer(nf)
                    writer.writerow([row[0], row[1], row[2]])
                    # M=CURRENT BRANCH (IF PRVIOUS BRANCH NOT MATCH)
                    if m != prv_branch:

                        if i != 1:
                            n = math.floor(count/total_grp)
                            br_dict[prv_branch] = 0

                            # WRITING STUDENTS DETAIL IN EACH GROUP
                            with open("groups/"+prv_branch+".csv", 'r') as ni:
                                reader1 = csv.reader(ni)
                                # K FOR WRITING n VALUES, J FOR REGULATING GRP NO.
                                k, j = 0, 1

                                for r in reader1:
                                    if re.search(pattern, r[0]):
                                        if j > total_grp:
                                            with open("left.csv", 'a', newline='') as left:
                                                writer2 = csv.writer(left)
                                                writer2.writerow(r)
                                        else:
                                            with open("groups/Group_G"+str(j).zfill(2)+".csv", 'a', newline='') as grp:
                                                writer1 = csv.writer(grp)
                                                writer1.writerow(r)
                                        k += 1
                                    if k == n:  # IF K=n THEN MOVING TO NEXT GRP
                                        j += 1
                                        k = 0
                        # write name roll
                        with open("groups/"+m+".csv", 'a', newline='') as nf:
                            writer = csv.writer(nf)
                            writer.writerow(["Roll", "Name", "Email"])
                            stats_header_list.append(m)
                            count = 0

                prv_branch = m
                count += 1

            i += 1
    # FOR LOOP ENDS

    # WRITING REMAINING VALUES
    n = math.floor(count/total_grp)
    br_dict[prv_branch] = n
    with open("groups/"+prv_branch+".csv", 'r') as ng:
        reader4 = csv.reader(ng)
        k, j = 0, 1
        for r in reader4:
            if re.search(pattern, r[0]):
                if j > total_grp:
                    with open("left.csv", 'a', newline='') as left:
                        writer2 = csv.writer(left)
                        writer2.writerow(r)
                else:
                    with open("groups/Group_G"+str(j).zfill(2)+".csv", 'a', newline='') as grp:
                        writer1 = csv.writer(grp)
                        writer1.writerow(r)
                k += 1

            if k == n:
                j += 1
                k = 0

    j = 1  # NEW VALUE OF J FOR BELOW LOOP

    # DISTRIBUTING LEFT STUDENTS IN ECAH GRP
    with open("left.csv", 'r') as lft:
        reader3 = csv.reader(lft)
        for r2 in reader3:
            r2[0][4]+r2[0][5]
            with open("groups/Group_G"+str(j).zfill(2)+".csv", 'a', newline='') as g:
                writer3 = csv.writer(g)
                writer3.writerow(r2)
                j += 1

            if j > total_grp:
                j = 1

    # WORKING ON STATS_GROUPING.CSV
        with open("groups/stats_grouping.csv", 'a', newline='')as stats:
            writer4 = csv.writer(stats)
            writer4.writerow(stats_header_list)
        dummy_list = []  # IT HAS BEEN USED FOR WRITING EACH ROW IN STATS_GRP.CSV
        total_stud = 0
        for j in range(1, total_grp+1):  # ACCESSING EACH GRP
            with open("groups/Group_G"+str(j).zfill(2)+".csv", 'r') as g:
                reader3 = csv.reader(g)
                dummy_list.append("Group_G"+str(j).zfill(2)+".csv")
                for row in reader3:
                    total_stud += 1
                    br = row[0][4]+row[0][5]
                    br_dict[br] += 1
                dummy_list.append(total_stud)
                for key in br_dict:
                    dummy_list.append(br_dict[key])
                    br_dict[key] = 0
                total_stud = 0
            with open("groups/stats_grouping.csv", 'a', newline='')as sta:
                writer5 = csv.writer(sta)
                writer5.writerow(dummy_list)
            dummy_list = []
    os.remove("left.csv")
# Group_allocation FUNCTION END


############ MAIN BEGIN###############
filename = "Btech_2020_master_data.csv"
number_of_groups = 12
group_allocation(filename, number_of_groups)
