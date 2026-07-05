# Write a program to accept number from user and print number of "*" on screen

def main():
    no1=int(input("Enter the Number:-"))
    for i in range(1,no1+1):
        print("*",end=" ")

if __name__ == "__main__":
    main() 

# Output
# C:\Users\Shree\Desktop\Assignment_16>python Assignment16_8.py                                                           
#  Enter the Number:-5                                                                                                     
#  * * * * *                                                                                                              
#  C:\Users\Shree\Desktop\Assignment_16>python Assignment16_8.py                                                          
#  Enter the Number:-3                                                                                                     
#  * * *                                                                                                                   
#  C:\Users\Shree\Desktop\Assignment_16>       