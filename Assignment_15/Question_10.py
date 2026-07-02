# Write a lambda function using filter() which accept list of numbers and return list of numbers divisible by 3 and 5
count_even=lambda x: x%2==0

def main():

    data=[1,3,5,6,9,10,15,30]
    print("List of Numbers:- ",data)

    even_data_lst=list(filter(count_even,data))
    print("List of even numbers:- ",even_data_lst)

    f_data=len(list(filter(count_even,data)))

    print("Count of Even elements :-",f_data)


if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_15>python Question_10.py
#List of Numbers:-  [1, 3, 5, 6, 9, 10, 15, 30]
#List of even numbers:-  [6, 10, 30]
#Count of Even elements :- 3





    