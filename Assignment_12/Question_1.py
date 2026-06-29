#Write a program whether to check character entered by user is vowel or not
def chk_vowel(val):
    
    if val.lower() in "aeiou":
        return 1
    else:
        return 2

def main():

    dt=str(input("Enter a character to check itis vowel or not:-"))
    
    ret=chk_vowel(dt)

    if ret==1:
        print(dt," Is a vowel")
    else:
        print(dt," Is not a vowel")   
if __name__ == "__main__":
    main()


#Output:-
# C:\Users\Shree\Desktop\Assignment_12>python Question_1.py
#Enter a character to check itis vowel or not:-p
#p  Is not a vowel
#C:\Users\Shree\Desktop\Assignment_12>python Question_1.py
#Enter a character to check itis vowel or not:-A
#A  Is a vowel

    