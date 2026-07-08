#Design a Python application that creates two threads named EvenList and OddList.
#Both threads should accept a list of integers as input.
#The EvenList thread should:
#Extract all even elements from the list.
#Calculate and display their sum.
#The OddList thread should:
#Extract all odd elements from the list.
#Calculate and display their sum.
#Threads should run concurrently.
import threading
import time
def EvenList(x):
    L1=[]
    sum_even=0
    for i in x:
        if i %2 ==0:
            sum_even+=i
            L1.append(i)
    print("Even element:-",L1)  

    even_sum=sum(L1) 
    print("Sum of Even elements in List",even_sum) 
    print(f"Inside Even_sum Thrade ID:- :",threading.get_ident())
    print(f"Inside Even_sum Thread Name: {threading.current_thread().name}")  

def OddList(x):
    L2=[]
    sum_odd=0
    for i in x:
        if i %2 !=0:
            sum_odd+=i
            L2.append(i)
    print("Even element:-",L2)  

    odd_sum=sum(L2) 
    print("Sum of Odd elements in List",odd_sum) 
    print(f"Inside Odd_sum Thrade ID:- :",threading.get_ident())
    print(f"Inside Odd_sum Thread Name: {threading.current_thread().name}")            



def main():
    
    print(f"Inside Main Thrade ID:- :",threading.get_ident())
    print(f"Inside Main Thread Name: {threading.current_thread().name}")
    
    dt=int(input("Enter how many elements needs to enter in list:-"))
    
    data=[]
    
    for i in range(1,dt+1):
        ele=int(input("Enter the element:-"))
        data.append(ele)

        start_time=time.perf_counter()

    t1=threading.Thread(target=EvenList,args=(data,),name="EvenFactor")

    t2=threading.Thread(target=OddList,args=(data,),name="OddFactor")

    t1.start()

    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main Thrade")

    end_time=time.perf_counter()

    print(f"Time Required :- {end_time-start_time:.4f}")        


if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_20>python Assignment20_3.py
#Inside Main Thrade ID:- : 15716
#Inside Main Thread Name: MainThread
#Enter how many elements needs to enter in list:-5
#Enter the element:-11
#Enter the element:-22
#Enter the element:-24
#Enter the element:-23
#Enter the element:-17
#Even element:- [22, 24]
#Sum of Even elements in List 46
#Inside Even_sum Thrade ID:- : 6604
#Inside Even_sum Thread Name: EvenFactor
#Even element:- [11, 23, 17]
#Sum of Odd elements in List 51
#Inside Odd_sum Thrade ID:- : 1708
#Inside Odd_sum Thread Name: OddFactor
#Exit from Main Thrade
#Time Required :- 0.0021    