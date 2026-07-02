# Write a lmabda function using reduce() which accept list of numbers and return minumun of its element
from functools import reduce
min_element=lambda x,x1:min(x,x1)
def main():
    data=[1,2,3,4,9,5,6]

    print("Element is List :-",data)

    r_data=reduce(min_element,data)
    print("Minimum element of list is:-",r_data)

if __name__ == "__main__":
    main()


# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_6.py
#Element is List :- [1, 2, 3, 4, 9, 5, 6]
#Minimum element of list is:- 1

    