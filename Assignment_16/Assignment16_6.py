# Write a program which accept number from user and check whether number is Positive,negetive or Zero
def Chk_Num(x):
    if x > 0:
        return"Positive Number"
    elif x < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():
    no1=int(input("Enter Number:-"))
    print(Chk_Num(no1))

if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_6.py
#Enter Number:--4
#Negative Number

#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_6.py
#Enter Number:-0
#Zero

#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_6.py
#Enter Number:-11
#Positive Number

    