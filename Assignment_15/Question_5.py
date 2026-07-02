# Write a lmabda function using reduce() which accept list of numbers and return maximum of its element
from functools import reduce
max_element=lambda x,x1:max(x,x1)
def main():
    data=[1,2,3,4,9,5,6]

    print("Element is List :-",data)

    r_data=reduce(max_element,data)
    print("Max element of list is:-",r_data)

if __name__ == "__main__":
    main()


# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_5.py
#Element is List :- [1, 2, 3, 4, 9, 5, 6]
#Max element of list is:- 9

    