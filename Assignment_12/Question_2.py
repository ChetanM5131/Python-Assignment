# Write a program to accept a number and print its factor
def fact(no1):
    lst=list()
    for i in range(1,no1+1):
        if no1%i ==0:
            lst.append(i)
    return lst        

def main():

    no1=int(input("Enter the number:- "))
    ret=fact(no1)
    print(ret)



if __name__ == "__main__":
    main()    

#Output:-
#C:\Users\Shree\Desktop\Assignment_12>python Question_2.py
#Enter the number:- 6
#[1, 2, 3, 6]
#C:\Users\Shree\Desktop\Assignment_12>python Question_2.py
#Enter the number:- 12
#[1, 2, 3, 4, 6, 12]

