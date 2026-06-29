#Write a progrm to accept number from user and check whether it is prime number or not
def prime_test(no1):

    if no1<=1:
        return False

    for  val in range(2,no1):
        if (no1 % val ==0):
           return False
        
    return True


def main ():
    
    no1=int(input("Enter the number :-"))
    ret=prime_test(no1)
    if ret:
        print("Number is prime")
    else:
        print("Number is not prime")           

if __name__ == "__main__":
    main() 

#Output
#C:\Users\Shree\Desktop\Assignment_11>python Question_1.py
#Enter the number :-15
#Number is not prime
#C:\Users\Shree\Desktop\Assignment_11>python Question_1.py
#Enter the number :-3
#Number is prime
#C:\Users\Shree\Desktop\Assignment_11>python Question_1.py
#Enter the number :-29
#Number is prime
