# Write a lmabda function using reduce() which accept list of numbers and return sum of its element
from functools import reduce

add_no=lambda x,x1: x+x1

def main():
    
    data=[1,2,3,4,5,6,7,8,9]
    print("List of number is :-",data)

    r_data=reduce(add_no,data)

    print("Addition of list elements is :-",r_data)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_4.py
#List of number is :- [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Addition of list elements is :- 45

    