# 3: Write a Python program to implement a class named Arithmetic with the following
# characteristics:
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
# ◦ Accept() – accepts values for Value1 and Value2 from the user.
# ◦ Addition() – returns the addition of Value1 and Value2.
# ◦ Subtraction() – returns the subtraction of Value1 and Value2.
# ◦ Multiplication() – returns the multiplication of Value1 and Value2.
# ◦ Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).
# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self):
        self.Value1=int(input("Enter Value1:- "))   
        self.Value2=int(input("Enter Value2:- "))     

    def Addition(self):
        return self.Value1 + self.Value2  

    def Subtraction(self):
        return self.Value1 - self.Value2   

    def Multiplication(self):
        return self.Value1 * self.Value2  

    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError: 
            return "Error: Division by zero is not allowed"     
    
obj1=Arithmetic()

obj2=Arithmetic()

print("** For obj1 **")
obj1.Accept()
print("Addition:- ",obj1.Addition())
print("Subtraction:- ",obj1.Subtraction())
print("Multiplication:- ",obj1.Multiplication())
print("Division:- ",obj1.Division())


print("** For obj2 **")
obj2.Accept()
print("Addition:- ",obj2.Addition())
print("Subtraction:- ",obj2.Subtraction())
print("Multiplication:- ",obj2.Multiplication())
print("Division:- ",obj2.Division())

# Output
# C:\Users\Shree\Desktop\Assignment_26>python Assignment26_3.py
# ** For obj1 **
# Enter Value1:- 5
# Enter Value2:- 3
# Addition:-  8
# Subtraction:-  2
# Multiplication:-  15
# Division:-  1.6666666666666667
# ** For obj2 **
# Enter Value1:- 10
# Enter Value2:- 2
# Addition:-  12
# Subtraction:-  8
# Multiplication:-  20
# Division:-  5.0