#: Design a Python application that creates two threads named EvenFactor and
# OddFactor.
# Both threads should accept one integer number as a parameter.
# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors.
# The OddFactor thread should:
# Identify all odd factors of the given number.
# Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
#Exit from main”
import threading
import time
def Even_fact_sum(no1):
    lst=[]
    even_fact_list=[]
    even_fact=0
    
    for i in range(1,no1+1):
        if no1 % i ==0:
            lst.append(i)

    for j in lst:
        if j % 2==0:
            even_fact+=j
            even_fact_list.append(j)
    print("Even Facotrs:-",even_fact_list)        

    print(f"Inside Even_fact_sum Thrade ID:- :",threading.get_ident())
    print(f"Inside Even_fact_sum Thread Name: {threading.current_thread().name}")

    print(f"Sum of Even facotrs of {no1} is :-",even_fact)        

def Odd_fact_sum(no1):
    lst=[]
    odd_fact_list=[]
    Odd_fact=0

    for i in range(1,no1+1):
        if no1 % i ==0:
            lst.append(i)

    for j in lst:
        if j % 2!=0:
            Odd_fact+=j
            odd_fact_list.append(j)
    
    print("Odd Facotrs:-",odd_fact_list) 

    print(f"Inside Odd_fact_sum Thrade ID:- :",threading.get_ident())
    print(f"Inside Odd_fact_sum Thread Name: {threading.current_thread().name}")

    print(f"Sum of Odd facotrs of {no1} is :-",Odd_fact)

def main():
    
    no1=int(input("Enter the Number :-"))

    print(f"Inside Main Thrade ID:- :",threading.get_ident())
    print(f"Inside Main Thread Name: {threading.current_thread().name}")

    start_time=time.perf_counter()

    t1=threading.Thread(target=Even_fact_sum,args=(no1,),name="EvenFactor")

    t2=threading.Thread(target=Odd_fact_sum,args=(no1,),name="OddFactor")

    t1.start()

    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main Thrade")

    end_time=time.perf_counter()

    print(f"Time Required :- {end_time-start_time:.4f}")



if __name__ == "__main__":
    main()    

# Output
# C:\Users\Shree\Desktop\Assignment_20>python Assignment20_2.py
# Enter the Number :-40
# Inside Main Thrade ID:- : 2396
# Inside Main Thread Name: MainThread
# Even Facotrs:- [2, 4, 8, 10, 20, 40]
# Inside Even_fact_sum Thrade ID:- : 15244
# Inside Even_fact_sum Thread Name: EvenFactor
# Sum of Even facotrs of 40 is :- 84
# Odd Facotrs:- [1, 5]
# Inside Odd_fact_sum Thrade ID:- : 17300
# Inside Odd_fact_sum Thread Name: OddFactor
# Sum of Odd facotrs of 40 is :- 6
# Exit from Main Thrade
# Time Required :- 0.0019  