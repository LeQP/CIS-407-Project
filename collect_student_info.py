from red_black_tree import Student, Node, rb_tree
import pandas as pd
import os
import glob

tree = rb_tree()
attendance = []
courses = []
current_directory = os.getcwd()
# Collect the files for the attendance sheet and course sheets
get_files = glob.glob(os.path.join(current_directory, "Attendance Sheet", "*.xlsx"))
for x in get_files:
    file = pd.read_excel(x, dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int})
    attendance.append(file)
    
get_files = glob.glob(os.path.join(current_directory, "Course Sheets", "*.xlsx"))
for x in get_files:
    file = pd.read_excel(x, dtype={"Student External ID": int, "Student First Name": str, "Student Last Name": str})
    class_info = x.split("_")[1].rsplit(" ", 1)
    courses.append(file)
    
# Begin extracting first name, last name, and student id and putting it into RB tree
for file in courses:
    len_row = len(file)
    for x in range(0, len_row):
        if tree.is_empty() == True or tree.find_node(file.iloc[x,0]) == None:
            tree.insert(file.iloc[x, 0], file.iloc[x, 1], file.iloc[x, 2])
tree.print_tree()
    

        