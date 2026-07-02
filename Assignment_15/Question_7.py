# Write a lambda function using filter() which accept list of string elements and return list of string having length > 5
str_data=lambda x:len(x)>5
def main():

    data=['abc','abcdef','aaabbbccc','ababc','abccba','abcpqr']
    print("List of string elements:- ",data)

    f_data=list(filter(str_data,data))

    print("Elements having length > 5 :-",f_data)


if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_7.py
#List of string elements:-  ['abc', 'abcdef', 'aaabbbccc', 'ababc', 'abccba', 'abcpqr']
#Elements having length > 5 :- ['abcdef', 'aaabbbccc', 'abccba', 'abcpqr']

    