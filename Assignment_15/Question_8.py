# Write a lambda function using filter() which accept list of numbers and return list of numbers divisible by 3 and 5
mod_data=lambda x: x%3==0 and x%5==0
def main():

    data=[1,3,5,6,9,10,15,30]
    print("List of Numbers:- ",data)

    f_data=list(filter(mod_data,data))

    print("List of numbers divisible by 3 and 5 :-",f_data)


if __name__ == "__main__":
    main()

# Output
# C:\Users\Shree\Desktop\Assignment_15>python Question_7.py
#List of string elements:-  ['abc', 'abcdef', 'aaabbbccc', 'ababc', 'abccba', 'abcpqr']
#Elements having length > 5 :- ['abcdef', 'aaabbbccc', 'abccba', 'abcpqr']

    