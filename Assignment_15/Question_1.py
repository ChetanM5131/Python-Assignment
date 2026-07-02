# Write a lambda function using map() which can accept the list of numbers and return list of squre of each number

squ= lambda no: no * no

def main():
    data=[13,12,8,10,11,20]
    print("Input data is :",data)
    m_data=list(map(squ,data))
    print("Data after Map :",m_data)
if __name__ == "__main__":
    main()    
