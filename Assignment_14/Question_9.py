# Write lambda function which accept two numbers and return its multiplication
mult=lambda no1,no2:no1*no2

def main():
    no1=int(input("Enter No1:- "))
    no2=int(input("Enter No2:- "))
    ret=mult(no1,no2) 
    print("Multiplication is :",ret)

if __name__ == "__main__":
    main()    

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_9.py
#Enter No1:- 10
#Enter No2:- 11
#Multiplication is : 110

