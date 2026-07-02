# Write a lambda function which return True if number is Odd otherwise False

even_odd = lambda no1: True if no1%2 == 1 else False

def main():
    
    no1=int(input("Enter No:- "))
    ret =even_odd(no1)
    print(ret)

if __name__ == "__main__":
    main()

# Output

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_6.py
#Enter No:- 2
#False

#C:\Users\Shree\Desktop\Assignment_14>python Question_6.py
#Enter No:- 3
#True     