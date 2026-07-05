# Write a program which accept number from user and returns addition of its factors

def fact(x):
        
        sum=0
        for i in range(1,x):
             
             if x % i ==0:
                  sum +=i
        return sum          

def main():
    
    no1=int(input("Enter the Number:- "))

    print(f"Sum of Factors of {no1} is:-",fact(no1))

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_4.py
#Enter the Number:- 12
#Sum of Factors of 12 is:- 16

    