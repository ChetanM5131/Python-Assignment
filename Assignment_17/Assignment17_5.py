# Write a program which accept the number from user and check whether it is prime or not

def chk_prime(no1):
    if no1<=1:
        return False

    for  val in range(2,no1):
        if (no1 % val ==0):
           return False
        
    return True
def main():

    x=int(input("Enter Number:-"))

    if chk_prime(x):
        ret="It is Prime Number"
    else:
        ret="It is not a Prime Number"    

    print(f"{x} :-",ret)    


if __name__ == "__main__":
    main()    

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_5.py
#Enter Number:-4
#4 :- It is not a Prime Number

#C:\Users\Shree\Desktop\Assignment_17>python Assignment17_5.py
#Enter Number:-11
#11 :- It is Prime Number

    