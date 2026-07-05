# Write a program to accept n numbers from user and stored it into list and print the max element in list
from functools import reduce

max_element=lambda x,x1: max(x,x1)
    
def main():
    lst=[]
    no1=int(input("Enter how many numbers need to insert into list:-"))
    
    for i in range(1,no1+1):
        ele=int(input("Enter the element of List:-"))
        lst.append(ele)
    
    r_data=reduce(max_element,lst)

    print("Max elements is :-",r_data)



if __name__ =="__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_18>python Assignment18_2.py
#Enter how many numbers need to insert into list:-3
#Enter the element of List:-11
#Enter the element of List:-21
#Enter the element of List:-9
#Max elements is :- 21

    