# Accept the number from user and count the digits in number

def main():

    no1=int(input("Enter the Number:-"))
    ret=len(str(no1))
    print(f"no of digits in {no1} is:-",ret)

if __name__ =="__main__":
    main()    

# Output
#C:\Users\Shree\Desktop\Assignment_17>python Assignment17_9.py
#Enter the Number:- 23456
#no of digits in 23456 is:- 5
