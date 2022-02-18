'''
Importing and Hashing

In this program, we look at the (one) attendence sheet and compare it against the (twenty-six) class roster sheets. After the comparison is done, we have
built a dictionary with "First Name [space] Last Name" as the key and "95#" as the value. From there we hash each value and store that hashed value in the 
red black tree.
'''

import csv
import bcrypt
from red_black_tree_copy import Student, Node, rb_tree
import os
import glob

tree = rb_tree()
attendance = []
courses = []
database = {}
classCRN = {}
name_id = {}

# open the attendence sheet
with open('Attendance Sheet/Example Attendance Sheet.csv', 'r') as names_csv:
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

'''
MY CODE BEFORE INTEGRATION
path = 'private_data'
os.chdir(path)
result = glob.glob('*.{}'.format(extension))
'''

current_directory = os.getcwd()
get_files = glob.glob(os.path.join(current_directory, "Course Sheets", "*.csv"))
# x contains the specific excel file and its pathway
for x in get_files:
    course_info = x.rsplit("\\", 1)[1].rsplit(" ", 1)
    # Here I changed from [0:5] to [0:4] because we changed from .xlsx to .csv 
    course_info[1] = course_info[1][0:4]
    database.setdefault(x, course_info)
    classCRN.setdefault(course_info[1], course_info[0])
    courses.append(x)

    csv_rder = csv.reader(x)
    
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


'''for file in result:
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
'''

for key in name_id:
    hashed_name = bcrypt.hashpw(b"key", bcrypt.gensalt())
    id = name_id[key]
    hashed_id = bcrypt.hashpw(b"id", bcrypt.gensalt())

    # as of right now, our full_name is the key into the tree
    hashed_id = int(hashed_id)

    if tree.is_empty() == True or tree.find_node(hashed_id) == None:
            tree.insert(hashed_id, hashed_name)
        
    curr_node = tree.find_node(hashed_id)
    curr_node.student.add_classes(course_info[0])
    curr_node.student.add_crn(course_info[1])
    # TODO: alter red_black_tree to fit this
    # red_black_tree.Node(hashed_id, hashed_name)
    print(hashed_id)


tree.print_tree()