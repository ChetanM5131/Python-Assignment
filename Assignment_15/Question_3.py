# Write a lambda function using filter() which accept list of numbers and return list of odd numbers

odd_no = lambda x: x%2==1
 
def main():
    
    data=[1,2,3,4,5,6,7,8,9,10]

    print("Input number list is :-",data)

    f_data=list(filter(odd_no,data))

    print("List of ODD numbers is :-",f_data)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_3.py
#Input number list is :- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#List of ODD numbers is :- [1, 3, 5, 7, 9]

    