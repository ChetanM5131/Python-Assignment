#Write a program that calculates
#1^5+2^5+3^5+…..+N^5
#for multiple values of N simultaneously using Pool.
#Input [1000000,2000000,3000000,4000000]
#Measure total execution time.
import os
import time
import multiprocessing
def sum_power(no1):
    print("Process is running with PID:-",os.getpid())
    sum=0
    for i in range(1,no1+1):
        sum=sum+(i**5)
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

    result=obj1.map(sum_power,l1)

    obj1.close()

    obj1.join()

    print("Result is:-")   
    print(result) 

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec") 



if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_22>python Assignment22_4.py
# Enter how many elemets need to insert into List :-4
# Enter elements of List :-1000000
# Enter elements of List :-2000000
# Enter elements of List :-3000000
# Enter elements of List :-4000000
# Elements in List :- [1000000, 2000000, 3000000, 4000000]
# Process is running with PID:- 15972
# Process is running with PID:- 17004
# Process is running with PID:- 7284
# Process is running with PID:- 236
# Result is:-
# [166667166667083333333333250000000000, 10666682666673333333333333000000000000, 121500121500033749999999999250000000000, 682667178666773333333333332000000000000]
# Time req:- 1.9007 sec
