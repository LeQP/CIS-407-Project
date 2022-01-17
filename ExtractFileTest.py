
# This file is designed to help people understand
# Feel Free to comment out or in certain sections to focus on a particular one


import pandas as pd
import os
import glob


# Test with opening an excel file (https://datatofish.com/read_excel/)
#   Will need to get the path to access a specific file


attendence_sheet = pd.read_excel(r"C:\Users\19894\Desktop\CIS 407 Project\Example Attendance Sheet.xlsx", dtype={"Attendance Date": str, "Study Groups": str, "Attended": str, "Number of Group Participants": int, "Attended.1": int}) # Identical columns have .# after the first one
print(attendence_sheet)


# Test with opening an excel file and having it stored in a list (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)
course_list = []
class0 = pd.read_excel(r"C:\Users\19894\Desktop\CIS 407 Project\Example Course Sheet -- _ACTG 211 10368_.xlsx", dtype={"Student External ID": int, "Student First Name": str, "Student Last Name": str})
course_list.append(class0)
print(course_list[0])


# Access a specifc row and col and length (https://www.delftstack.com/howto/python-pandas/get-first-row-of-dataframe-pandas/)
#   Col
print(attendence_sheet["Study Groups"]) 
print(course_list[0]["Student External ID"])

#   Row
#print(attendence_sheet.iloc[0] + "\n") # Prepose with the col category followed the row value

print(course_list[0].iloc[0])
#   List the first n rows with header
print(attendence_sheet.head(2))


#   Access a specific cell (start at 0 and exclude headers) (https://stackoverflow.com/questions/21393489/pandas-how-to-access-cell-in-pandas-equivalent-of-df3-4-in-r)
print(course_list[0].iloc[0, 0])


#   Get the length of row and cols of a file (count excludes headers)
len_row = len(attendence_sheet)
len_col = len(attendence_sheet.columns) 
print(f"The attendence sheet has {len_row} rows and {len_col} columns")


# Access the current working directory (for collecting all the excel files stored in a directory)
# Step 1: Get the current working directory with the os module
path = os.getcwd()
print(os.listdir(path))
print(path)
# Step 2: Set up specific a variable to search for all excel files with the glob module
get_files = glob.glob(os.path.join(path, "Attendance Sheet", "*.xlsx"))
print(get_files)
# Step 3: Set a loop to iterate through all files to read or store (https://www.geeksforgeeks.org/how-to-read-all-excel-files-under-a-directory-as-a-pandas-dataframe/)
# https://docs.python.org/3/library/os.path.html
for x in get_files:
    file = pd.read_excel(x)
    print(f"Location: {x}\n")

# Get the file name and CRN for a course
path = os.getcwd()    
get_files = glob.glob(os.path.join(path, "Course Sheets", "*.xlsx"))