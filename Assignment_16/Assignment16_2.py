# Write a program which contains one function chknum() which accept paramter as number and if number is even display Even Number else Odd Number

def ChkNum(no1):

    if no1 % 2 ==0:
        return "Even Number"

    else:
        return "Odd Number"

def main():

    x=int(input("Enter the Number :-"))
    ret=ChkNum(x)

    print(ret)

if __name__ == "__main__":
    main()    

# Output
# C:\Users\Shree\Desktop\Assignment_16>python Assignment16_2.py
#Enter the Number :-11
#Odd Number

#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_2.py
#Enter the Number :-6
#Even Number

    