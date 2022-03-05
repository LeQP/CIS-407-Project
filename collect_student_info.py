"""
collect_student_info: A program made to read different excel files containing information 
regarding Class Encore attendance and specific class rosters, including the class name and CRN; the
information collected gets stored in a red-black tree to access later on.

"""
# Side Note: Program will not work correctly if any of the Excel files are opened on the computer
# Import statements to use a red-black tree and modules for accessing Excel files.
from red_black_tree import Student, Node, rb_tree
import pandas as pd
import os
import glob

# Declare variables to use throughout the program or for relevant information access
tree = rb_tree()
attendance = [] # Stores the attendance sheets' pathways to access
courses = []    # Stores the course sheets' pathways to access
database = {}   # Stores each couse sheets' pathways as a key to access each course's class and CRN as a value
classCRN = {}   # Stores a class's CRN as a key to access the class name as a value
current_directory = os.getcwd()

# Collect the file pathways for the attendance sheet
# x contains the specific excel file and its pathway
get_files = glob.glob(os.path.join(current_directory, "Attendance Sheet", "*.xlsx"))
for x in get_files:
    attendance.append(x)

# Collect the file pathways for the course sheets
# x contains the specific excel file and its pathway

get_files = glob.glob(os.path.join(current_directory, "Course Sheets", "*.xlsx"))
for x in get_files:
    # Remove all the extra characters from the pathway to leave only the class name and CRN
    course_info = x.rsplit("\\", 1)[1].rsplit(" ", 1)
    course_info[1] = course_info[1][0:5] # Remove the ".xlsx" attached to each CRN
    # Add relevent info to the dictionaries and course list
    database.setdefault(x, course_info)
    classCRN.setdefault(course_info[1], course_info[0])
    courses.append(x)
    
# Extract first name, last name, and student id from each course sheet (represented by x)
# and place that information into a node for the red-black tree
for x in courses:
    # Reads the file and get the neccessary values to begin storage
    file = pd.read_excel(x, dtype={"Student External ID": int, "Student First Name": str, "Student Last Name": str})
    len_row = len(file)
    course_info = database.get(x)
    
    # Read through each row in a course sheet to acquire information for storage
    for i in range(0, len_row):
        # Add student in tree if not already there
        if tree.is_empty() == True or tree.find_node(file.iloc[i, 0]) == None:
            tree.insert(file.iloc[i, 0], file.iloc[i, 1], file.iloc[i, 2])
        
        # Insert a student's class and CRN into their node 
        curr_node = tree.find_node(file.iloc[i,0])
        curr_node.student.add_classes(course_info[0])
        curr_node.student.add_crn(course_info[1])

# Read through the attendance sheet to count how many Class Encore sessions that a student, within any
# of the course sheets, has attended
for x in attendance:
    # Reads the file and get the neccessary values to begin gathering a count
    file = pd.read_excel(x, dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int})
    len_row = len(file)

    # Read through all the names contained in the second column of the attendance sheet (row represented by i)
    for i in range(0, len_row):
        # Each cell can contain multiple names and need to be breaken down
        names = file.iloc[i, 2].split("\n ")

        # All the names in a cell get stored into its own list for access (each full name represented by j)
        for j in names:
            # Will need to remove an extra space (" ") found at the first name
            if j[0] == " ": 
                j = j[1:len(j)] 
            
            # Seperate first and last name to check for name on the tree to count their attendance
            name = j.split(", ")
            curr_node = tree.find_name(name[1], name[0])
            if curr_node != None:
                curr_node.student.add_attended()

# Different ways to print the tree (the entire tree or a specific name or 95-number)       
  
tree.print_tree()
tree.print_specific(first="Gaston", last="Bowers")
tree.print_specific(id=951718481)

    


        