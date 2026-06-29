#Write a program to accept the number and generate its table
def main ():
    arr=list()
    
    tbl=int(input("Enter the number :-"))

    print("Table of ",str(tbl) + ":-")

    for i in range(1,11):
        no = tbl*i
        arr.append(no)

    print(arr)   

if __name__ == "__main__":
    main() 

#Output
#     