#Write the program which accept the number and print its factorial
def fact(val1):
    fac=1
    
    for i in range(1,val1+1):
        fac = fac*i
    return fac

def main ():
    
    no1=int(input("Enter the number :-"))

    ret=fact(no1)
    print("Factorial of number ",str(no1) + "  is :-",ret)

if __name__ == "__main__":
    main() 

#Output:-
#C:\Users\Shree\Desktop\Assignment_10>python Question_3.py
#Enter the number :-5
#Factorial of number  5  is :- 120

