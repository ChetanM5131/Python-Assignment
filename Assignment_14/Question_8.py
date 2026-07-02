# Write lambda function which accept two numbers and return its addition
add=lambda no1,no2:no1+no2

def main():
    no1=int(input("Enter No1:- "))
    no2=int(input("Enter No2:- "))
    ret=add(no1,no2) 
    print("Addition :",ret)

if __name__ == "__main__":
    main()    

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_8.py
#Enter No1:- 10
#Enter No2:- 11
#Addition : 21

