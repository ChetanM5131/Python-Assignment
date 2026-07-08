# Write a program that counts how many even numbers exist
# between 1 and N using Pool.map()

import os
import time
import multiprocessing

def even_count(no1):
    if no1<=1:
        return False
    count=0
    for i in range(1,no1+1):

        if i%2==0:
            count+=1
            
    return os.getpid(),no1,count
    
def main():
    l1=[]
    v1=int(input("Enter how many elemets need to insert into List :-"))
    for i in range(1,v1+1):
        v2=int(input("Enter elements of List :-"))
        l1.append(v2)
    print("Elements in List :-",l1) 

    start_time=time.perf_counter()
    
    obj1=multiprocessing.Pool()
    result=obj1.map(even_count,l1)

    obj1.close()
    obj1.join()

    print("\nResult is:-")    

    for pid,v2,count in result:
        print(f"Process Id:- {pid}")
        print(f"Input:- {v2}")
        print(f"Count Even:- {count}")
        print()

    end_time=time.perf_counter()
    print(f"Time req:- {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_23>python Assignment23_3.py
# Enter how many elemets need to insert into List :-4
# Enter elements of List :-1000000
# Enter elements of List :-2000000
# Enter elements of List :-3000000
# Enter elements of List :-4000000
# Elements in List :- [1000000, 2000000, 3000000, 4000000]
# 
# Result is:-
# Process Id:- 2100
# Input:- 1000000
# Count Even:- 500000
# 
# Process Id:- 5856
# Input:- 2000000
# Count Even:- 1000000
# 
# Process Id:- 7284
# Input:- 3000000
# Count Even:- 1500000
# 
# Process Id:- 8072
# Input:- 4000000
# Count Even:- 2000000
# 
# Time req:- 1.0266 sec