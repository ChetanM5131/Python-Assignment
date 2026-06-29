# Write program which accept marks and display grade

def main():
    marks=int(input("Enter Mark of Student :-"))
    grade=""

    if marks >= 75:
        grade='Distinction'
    elif marks >=60 and marks <=75:
        grade="First_Class"
    elif marks >=50 and marks<=60:
        grade="Secod Class"
    elif marks < 50 :
        grade="Fail"
    else:
        grade="Fail"       

    print("Student Grade is :-",grade)             


if __name__ == "__main__":
    main()

#Output
# C:\Users\Shree\Desktop\Assignment_13>python Question_5.py
#Enter Mark of Student :-75
#Student Grade is :- Distinction

#C:\Users\Shree\Desktop\Assignment_13>python Question_5.py
#Enter Mark of Student :-61
#Student Grade is :- First_Class

#C:\Users\Shree\Desktop\Assignment_13>python Question_5.py
#Enter Mark of Student :-50
#Student Grade is :- Secod Class

#C:\Users\Shree\Desktop\Assignment_13>python Question_5.py
#Enter Mark of Student :-44
#Student Grade is :- Fail

    