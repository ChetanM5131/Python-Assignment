# Write a program to accept number as input from user and print all previous numbers till 1
def num_print(no1):
    

    for i in range(1,no1+1):
        
        print(no1,end="")
        no1=no1-1
    
def main():
    no1=int(input("Enter the number :-"))
    ret=num_print(no1)
    

if __name__ == "__main__":
    main()

#Output:-
#C:\Users\Shree\Desktop\Assignment_12>python Question_5.py
#Enter the number :-4
#4321
#C:\Users\Shree\Desktop\Assignment_12>python Question_5.py
#Enter the number :-6
#654321
