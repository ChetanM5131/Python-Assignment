#Write a program which contains one lambda function which accepts one parameter and return
#power of two.
pow=lambda x: x * x
def main():
    no1=int(input("Enter Number :-"))

    ret=pow(no1)

    print(f" Number = {no1} and power of 2 is:-",ret)

if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_19>python Assignment19_1.py
# Enter Number :-4
# Number = 4 and power of 2 is:- 16

    