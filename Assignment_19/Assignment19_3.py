#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that numbers.
from functools import reduce

flt=lambda x: x>=70 and x<=90

map_data=lambda x: x+10

rd_data=lambda x,x1: x*x1

def main():
    
    dt=int(input("Enter how many elements needs to enter in list:-"))
    
    data=[]
    
    for i in range(1,dt+1):
        ele=int(input("Enter the element:-"))
        data.append(ele)

    f_data=list(filter(flt,data))

    print("Filter data list:-",f_data)

    m_data=list(map(map_data,f_data))

    print("Map data list:-",m_data)

    r_data= reduce(rd_data,m_data)

    print("Reduce data :-",r_data)

if __name__ == "__main__":
    main()


# Output
#C:\Users\Shree\Desktop\Assignment_19>python Assignment19_3.py
#Enter how many elements needs to enter in list:-12
#Enter the element:-4
#Enter the element:-34
#Enter the element:-36
#Enter the element:-76
#Enter the element:-68
#Enter the element:-24
#Enter the element:-89
#Enter the element:-23
#Enter the element:-86
#Enter the element:-90
#Enter the element:-45
#Enter the element:-70
#Filter data list:- [76, 89, 86, 90, 70]
#Map data list:- [86, 99, 96, 100, 80]
#Reduce data :- 6538752000


