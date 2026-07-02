# Write a program to accept the lambda function using filter() which accept the list from user and return even numbers
even_odd=lambda x: x%2==0

def main():

    data=[13,12,8,10,11,20]
    print("Input data is :",data)
    f_data=list(filter(even_odd,data))   

    print("List of Even numbers is:- ",f_data) 

if __name__ == "__main__":
    main()


#Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_2.py
#Input data is : [13, 12, 8, 10, 11, 20]
#List of Even numbers is:-  [12, 8, 10, 20]

    