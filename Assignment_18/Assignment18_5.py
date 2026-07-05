# Write the program which accept N numbers from user and store it into list.
# Return addition of prime numbers from that list
# Main python file accept N numbers from user and pass each number to ChkPrime() which is part of out module MarvellousNum
# Name of function in main python file is ListPrime()
import MarvellousNum
from functools import reduce

prime_demo=lambda val1:MarvellousNum.ChkPrime(val1)

add_element=lambda t1,t2:t1+t2

def main():
    lst=[]
    no1=int(input("Enter how many numbers  into list:- "))

    for i in range(1,no1+1):
        x=int(input("enter number to insert into list:-"))
        lst.append(x)

    f_data=list(filter(prime_demo,lst)) 

    print("data after filter:",f_data)  

    r_data=reduce(add_element,f_data)
    print("Sum of prime numbers from list is:-",r_data)  
    


if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_18>python Assignment18_5.py
#Enter how many numbers  into list:- 11
#enter number to insert into list:-13
#enter number to insert into list:-5
#enter number to insert into list:-45
#enter number to insert into list:-7
#enter number to insert into list:-4
#enter number to insert into list:-56
#enter number to insert into list:-10
#enter number to insert into list:-34
#enter number to insert into list:-2
#enter number to insert into list:-5
#enter number to insert into list:-8
#data after filter: [13, 5, 7, 2, 5]
#Sum of prime numbers from list is:- 32

    