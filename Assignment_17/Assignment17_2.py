# Write a program which accept one number and display * pattern e.g 
# for input=3 display below patteren
#   ***
#   ***
#   ***

def main():
    no1= int(input("Enter the Number:-"))
    for i in range(no1):
        print("*" *no1)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_2.py
#Enter the Number:-5
# *****
# *****
# *****
# *****
# *****

    