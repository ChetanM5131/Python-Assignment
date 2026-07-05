# Write a program which contains one function Add() which accept 2 numbers from user and display their the Addition
def Add(x,x1):
    sum_1=0
    sum_1=x+x1
    return sum_1

def main():
    
    no1=int(input("Enter no1 :-"))
    no2=int(input("Enter no2 :-"))

    ret=Add(no1,no2)
    print(ret)

if __name__ == "__main__":
    main()


#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_3.py
#Enter no1 :-11
#Enter no2 :-5
#16

    

