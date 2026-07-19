# Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

import os
import sys
if len(sys.argv) < 2:
    print("Enter File Name as argument")
def main():
    try:

        filename=sys.argv[1]
        fobj=open(filename,"r")
        file=fobj.read()
        print(file)

    except FileNotFoundError as fobj:
        print("File not present in current directory")    

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_29>python Assignment29_2.py Demo.txt
# Jay Ganesh...
# This
# is
# demo
# file
# to
# count the number of lines and
# count the number of words    