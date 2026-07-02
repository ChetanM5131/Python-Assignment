# Write lambda function which accept number and return cube of its number

cube=lambda no1: no1*no1*no1

def main():
    no1=int(input("Enter No:-"))
    ret=cube(no1)

    print("Cube of given Number :-",ret)

if __name__ == "__main__":
    main()

# Output
#C:\Users\Shree\Desktop\Assignment_14>python Question_2.py
#Enter No:-5
#Cube of given Number :- 125

    