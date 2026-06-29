#Write a program which accept a number and print all even number till that program
def main ():
    
    tbl=int(input("Enter the number :-"))

    print("Even Numbers till ",str(tbl) + ":-")

    for i in range(1,tbl+1):
        if (i%2 ==0):
           print(i,end=" ")   

if __name__ == "__main__":
    main() 


#Output:-
#C:\Users\Shree\Desktop\Assignment_10>python Question_4.py
#Enter the number :-15
#Even Numbers till  15:-
#2 4 6 8 10 12 14
