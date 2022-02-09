'''
Importing and Hashing

In this program, we look at the (one) attendence sheet and compare it against the (twenty-six) class roster sheets. After the comparison is done, we have
built a dictionary with "First Name [space] Last Name" as the key and "95#" as the value. From there we hash each value and store that hashed value in the 
red black tree.
'''

import csv
import bcrypt
# import red_black_tree
import os
import glob

# read attendence csv

name_id = {}

with open('names.csv', 'r') as names_csv:
    csv_rder = csv.reader(names_csv)
    
    # each row is a list of names
    # each name is stored like Last, First \n
    # first, we want to separate the csv by name
    for row in csv_rder:
        for name in row:
            l_f = name.split('\n')
            for last_first in l_f:
                broken = last_first.split(', ')
                last_name = broken[0]
                first_name = broken[1]
                # going to store student name as first name [space] last name
                stud_name = first_name+' '+last_name
                # all values will be initialized to zero
                if(stud_name not in name_id):
                    name_id[stud_name] = 0
                # else:
                    # TODO: attendence_count += 1

# now I have a dictionary that stores the First Name [space] Last Name as the key and the student ID as the value

path = 'private_data'
extension = 'csv'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))

for file in result:
    with open(file, 'r') as my_file:
        csv_rder = csv.reader(my_file)
    
        # each row is a list of names
        # each name is stored like Last, First \n
        # first, we want to separate the csv by name
        for row in csv_rder:
            id = row[0]
            first_name = row[1]
            last_name = row[2]
            stud_name = first_name+' '+last_name
            if(stud_name in name_id):
                name_id[stud_name] = id

for key in name_id:
    hashed_name = bcrypt.hashpw(b"key", bcrypt.gensalt())
    id = name_id[key]
    hashed_id = bcrypt.hashpw(b"id", bcrypt.gensalt())
    # TODO: alter red_black_tree to fit this
    # red_black_tree.Node(hashed_id, hashed_name)