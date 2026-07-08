# Design a Python application that creates two threads.
# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.


import threading
import time
import math
def sum_element(x):
    tot=sum(x)
    print("Sum of element:-",tot)

def prod_element(x):
    prod_ele = math.prod(x)
    print("Product of elements:-",prod_ele)    


def main():
    l1=[]
    e1=int(input("Enter how many elements need to insert into List :-"))

    for i in range(1,e1+1):
        v1=int(input("Enter List element:-"))
        l1.append(v1)

    print("List elements are:- ",l1)

    T1=threading.Thread(target=sum_element,args=(l1,),name="Thread1")

    T2=threading.Thread(target=prod_element,args=(l1,),name="Thread2")

    T1.start()
    
    T2.start()

    T1.join()

    T2.join()

    


if __name__ == "__main__":
    main()

# Output
#Enter how many elements need to insert into List :-5
#Enter List element:-2
#Enter List element:-3
#Enter List element:-4
#Enter List element:-5
#Enter List element:-6
#List elements are:-  [2, 3, 4, 5, 6]
#Sum of element:- 20
#Product of elements:- 720


