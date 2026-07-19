#Frequency of a String in File
#Problem Statement:
#Write a program which accepts a file name and one string from the user and returns the frequency (count of
#occurrences) of that string in the file.
#Input:
#Demo.txt Marvellous
#Expected Output:
#Count how many times "Marvellous" appears in Demo.txt.
import sys

if len(sys.argv) < 3:
    print("enter file name and word we need to search in file")

def main():
    try:
        readfile=sys.argv[1]
        searchword=sys.argv[2]

        fobj=open(readfile,"r")

        cnt=0
        lineno=1
        for i in fobj:
            chk_word=i.split()

            if searchword in i.split():
              line_word_cnt=chk_word.count(searchword)
              cnt+=line_word_cnt
            lineno +=1  

        if cnt > 0:
             print(f"Total frequency of '{searchword}' is:-",cnt)
        else:
            print(f"word '{searchword}' not found in file") 


    except FileNotFoundError as fobj:
        print("File not present in current directory")
    

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignments\Assignment_29>python Assignment29_5.py Demo1.txt Marvellous
# Total frequency of 'Marvellous' is:- 6

# Input file Demo1.txt
#Marvellous Marvellous Marvellous
#Marvellous Info Systems Marvellous
#Marvellous
