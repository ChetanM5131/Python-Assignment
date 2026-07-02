# Write a lambda function which return True if number is divisible by 5 otherwise False

divisible_5 = lambda no1: True if no1%5 == 0 else False

def main():
    
    no1=int(input("Enter No:- "))
    ret =divisible_5(no1)
    print(ret)


if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_7.py
#Enter No:- 23
#False

#C:\Users\Shree\Desktop\Assignment_14>python Question_7.py
#Enter No:- 30
#True         