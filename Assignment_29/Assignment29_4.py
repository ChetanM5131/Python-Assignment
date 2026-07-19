# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys
import os

if len(sys.argv) < 3:
    print("Enter file names as input arguments")


def main():
    try:
        fname1=sys.argv[1]
        fname2=sys.argv[2]

        fobj1=open(fname1,"r")
        fobj2=open(fname2,"r")

        ret1=fobj1.read()

        ret2=fobj2.read()

        if ret1 == ret2:
            print("Success")
        else:
            print("Failure")    

    except FileNotFoundError as fobj:
        print("File not present in current directory")


if __name__ == "__main__":
    main()

#C:\Users\Shree\Desktop\Assignments\Assignment_29>python Assignment29_4.py Demo.txt copy.txt
#Success

#C:\Users\Shree\Desktop\Assignments\Assignment_29>python Assignment29_4.py Demo.txt file2.txt
#Failure

