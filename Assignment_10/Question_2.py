#Write the program to accept number and print the sum of first N natiral number
def sum_natural(val1):
    sum=0
    
    for i in range(val1+1):
        sum = sum+i
    return sum

def main ():
    
    no1=int(input("Enter the number :-"))

    ret=sum_natural(no1)
    print("Sum of first",str(no1) + " Natural number is :-",ret)

if __name__ == "__main__":
    main() 

#Output:-
# C:\Users\Shree\Desktop\Assignment_10>python Question_2.py
#Enter the number :-6
#Sum of first 6 Natural number is :- 21

    