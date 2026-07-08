# Design a Python application where multiple threads update a shared variable.
# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.


import threading

tot_cnt = 0
t_lock = threading.Lock()

def data_counter():
    global tot_cnt
    for val in range(50000):
        with t_lock:
            tot_cnt += 1


t1 = threading.Thread(target=data_counter)
t2 = threading.Thread(target=data_counter)
t3 = threading.Thread(target=data_counter)

t1.start()
t2.start()
t3.start()

t1.join()
print(f"count t1: {tot_cnt}")  
t2.join()
print(f"count t2: {tot_cnt}")  
t3.join()
print(f"count t3: {tot_cnt}")  

print(f"Total count is: {tot_cnt}")  


# Output
#C:\Users\Shree\Desktop\Assignment_21>python Assignment21_3.py
#count t1: 128329
#count t2: 150000
#count t3: 150000
#Total count is: 150000

