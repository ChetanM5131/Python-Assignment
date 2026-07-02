# Write lambda function which accept two numbers and return its multiplication
find_max=lambda val1,val2,val3: max(val1,val2,val3)

def main():
    no1=int(input("Enter No1:- "))
    no2=int(input("Enter No2:- "))
    no3=int(input("Enter No3:- "))
    ret=find_max(no1,no2,no3) 
    print("Max Number is :",ret)

if __name__ == "__main__":
    main()    

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_10.py
#Enter No1:- 10
#Enter No2:- 11
#Enter No2:- 7
#Max Number is : 11

