# 1: Write a Python program to implement a class named Demo with the following
# specifications:
# • The class should contain two instance variables: no1 and no2.
# • The class should contain one class variable named Value.
# • Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# • Implement two instance methods:
# ◦ Fun() – displays the values of instance variables no1 and no2.
# ◦ Gun() – displays the values of instance variables no1 and no2.
# Create two objects of the Demo class as follows:
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)
# Call the instance methods in the given sequence:
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    value=10

    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2

    def fun(self):

        print("Inside fun()")
        print("Value of no1 is:-",self.no1)
        print("Value of no2 is:-",self.no2)  

    def gun(self):

        print("Inside fun()")
        print("Value of no1 is:-",self.no1)
        print("Value of no2 is:-",self.no2)  

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)   

Obj1.fun()
Obj2.fun()
Obj1.gun()
Obj2.gun()

# Output
# C:\Users\Shree\Desktop\Assignment_26>python Assignment26_1.py
# Inside fun()
# Value of no1 is:- 11
# Value of no2 is:- 21
# Inside fun()
# Value of no1 is:- 51
# Value of no2 is:- 101
# Inside fun()
# Value of no1 is:- 11
# Value of no2 is:- 21
# Inside fun()
# Value of no1 is:- 51
# Value of no2 is:- 101