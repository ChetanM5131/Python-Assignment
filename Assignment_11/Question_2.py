#Write the prograam to accept the number from user and count the digits in that numbert 
def cnt_dgt(no1):
    cnt=0

    if no1==0:
        cnt=1

    while no1!=0:
        
        no1=(no1//10)
        
        cnt+=1
    
    return cnt    

def main():

    no1=int(input("Enter the Number:- "))
    
    ret=cnt_dgt(no1)
    print("Number of digits:-",ret)

if __name__ == "__main__":
    main()    

#Output:-
#C:\Users\Shree\Desktop\Assignment_11>python Question_2.py
#Enter the Number:- 23
#Number of digits:- 2

#C:\Users\Shree\Desktop\Assignment_11>python Question_2.py
#Enter the Number:- 34657
#Number of digits:- 5

    