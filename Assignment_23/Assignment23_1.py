# Write a Python program using multiprocessing.Pool to calculate the
# sum of all even numbers from 1 to N for every number from the given list.

import os
import time
import multiprocessing

def sum_even(no1):
    if no1<=1:
        return False
    sum=0
    for i in range(1,no1+1):

        if i%2==0:
            sum+=i
            
    return os.getpid(),no1,sum
    
def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        l1.append(v2)
    print("Elements in List :-",l1) 

    start_time=time.perf_counter()
    
    obj1=multiprocessing.Pool()
    result=obj1.map(sum_even,l1)

    obj1.close()
    obj1.join()

    print("\nResult is:-")    

    for pid,v2,sum in result:
        print(f"Process Id:- {pid}")
        print(f"Input:- {v2}")
        print(f"Even Sum:- {sum}")
        print()

    #print("Result is:-")   
    #print(result) 

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_23>python Assignment23_1.py
#Enter how many elemets need to insert into List :-4
#Enter elements of List :-1000000
#Enter elements of List :-2000000
#Enter elements of List :-3000000
#Enter elements of List :-4000000
#Elements in List :- [1000000, 2000000, 3000000, 4000000]
#Result is:-
#Process Id:- 15060
#Input:- 1000000
#Even Sum:- 250000500000
#
#Process Id:- 12648
#Input:- 2000000
#Even Sum:- 1000001000000
#
#Process Id:- 6448
#Input:- 3000000
#Even Sum:- 2250001500000
#
#Process Id:- 14340
#Input:- 4000000
#Even Sum:- 4000002000000
#Time req:- 1.1135 sec    