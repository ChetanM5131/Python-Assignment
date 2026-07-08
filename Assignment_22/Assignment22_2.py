# Write a program that calculates factorials of multiple numbers
# simultaneously using Pool.map().
import time
import os
import multiprocessing
def fact_fun(no1):
    print("Process is running with PID:-",os.getpid())
    fact=1
    for i in range(1,no1+1):
        fact=fact*i
    return fact    
def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        l1.append(v2)
    print("Elements in List :-",l1) 

    start_time=time.perf_counter()
    obj1=multiprocessing.Pool()
    result=obj1.map(fact_fun,l1)

    obj1.close()

    obj1.join()

    print("Result is:-")   
    print(result) 

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_22>python Assignment22_2.py
# Enter how many elemets need to insert into List :-4
# Enter elements of List :-10
# Enter elements of List :-11
# Enter elements of List :-12
# Enter elements of List :-13
# Elements in List :- [10, 11, 12, 13]
# Process is running with PID:- 7180
# Process is running with PID:- 15296
# Process is running with PID:- 7180
# Process is running with PID:- 7180
# Result is:-
# [3628800, 39916800, 479001600, 6227020800]
# Time req:- 0.3921 sec    