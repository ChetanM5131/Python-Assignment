# Write the program to accept the number and print the number in reverse
def rev_num(no1):
    str1 = ""
    for i in str(no1):
        str1 = i + str1  # Prepend character
    return str1

def main():
    no1=int(input("Enter the number :-"))
    ret=rev_num(no1)
    print("Reverse Number is :-",ret)


if __name__ == "__main__":
    main()

#Output
#C:\Users\Shree\Desktop\Assignment_11>python Question_4.py
#Enter the number :-123
#Reverse Number is :- 321

#C:\Users\Shree\Desktop\Assignment_11>python Question_4.py
#Enter the number :-234567
#Reverse Number is :- 765432




