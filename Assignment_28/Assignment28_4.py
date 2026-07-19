# Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt

import sys

if len(sys.argv) < 3:
    print("Enter 2 file names as commonad line arguments:")
    sys.exit()
 
    

def main():
    try:
        readfile=sys.argv[1]
        wfile=sys.argv[2]

        robj=open(readfile,"r")
        wobj=open(wfile,"w")

        file=robj.read()
        wobj.write(file)

        print("Data written successfully")

        robj.close()
        wobj.close()

    except FileNotFoundError as fobj:
        print("File not present in current directory")

if __name__ =="__main__":
    main()





