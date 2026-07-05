# Write a program which contain one function which return True if number is divisible by 5 else return False

def Chk_div(x):
    if x % 5 ==0:
        return "True"
    else:
        return "False"
def main():
    no1=int(input("Enter Number:- "))

    print(Chk_div(no1))

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_16>python Assignment16_7.py
#Enter Number:- 15
#True

#C:\Users\Shree\Desktop\Assignment_16>python Assignment16_7.py
#Enter Number:- 9
#False

    