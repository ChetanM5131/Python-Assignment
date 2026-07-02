# Write a lambda function which accept two numbers and return maximum number
max_val= lambda no1,no2: no1 if no1>no2 else no2
def main():
    no1=int(input("Enter 1st Number:-"))
    no2=int(input("Enter 2nd Number:-"))

    ret=max_val(no1,no2)
    print("Maximum Number is:-",ret)

if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_3.py
#Enter 1st Number:-23
#Enter 2nd Number:-34
#Maximum Number is:- 34

    