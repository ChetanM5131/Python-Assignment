# Write a program to check whether given number is palindrom or not

def chk_palindrom(no1):
    str1 = ""
    for i in str(no1):
        str1 = i + str1  
        
    return str1

def main():
    no1=int(input("Enter the number :-"))
    ret=chk_palindrom(no1)

    if no1==int(chk_palindrom(no1)):
        print("Number is palindrom")
    else:    
        print("Number is not palindrom")


if __name__ == "__main__":
    main()

#C:\Users\Shree\Desktop\Assignment_11>python Question_5.py
#Enter the number :-123
#Number is not palindrom

#C:\Users\Shree\Desktop\Assignment_11>python Question_5.py
#Enter the number :-1221
#Number is palindrom

