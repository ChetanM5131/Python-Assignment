# Write a program to accept lenght and width of rectangle and print its area

def area_rect(length,width):
    return length*width

def main():

    len1=int(input("Enter the lenth of rectangle in cm :-"))
    
    wdt=int(input("Enter the width of rectangle in cm  :-"))

    ret=area_rect(len1,wdt)

    print("Area of rectangle  is:- ",str(ret) + " sqcm")

if __name__ == "__main__":
    main()    

#Output:-
#C:\Users\Shree\Desktop\Assignment_13>python Question_1.py
#Enter the lenth of rectangle :-5
#Enter the width of rectangle  :-6
#Area of rectangle is:-  30


    