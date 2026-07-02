# Write lambda function which accept one number and returns square of that number
square= lambda no1: no1*no1 
def main():
    value=int(input("Enter No:- "))
    ret = square(value)
    print("Square of given number is :-",ret)

if __name__ == "__main__":
    main()    
    
# Output:-
#C:\Users\Shree\Desktop\Assignment_14>python Question_1.py
#Enter No:- 5
#Square of given number is :- 25


