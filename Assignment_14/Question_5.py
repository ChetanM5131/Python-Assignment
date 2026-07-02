# Write a lambda function which return True if number is even otherwise False

even_odd = lambda no1: True if no1%2 == 0 else False

def main():
    
    no1=int(input("Enter No:- "))
    ret =even_odd(no1)
    print(ret)
    
if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_5.py
#Enter No:- 2
#True

#C:\Users\Shree\Desktop\Assignment_14>python Question_5.py
#Enter No:- 3
#False 