# Write a program to accept 2 numbers and perform addition,substraction,multiplication,division
def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mult(no1,no2):
    return no1*no2

def div(no1,no2):
    if no2==0:
        print("divisor should not be 0")
    else:
        return no1/no2      
      

def main():
    no1=int(input("Enter no1 :-"))
    no2=int(input("Enter no2 :-"))

    print("Addition of given numbers is :-",add(no1,no2))

    print("Substraction of given numbers is :-",sub(no1,no2))

    print("Multiplication of given numbers is :-",mult(no1,no2))

    print("Division of given numbers is :-",div(no1,no2))

if __name__ == "__main__":
    main()    

#output
#C:\Users\Shree\Desktop\Assignment_12>python Question_3.py
#Enter no1 :-12
#Enter no2 :-4
#Addition of given numbers is :- 16
#Substraction of given numbers is :- 8
#Multiplication of given numbers is :- 48
#Division of given numbers is :- 3.0

    