#Write a program which contains one lambda function which accepts two parameters and return
#its multiplication.
mult=lambda x,x1: x * x1
def main():

    no1=int(input("Enter No1 :-"))
    no2=int(input("Enter No2 :-"))

    ret=mult(no1,no2)
    print(f"Multiplication of {no1} and {no2} is:-",ret)

if __name__ == "__main__":
    main()


# Output
# C:\Users\Shree\Desktop\Assignment_19>python Assignment19_2.py
# Enter No1 :-4
# Enter No2 :-5
# Multiplication of 4 and 5 is:- 20

    