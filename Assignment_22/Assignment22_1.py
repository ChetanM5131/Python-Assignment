# Write a program that accepts a list of integers and uses Pool.map()
# to calculate the sum of squares from 1 to N for every element in the list.
import os
import time
import multiprocessing
def sum_squre(no1):
    print("Process is running with PID:-",os.getpid())
    sum=0
    for i in range(1,no1+1):
        sum=sum+(i*i)
    return sum  

def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        l1.append(v2)
    print("Elements in List :-",l1)   

    start_time=time.perf_counter()

    obj1=multiprocessing.Pool() 

    result=obj1.map(sum_squre,l1)

    obj1.close()

    obj1.join()

    print("Result is:-")   
    print(result) 

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec") 



if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_22>python Assignment22_1.py
# Enter how many elemets need to insert into List :-4
# Enter elements of List :-1000000
# Enter elements of List :-2000000
# Enter elements of List :-3000000
# Enter elements of List :-4000000
# Elements in List :- [1000000, 2000000, 3000000, 4000000]
# Process is running with PID:- 6224
# Process is running with PID:- 17448
# Process is running with PID:- 17676
# Process is running with PID:- 9296
# Result is:-
# [333333833333500000, 2666668666667000000, 9000004500000500000, 21333341333334000000]
# Time req:- 1.1485 sec    