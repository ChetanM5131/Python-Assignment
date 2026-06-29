# Write function to accept 2 numbers and find out greater number
def chkgreater(val1,val2):
    if (val1 > val2):
        return val1
    else:
        return val2

def main():
    print("Enter No1 :-")
    no1=int(input())

    print("Enter No2 :-")
    no2=int(input())

    ret=chkgreater(no1,no2)

    print("Greater Number is:-",ret)
if __name__ == "__main__":
    main()


#Output:- 
#C:\Users\Shree\Desktop\Assignment_9>python Question_2.py
#Enter No1 :-
#12
#Enter No2 :-
#23
#Greater Number is:- 23
