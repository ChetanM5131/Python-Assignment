# Write a program to accept n numbers from user and stored it into list and print the sum of numbers in list
from functools import reduce

add_no=lambda x,x1: x+x1
    
def main():
    lst=[]
    no1=int(input("Enter how many numbers need to insert into list:-"))
    
    for i in range(1,no1+1):
        ele=int(input("Enter the element of List:-"))
        lst.append(ele)
    
    r_data=reduce(add_no,lst)

    print("Addition of list elements is :-",r_data)



if __name__ =="__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_18>python Assignment18_1.py                                                            
# Enter how many numbers need to insert into list:-4                                                                       
# Enter element of list:-1                                                                                                 
# Enter element of list:-2                                                                                                 
# Enter element of list:-3                                                                                                 
# Enter element of list:-4                                                                                                 
# Sum of list elements := 10                                                                                                                                                                                                                       
#  C:\Users\Shree\Desktop\Assignment_18>   