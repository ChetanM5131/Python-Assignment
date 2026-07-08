#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
#return Maximum number from that numbers. (You can also use normal functions instead of
#lambda functions)

from functools import reduce

def find_prime(no1):

    if no1 < 1:
        return False
    
    for i in range(2,no1):

        if no1 % i ==0:
            return False
    
    return True

chk_prime=lambda x: find_prime(x) 

map_func=lambda x: x*2

reduce_data=lambda x ,x1: max(x,x1)

def main():
    
    dt=int(input("Enter how many elements needs to enter in list:-"))
    
    data=[]
    
    for i in range(1,dt+1):
        ele=int(input("Enter the element:-"))
        data.append(ele)

    f_data=list(filter(chk_prime,data))   

    print("Filter Data List:-",f_data)

    m_data=list(map(map_func,f_data))  

    print("Map data list:-",m_data)

    r_data=reduce(reduce_data,m_data)  

    print("Reduce Data:-",r_data)

if __name__ == "__main__":
    main()


# Output
# C:\Users\Shree\Desktop\Assignment_19>python Assignment19_5.py                                                            
# Enter how many elements needs to enter in list:-5                                                                        
# Enter the element:-2                                                                                                     
# Enter the element:-3                                                                                                     
# Enter the element:-4                                                                                                     
# Enter the element:-5                                                                                                     
# Enter the element:-9                                                                                                     
# Filter Data List:- [2, 3, 5]                                                                                             
# Map data list:- [4, 6, 10]                                                                                               
# Reduce Data:- 10     