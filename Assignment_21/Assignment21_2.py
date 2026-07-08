# Design a Python application that creates two threads.
# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading
import time

def is_max(x):
    max_no=max(x)
    print("Max Numbers:-",max_no)

def is_min(x):
    min_no = min(x)
    print("Min Numbers:-",min_no)    


def main():
    l1=[]
    e1=int(input("Enter how many elements need to insert into List :-"))

    for i in range(1,e1+1):
        v1=int(input("Enter List element:-"))
        l1.append(v1)

    print("List elements are:- ",l1)

    T1=threading.Thread(target=is_max,args=(l1,),name="MaxT")

    T2=threading.Thread(target=is_min,args=(l1,),name="MinT")

    T1.start()
    
    T2.start()

    T1.join()

    T2.join()

    


if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_21>python Assignment21_2.py
# Enter how many elements need to insert into List :-5
# Enter List element:-23
# Enter List element:-12
# Enter List element:-11
# Enter List element:-7
# Enter List element:-89
# List elements are:-  [23, 12, 11, 7, 89]
# Max Numbers:- 89
# Min Numbers:- 7    
