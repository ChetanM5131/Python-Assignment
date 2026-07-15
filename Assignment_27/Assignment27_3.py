#3: Write a Python program to implement a class named Numbers with the following
#specifications:
#• The class should contain one instance variable:
#◦ Value
#• Define a constructor (__init__) that accepts a number from the user and initializes Value.
#• Implement the following instance methods:
#◦ ChkPrime() – returns True if the number is prime, otherwise returns False
#◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
#◦ Factors() – displays all factors of the number
#◦ SumFactors() – returns the sum of all factors
#• Create multiple objects and call all methods.

class Numbers:

    def __init__(self,Value):
        
        self.Value=int(Value)

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2,self.Value):
            if self.Value % i==0:
                return False
        return True    


    def ChkPerfect(self):
        if self.Value <= 0:
            return False
        
        sum_proper_factors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_proper_factors += i
                
        return sum_proper_factors == self.Value
    
    def Factors(self):
        l1=[]
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                l1.append(i)
        return l1        

    def SumFactors(self):
        total_sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total_sum += i
        return total_sum
    
num1 = int(input("Enter a number for Object 1: "))
obj1=Numbers(num1)



print("*** Object 1 ***")

print(f"Is Prime Number:- {obj1.ChkPrime()}")
print(f"Is Perfect Number:- {obj1.ChkPerfect()}")
obj1.Factors()
print(f"Sum of factors: {obj1.SumFactors()}")
print("-" * 30)

num2 = int(input("Enter a number for Object 2: "))
obj2=Numbers(num2)
print("*** Object 2 ***")

print(f"Is Prime Number:- {obj2.ChkPrime()}")
print(f"Is Perfect Number:- {obj2.ChkPerfect()}")
obj2.Factors()
print(f"Sum of factors: {obj2.SumFactors()}")
print("-" * 30)

# Output
# C:\Users\Shree\Desktop\Assignment_27>python Assignment27_3.py
# Enter a number for Object 1: 7
# *** Object 1 ***
# Is Prime Number:- True
# Is Perfect Number:- False
# Sum of factors: 8
# ------------------------------
# Enter a number for Object 2: 28
# *** Object 2 ***
# Is Prime Number:- False
# Is Perfect Number:- True
# Sum of factors: 56
# ------------------------------