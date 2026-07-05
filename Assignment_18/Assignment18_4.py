# Write the program which accept N numbers from user and store it into list.
# Accept another number from user and find its frequency
def main():
    lst=[]
    no1=int(input("Enter how many numbers  into list:- "))

    for i in range(1,no1+1):
        x=int(input("enter number to insert into list:-"))
        lst.append(x)
    
    val=int(input("Enter the element to get its frequency in list:-"))
    cnt=lst.count(val)

    print(f"Frequency of {val} in given list is:-",cnt)

    

if __name__ =="__main__":
    main() 

# Output
# 
#C:\Users\Shree\Desktop\Assignment_18>python Assignment18_4.py
#Enter how many numbers  into list:- 5
#enter number to insert into list:-1
#enter number to insert into list:-1
#enter number to insert into list:-2
#enter number to insert into list:-3
#enter number to insert into list:-1
#Enter the element to get its frequency in list:-1
#Frequency of 1 in given list is:- 3

           