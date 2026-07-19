# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.
import sys

def main():
    if len(sys.argv) < 2:
        print("Enter the file name as Argument")

    try:
        cnt=0
        filename=sys.argv[1]
        fobj=open(filename,"r")
               
        
        for i in fobj:
            cnt+=1
        
        print(f"Totla number of lines in file {fobj.name}:-",cnt)    
        # Option 2 using readlines()
        fobj.seek(0)
        
        print(f"Totl number of lines in {fobj.name} is:-",len(fobj.readlines()))
    
    except FileNotFoundError as fobj:
        print("File not present in current directory") 


if __name__ == "__main__":
    main()    

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_28>python Assignment28_1.py Demo.txt
# Totla number of lines in file Demo.txt:- 8
# Totl number of lines in Demo.txt is:- 8

#C:\Users\Shree\Desktop\Assignments\Assignment_28>    