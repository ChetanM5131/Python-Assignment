# Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not. 

import sys
import os

if len(sys.argv) < 2:
    print("Enter the File Name as Argument")

def main():
    filename=sys.argv[1]
    flg=False
    for FolderName,SubFolder,FileName in os.walk("."):
        for fname in FileName:
            if fname==filename:
                flg=True
    if flg==True:
        print("File is Present")
    else:
        print("File not present")                    


if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_29>python Assignment29_1.py Demo.txt
# File is Present
    
