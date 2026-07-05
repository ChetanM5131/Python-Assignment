# Accept the number from user and count the digits in number
def digit_sum(x):
    sum1=0
       
    for i in range(1,int(len(str(x)))+1):
        sum1=sum1+i
    
    return int(sum1)


def main():

    no1=int(input("Enter the Number:-"))
    ret=digit_sum(no1)
    print(f"Sum of didits of {no1} is:-",ret)

if __name__ =="__main__":
    main()    

# Output
#C:\Users\Shree\Desktop\Assignment_17>python Assignment17_10.py
#Enter the Number:-123
#Sum of didits of 123 is:- 6


