# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import sys

def main():
    if len(sys.argv) < 2:
        print("Enter the file name as Argument")

    try:
        cnt=0
        filename=sys.argv[1]
        fobj=open(filename,"r")
               
        file=fobj.read()
        wordlist=file.split()
        print(wordlist)
        wordcnt=len(wordlist)
        print(f"Number of word list in file {fobj.name} :-",wordcnt)
        
 
    except FileNotFoundError as fobj:
        print("File not present in current directory") 


if __name__ == "__main__":
    main() 
# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_28>python Assignment28_2.py Demo.txt
# ['Jay', 'Ganesh...', 'This', 'is', 'demo', 'file', 'to', 'count', 'the', 'number', 'of', 'lines', 'and', 'count', 'the', 'number', 'of', 'words']
# Number of word list in file Demo.txt :- 18

    