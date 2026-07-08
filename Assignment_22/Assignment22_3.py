# For every number in the given list, count how many prime numbers
# exist between 1 and N using multiprocessing Pool.
import os
import sys  
import time
import multiprocessing

def chk_prime(no1):
    if no1<=1:
        return False
    
    for i in range(2,no1):

        if no1%i==0:
            return False
    return True
    
def count_prime(no1):
    print("Process is running with PID:-",os.getpid())
    cnt=0
    for i in range(1,no1+1):
        if chk_prime(i):
            cnt+=1
    return cnt

def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        l1.append(v2)
    print("Elements in List :-",l1) 

    start_time=time.perf_counter()
    
    obj1=multiprocessing.Pool()
    result=obj1.map(count_prime,l1)

    obj1.close()

    obj1.join()

    print("Result is:-")   
    print(result) 

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_22>python Assignment22_3.py
# Enter how many elemets need to insert into List :-4
# Enter elements of List :-10000
# Enter elements of List :-20000
# Enter elements of List :-30000
# Enter elements of List :-40000
# Elements in List :- [10000, 20000, 30000, 40000]
# Process is running with PID:- 9548
# Process is running with PID:- 17504
# Process is running with PID:- 4804
# Process is running with PID:- 17616
# Result is:-
# [1229, 2262, 3245, 4203]
# Time req:- 10.0064 sec    