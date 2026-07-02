# Write a lambda function using reduce() which accept list of numbers and return product of all elements in list
from functools import reduce

prod_element=lambda x,x1: x*x1

def main():

    data=[2,3,5,10]
    print("Elements of list :-",data)

    r_data=reduce(prod_element,data)

    print("Product of elements of list :-",r_data)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_10.py
#List of Numbers:-  [1, 3, 5, 6, 9, 10, 15, 30]
#List of even numbers:-  [6, 10, 30]
#Count of Even elements :- 3

    