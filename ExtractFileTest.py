"""
Description:
------------
This file is designed for referencing and understanding how to apply Microsoft Excel files into Python Code
This program was made very informally and should be removed by the end of the project from GitHub
Feel free to comment out or in certain sections to focus on a particular one
"""

"""
Section 0: Import Statements
"""
# Access Excel Files with pandas
import pandas as pd
# Find your current working directory to work from
import os
# Be able to search through files in your directory
import glob

# Side Note: The os and glob modules work together to access the files in a specific directory (Section 3)


"""
Section 1: Opening an Excel File

Resources
https://datatofish.com/read_excel
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
"""

print("===========================================================================================")
# Side Note: You will need to change the path for .read_excel() since they are originally based off of my computer
# Opening an Excel file (You will need to get the path to access a specific file)
print("Section 1:\n")
print("Opening an Excel file:")
attendence_sheet = pd.read_excel(r"C:\Users\19894\Desktop\CIS 407 Project\Example Attendance Sheet.xlsx", dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int}) 
# Side Note: Identical column names have .# after the first one to differentiate them
print(attendence_sheet)


# Test with opening an excel file and having it stored in a list
course_list = []
class0 = pd.read_excel(r"C:\Users\19894\Desktop\CIS 407 Project\Example Course Sheet -- _ACTG 211 10368_.xlsx", dtype={"Student External ID": int, "Student First Name": str, "Student Last Name": str})
course_list.append(class0)
print("\nOpening an Excel file appended to a list:")
print(course_list[0])
print("===========================================================================================")

"""
Section 2: Accessing Cell Information

Resources
https://www.delftstack.com/howto/python-pandas/get-first-row-of-dataframe-pandas/
https://stackoverflow.com/questions/21393489/pandas-how-to-access-cell-in-pandas-equivalent-of-df3-4-in-r
"""
print("===========================================================================================")
print("Section 2: \n")
# Gather a specific column
print("Getting a specific column (Study Groups):")
print(attendence_sheet["Study Groups"]) 
print("\n")
print("Getting a specific column (Student External ID):")
print(course_list[0]["Student External ID"])
print("\n")

# Gather a specific Row (Note. row number starts at 0)
print("Getting a specific row (Atendance - Row 0):")
print(attendence_sheet.iloc[0])
print("\n")
print("Getting a specific row (Course - Row 1):") 
print(course_list[0].iloc[1])
print("\n")

# List the first n rows with header (Attendance - first 2 rows [0, 1])
print("Getting the first n rows with header (Attendance - first 2 rows [0, 2)):")
print(attendence_sheet.head(2))
print("\n")

# Access a specific cell (count starts at 0 and exclude headers)
print("Getting cell (0,0) from Course:")
print(course_list[0].iloc[0, 0])
print("\n")

# Get the length of row and cols of a file (count excludes headers)
print("Length:")
len_row = len(attendence_sheet)
len_col = len(attendence_sheet.columns) 
print(f"The attendence sheet has {len_row} rows and {len_col} columns")
print("\n")

"""
Section 3: Searching through Excel Files

Resources
https://www.geeksforgeeks.org/how-to-read-all-excel-files-under-a-directory-as-a-pandas-dataframe/
https://docs.python.org/3/library/os.path.html
"""
print("===========================================================================================")
print("Section 3:\n")

# Step 1: Get the current working directory with the os module
path = os.getcwd()
print("The current working directory:")
print(path)
print("\n")

print("All the files in the the current working directory:")
print(os.listdir(path))
print("\n")


# Step 2: Set up specific a variable to search for all excel files with the glob module
print("Listing all files (and the path) found in the \"Attendance Sheet\" file:")

# Side Note: join() connects different path components togeter and *.xlsx specifies what kind of files
get_files = glob.glob(os.path.join(path, "Attendance Sheet", "*.xlsx"))
print(get_files)
print("\n")


# Step 3: Set a loop to iterate through all files to read or store ()
print("Listing the location of all files found in the \"Course Sheets\" file:")
for x in get_files:
    file = pd.read_excel(x)
    print(x)
print("\n")

# Get the file name and CRN for a course (and add it to the list)
path = os.getcwd()    
get_files = glob.glob(os.path.join(path, "Course Sheets", "*.xlsx"))
course = []
crn = []
for x in get_files:
    # Side Note: split() based on the underscores(_) first then use rsplit to split class number and CRN
    class_info = x.split("_")[1].rsplit(" ", 1) 
    course.append(class_info[0])
    crn.append(class_info[1])

print("Printing the first excel file's class and CRN:")
print(f"{course[0]}\n{crn[0]}")
print("===========================================================================================")   