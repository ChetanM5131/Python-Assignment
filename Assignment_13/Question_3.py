#Accept the number from User and check whether it is perfect number or not
def perfect_no(no1):
    sum=0
    for i in range(1,no1):
        if(no1%i==0):
            sum=sum+i
    return sum        

def main():
    no1=int(input("Enter the number :-"))

    if no1==perfect_no(no1):
        print(no1," Is perfect Number")
    else:
        print(no1," Is not perfect Number")


if __name__ == "__main__":
    main()

#Output
# C:\Users\Shree\Desktop\Assignment_13>python Question_3.py
#Enter the number :-4
#4  Is not perfect Number

#C:\Users\Shree\Desktop\Assignment_13>python Question_3.py
#Enter the number :-6
#6  Is perfect Number

