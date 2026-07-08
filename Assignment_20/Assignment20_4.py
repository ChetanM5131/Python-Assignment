# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:Thread ID Thread Name
import threading
import time

def sm_data(val1):
    
    print(f"Inside sm_data Thrade ID:- :",threading.get_ident())
    
    l1=[]
    cnt=0
    for alpha in val1:
        if alpha.islower():
            l1.append(alpha)
    print(l1)
    cnt=len(l1)
    print(f"Inside sm_data Thread Name: {threading.current_thread().name}") 
    print(f"Count of lower case characters is:-{cnt} and lowecase char are:-",l1)




def upper_data(val1):
    
    print(f"Inside upper_data Thrade ID:- :",threading.get_ident())
    
    l1=[]
    cnt=0
    for alpha in val1:
        if alpha.isupper():
            l1.append(alpha)
    print(l1)
    cnt=len(l1)
    print(f"Inside upper_data Thread Name: {threading.current_thread().name}") 
    print(f"Count of Upper case characters is:-{cnt} and Uppercase char are:-",l1)


def digit_data(val1):
    print(f"Inside digit_data Thrade ID:- :",threading.get_ident())
    
    l1=[]
    cnt=0
    for alpha in val1:
        if alpha.isdigit():
            l1.append(alpha)
    print(l1)
    cnt=len(l1)
    print(f"Inside digit_data Thread Name: {threading.current_thread().name}") 
    print(f"Count of Digits:-{cnt} and Digits are:-",l1)
    

def main():
    
    str1=input("Enter the String Having Uppercase, LowerCase and Digits:- ")

    start_time=time.perf_counter()

    small_t=threading.Thread(target=sm_data,args=(str1,),name="Small_T")

    upper_t=threading.Thread(target=upper_data,args=(str1,),name="Upper_T")

    digit_t=threading.Thread(target=digit_data,args=(str1,),name="Digit_T")

    small_t.start()

    small_t.join()

    upper_t.start()

    upper_t.join()

    digit_t.start()

    digit_t.join()

    print("Exit from Main Thrade")

    end_time=time.perf_counter()

    print(f"Time Required :- {end_time-start_time:.4f}")         


if __name__ == "__main__":
    main()

# C:\Users\Shree\Desktop\Assignment_20>Assignment20_4.py
# Enter the String Having Uppercase, LowerCase and Digits:- HeLL0123PyTHon
# Inside sm_data Thrade ID:- : 16012
# ['e', 'y', 'o', 'n']
# Inside sm_data Thread Name: Small_T
# Count of lower case characters is:-4 and lowecase char are:- ['e', 'y', 'o', 'n']
# Inside upper_data Thrade ID:- : 9764
# ['H', 'L', 'L', 'P', 'T', 'H']
# Inside upper_data Thread Name: Upper_T
# Count of Upper case characters is:-6 and Uppercase char are:- ['H', 'L', 'L', 'P', 'T', 'H']
# Inside digit_data Thrade ID:- : 12188
# ['0', '1', '2', '3']
# Inside digit_data Thread Name: Digit_T
# Count of Digits:-4 and Digits are:- ['0', '1', '2', '3']
# Exit from Main Thrade
# Time Required :- 0.0136 