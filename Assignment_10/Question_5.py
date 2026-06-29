#Write a program which accept a number and print all odd number till that program
def main ():
    
    no1=int(input("Enter the number :-"))

    print("Odd Numbers till ",str(no1) + ":-")

    for i in range(1,no1+1):
        if (i%2 ==1):
           print(i,end=" ")   

if __name__ == "__main__":
    main() 


#Output:-
#C:\Users\Shree\Desktop\Assignment_10>python Question_5.py
#Enter the number :-12
#Even Numbers till  12:-
#1 3 5 7 9 11
