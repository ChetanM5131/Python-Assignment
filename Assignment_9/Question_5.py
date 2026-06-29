# Write a program to accept the number and check whether it is divisible by 3 and 5

def div(val1):
    if ((val1%3 == 0) and (val1%5 == 0)):
        return True
    else:
        return False

def main():
    
    no1=int(input("Enter Number:- "))
    ret=div(no1)
    
    if ret==True:
        print("Divisible by 3 and 5")
    else:        
        print("Not divisible by 3 and 5")

if __name__ == "__main__":
    main()


#Output:-
#C:\Users\Shree\Desktop\Assignment_9>python Question_5.py
#Enter Number:- 15
#Divisible by 3 and 5

#C:\Users\Shree\Desktop\Assignment_9>python Question_5.py
#Enter Number:- 8
#Not divisible by 3 and 5

