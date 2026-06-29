# Write a program to accept number as input from user and print all previous numbers starting from 1
def num_print(no1):

    for i in range(1,no1+1):
        val=print(i,end="")
    return val
def main():
    no1=int(input("Enter the number :-"))
    ret=num_print(no1)
    

if __name__ == "__main__":
    main()