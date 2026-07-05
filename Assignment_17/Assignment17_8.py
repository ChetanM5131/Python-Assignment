# Write a program to display patteren

def main():
    no1=int(input("Enter Number :-")) 
    
    for i in range(1,no1+1):

        for j in range(1,i+1):
            print(j,end=" ")
            
           
        print()


if __name__ == "__main__":
    main()    

# Output
# C:\Users\Shree\Desktop\Assignment_17>python Assignment17_8.py
#Enter Number :-4
#1 
#1 2 
#1 2 3 
#1 2 3 4

