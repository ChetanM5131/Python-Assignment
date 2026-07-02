# Write a lambda function which accept 2 numbers and return minimum of number
min_num=lambda no1,no2:min(no1,no2)
def main():
    no1=int(input("Enter No1 :-"))
    no2=int(input("Enter No2 :-"))

    ret=min_num(no1,no2)
    print("Minimum Number is :-",ret)

if __name__ == "__main__":
    main()


# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_4.py
#Enter No1 :-32
#Enter No2 :-23
#Minimum Number is :- 23

    