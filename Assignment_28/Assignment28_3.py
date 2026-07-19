# Q3) Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

import sys

if len(sys.argv) < 2:
    print("Enter file name as command line argument:-")

def main():
    try:
        filename=sys.argv[1]
        fobj=open(filename,"r")


        for i in fobj:

            print(i,end="")
            
        fobj.close()  

        # ************* Using splitlines() ******************
        #fobj.seek(0)
        #file=fobj.read()
        #line=file.splitlines()
        #for i in line:
        #    print("Using splitlines():-",i) 
        #fobj.close()
            

    except FileNotFoundError as fobj:
        print("File not present in current directory")


if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_28>python Assignment28_3.py Demo.txt
# Jay Ganesh...
# This
# is
# demo
# file
# to
# count the number of lines and
# count the number of words    