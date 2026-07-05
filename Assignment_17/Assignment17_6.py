# Write a program which accept given number and display below patteren
# input=3
# ***
# **
# *

def main():
    no1= int(input("Enter Number:- "))

    for i in range(1,no1+1):

        print("*" * int((no1+1)-i))

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_6.py
# Enter Number:- 3
# ***
# **
# *

    