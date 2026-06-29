# Write a program to accept radius and print itarea of circle

def area_circle(rad1):
    pi=3.14
    return pi*rad1*rad1

def main():

    rad1=int(input("Enter the raidus of circle in cm :-"))
    
    ret=area_circle(rad1)

    print("Area of Circle  is:- ",ret )

if __name__ == "__main__":
    main()    

#Output:-
#C:\Users\Shree\Desktop\Assignment_13>python Question_2.py
#Enter the raidus of circle in cm :-4
#Area of Circle  is:-  50.24

