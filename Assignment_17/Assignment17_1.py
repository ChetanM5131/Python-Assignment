# Create module Arithmetic which contains Add(),sub(),mult() and div() 
# Write a program which called module Arithmetic and perform Add,substract, Mult and Div

import Arithmetic
def main():
    x=int(input("Enter No1:- "))

    x1=int(input("Enter No2:-"))

    ret=Arithmetic.Add(x,x1)
    print(f"Addition of {x} and {x1} is :-",ret)

    ret=Arithmetic.Sub(x,x1)
    print(f"Substraction of {x} and {x1} is :-",ret)

    ret=Arithmetic.Mult(x,x1)
    print(f"Multiplication of {x} and {x1} is :-",ret)

    
    ret=Arithmetic.Div(x,x1)
    print(f"Division of {x} and {x1} is :-",ret)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_1.py
#Enter No1:- 15
#Enter No2:-5
#Addition of 15 and 5 is :- 20
#Substraction of 15 and 5 is :- 10
#Multiplication of 15 and 5 is :- 75
#Division of 15 and 5 is :- 3.0

    