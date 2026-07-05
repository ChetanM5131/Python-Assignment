# Write a program which accept number from user and print its factorial
def fact(x):
    ft=1
    for i in range(1,x+1):
    
        ft= ft * i

    return ft


def main():
    no1=int(input("Enter the Number :-"))

    ret=fact(no1)
    print(f"Factorial of {no1} is :-",ret)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_3.py
#Enter the Number :-3
#Factorial of 3 is :- 6

    