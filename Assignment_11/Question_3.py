#Write the prograam to accept the number from user and sum the digits in that numbert 
def sum_dgt(no1):
    sum=0

    if no1==0:
        sum=0

    while no1 > 0:
        
        sum +=no1%10
        no1=(no1//10)
        
        
    
    return sum    

def main():

    no1=int(input("Enter the Number:- "))
    
    ret=sum_dgt(no1)
    print("Sum of Number of digits:-",ret)

if __name__ == "__main__":
    main()    

#Output:-
#C:\Users\Shree\Desktop\Assignment_11>python Question_3.py
#Enter the Number:- 23
#Sum of Number of digits:- 5

#C:\Users\Shree\Desktop\Assignment_11>python Question_3.py
#Enter the Number:- 123
#Sum of Number of digits:- 6



    