# Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
import sys

if len(sys.argv) < 3:
    print("enter file name and word we need to search in file")

def main():
    try:
        readfile=sys.argv[1]
        searchword=sys.argv[2]

        fobj=open(readfile,"r")

        wordfound=False
        lineno=1
        for i in fobj:
            if searchword in i.split():
                print(f"word '{searchword}' found in file")
                wordfound=True
            lineno+=1    

        if wordfound==False:
            print(f"word {searchword} not found in file")   
    except FileNotFoundError as fobj:
        print("File not present in current directory")
    

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_28>python Assignment28_5.py Demo.txt count
# word 'count' found in file 
# word 'count' found in file 
