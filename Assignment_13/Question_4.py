# Write program to accept the number from User and prints its binary equivalant

def main():
    
    no1=int(input("Enter the Number :-"))
    bn_no=bin(no1)
    
    print("Binary equivalant is:- ",bn_no[2:])

if __name__ == "__main__":
    main()

#Output
# C:\Users\Shree\Desktop\Assignment_13>python Question_4.py
#Enter the Number :-4
#Binary equivalant is:-  100
#C:\Users\Shree\Desktop\Assignment_13>python Question_4.py
#Enter the Number :-10
#Binary equivalant is:-  1010

  