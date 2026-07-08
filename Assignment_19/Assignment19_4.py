#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.

from functools import reduce

filt_even=lambda x: x % 2==0

map_data=lambda x: x * x

reduce_add=lambda x,x1: x+x1

def main():
    
    dt=int(input("Enter how many elements needs to enter in list:-"))
    
    data=[]
    
    for i in range(1,dt+1):
        ele=int(input("Enter the element:-"))
        data.append(ele)

    f_data=list(filter(filt_even,data))    

    print("Filter Data is:-",f_data)

    m_data=list(map(map_data,f_data))

    print("Map Data is:-",m_data)

    r_data=reduce(reduce_add,m_data)

    print("Reduce Data is:-",r_data)

if __name__ == "__main__":
    main()


# Output
# C:\Users\Shree\Desktop\Assignment_19>python Assignment19_4.py
# Enter how many elements needs to enter in list:-4
# Enter the element:-1
# Enter the element:-2
# Enter the element:-3
# Enter the element:-4
# Filter Data is:- [2, 4]
# Map Data is:- [4, 16]
# Reduce Data is:- 20    