# Write program to accept one number and prints its cube number

def cube(val1):
    return val1*val1*val1

def main():
    
    no1=int(input("Enter Number:- "))
    ret=cube(no1)
    
    print("Cube of given number is :-",ret)

if __name__ == "__main__":
    main()

#Output:-
#C:\Users\Shree\Desktop\Assignment_9>python Question_4.py
#Enter Number:- 3
#Cube of given number is :- 27

