# Write a program that calculates factorials of multiple numbers
# simultaneously using multiprocessing.Pool.

import os
import time
import multiprocessing

def fact(no1):
    if no1==0:
        return False
    fact_cnt=1
    for i in range(1,no1+1):

        fact_cnt=fact_cnt*i
    return os.getpid(),no1,fact_cnt
    
def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        if v2==0:
            print("Enter non zero element")
        else:
            l1.append(v2)
    print("Elements in List :-",l1) 

    start_time=time.perf_counter()
    
    obj1=multiprocessing.Pool()
    result=obj1.map(fact,l1)

    obj1.close()
    obj1.join()

    print("\nResult is:-")    

    for pid,v2,fact_cnt in result:
        print(f"Process Id:- {pid}")
        print(f"Input:- {v2}")
        print(f"Factorial is:- {fact_cnt}")
        print()

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_23>python Assignment23_5.py
# Enter how many elemets need to insert into List :-2
# Enter elements of List :-10
# Enter elements of List :-20
# Elements in List :- [10, 20]
# 
# Result is:-
# Process Id:- 19052
# Input:- 10
# Factorial is:- 3628800
# 
# Process Id:- 19052
# Input:- 20
# Factorial is:- 2432902008176640000
# 
# Time req:- 0.3993 sec    