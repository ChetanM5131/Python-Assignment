# Design a Python application that creates two threads named Prime and NonPrime.
# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.
import threading
import time
def chk_prime(no1):

    if no1 <= 1:
        return False
    for i in range(2,no1):

        if no1 % i ==0:
            return False
    return True

def is_prime(x):
    prime_no=list(filter(chk_prime,x))

    print("Prime Numbers:-",prime_no)

def is_not_prime(x):
    non_prime_no = list(filter(lambda num: not chk_prime(num), x))
    print("Non Prime Numbers:-",non_prime_no)    


def main():
    l1=[]
    e1=int(input("Enter how many elements need to insert into List :-"))

    for i in range(1,e1+1):
        v1=int(input("Enter List element:-"))
        l1.append(v1)

    print("List elements are:- ",l1)

    T1=threading.Thread(target=is_prime,args=(l1,),name="PrimeT")

    T2=threading.Thread(target=is_not_prime,args=(l1,),name="NonPrimeT")

    T1.start()
    
    T2.start()

    T1.join()

    T2.join()

    


if __name__ == "__main__":
    main()

# C:\Users\Shree\Desktop\Assignment_21>python Assignment21_1.py
# Enter how many elements need to insert into List :-5
# Enter List element:-2
# Enter List element:-4
# Enter List element:-5
# Enter List element:-7
# Enter List element:-9
# List elements are:-  [2, 4, 5, 7, 9]
# Prime Numbers:- [2, 5, 7]
# Prime Numbers:- [4, 9]    