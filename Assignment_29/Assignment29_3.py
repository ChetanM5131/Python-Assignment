# Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys
if len(sys.argv) < 3:
    print("Enter File Name as argument")

def main():
    try:
        rfile=sys.argv[1]
        wfile=sys.argv[2]
    
        fobj=open(rfile,"r")
        fobj2=open(wfile,"w")

        file=fobj.read()
        fobj2.write(file)

        print("File copy completed")

        fobj.close()
        fobj2.close()
    
    except FileNotFoundError as fobj:
        print("File not present in current directory")     

if __name__ == "__main__":
    main()