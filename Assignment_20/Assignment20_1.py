#  Design a Python application that creates two separate threads named Even and Odd.
#• The Even thread should display the first 10 even numbers.
#• The Odd thread should display the first 10 odd numbers.
#• Both threads should execute independently using the threading module.
#• Ensure proper thread creation and execution.

import threading
import time

def Even():
    for i in range(2,21,2):
        print(i,end=" ")
                
    print(f"Inside Even :",threading.get_ident())
        

def Odd():
    
    for i in range(1,21,2):
        print(i,end=" ")
                
    print(f"Inside Odd :",threading.get_ident())

def main():

    print(f"Inside Main :",threading.get_ident())

    start_time=time.perf_counter()

    t1=threading.Thread(target=Even)
    t2=threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time=time.perf_counter()

    print(f"Time Required :- {end_time-start_time:.4f}")

    
if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_20>python Assignment20_1.py
# Inside Main : 1320
# 2 4 6 8 10 12 14 16 18 20 
# Inside Even : 6860
# 1 3 5 7 9 11 13 15 17 19 
# Inside Odd : 11344
# Time Required :- 0.0013

    