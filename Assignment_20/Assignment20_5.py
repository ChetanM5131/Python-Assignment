# Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure that:
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronizatio
import threading

import time

def disp_num():
    print(f"Inside disp_num Thrade ID:- :",threading.get_ident())
    for i in range(1,51):
        print(i , end= " ")
    print()    

def disp_num_rev():
    print(f"Inside disp_num_rev Thrade ID:- :",threading.get_ident())
    for i in range(50,0,-1):
        print(i , end= " ")
    print()    
            
def main():

    start_time=time.perf_counter()

    print(f"Inside Main Thrade ID:- :",threading.get_ident())

    t1_start_time=time.perf_counter()
    T1=threading.Thread(target=disp_num,name="Thread1")

    T1.start()

    T1.join()

    print("Thread 1 Completed")

    t1_end_time=time.perf_counter()

    t2_start_time=time.perf_counter()

    T2=threading.Thread(target=disp_num_rev,name="Thread2")

    T2.start()

    T2.join()

    print("Thread 2 Completed")

    t2_end_time=time.perf_counter()

    end_time=time.perf_counter()

    print(f"Time Required for T1:- {t1_end_time-t1_start_time:.4f}") 

    print(f"Time Required for T2:- {t2_end_time-t2_start_time:.4f}") 

    print(f"Time Required for Main:- {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_20>python Assignment20_5.py
# Inside Main Thrade ID:- : 6384
# Inside disp_num Thrade ID:- : 16988
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
# Thread 1 Completed
# Inside disp_num_rev Thrade ID:- : 15200
# 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
# Thread 2 Completed
# Time Required for T1:- 0.0010
# Time Required for T2:- 0.0004
# Time Required for Main:- 0.0015    