#2: Write a Python program to implement a class named BankAccount with the following
#requirements:
#• The class should contain two instance variables:
#◦ Name (Account holder name)
#◦ Amount (Account balance)
#• The class should contain one class variable:
#◦ ROI (Rate of Interest), initialized to 10.5
#• Define a constructor (__init__) that accepts Name and initial Amount.
#• Implement the following instance methods:
#◦ Display() – displays account holder name and current balance
#◦ Deposit() – accepts an amount from the user and adds it to balance
#◦ Withdraw() – accepts an amount from the user and subtracts it from balance
#(Ensure withdrawal is allowed only if sufficient balance exists)
#◦ CalculateInterest() – calculates and returns interest using formula:
#Interest = (Amount * ROI) / 100

class BankAccount:
    ROI=10.5
    
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Deposit(self):
        
        amt=float(input("Enter the Amount need to Deposit:-"))
        self.Amount=self.Amount+amt

    def Withdraw(self):
        try:
            amt=float(input("Enter the Amount need to Withdraw:-"))
            if amt > self.Amount:
                print(f"Insufficient balance. Available: INR {self.Amount}\n")
                print("Can  not execute Transaction")
                exit()                  
                
                self.Amount=self.Amount - amt
            
        except ValueError:
                print("Invalid Transaction Amount")   
                print()

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

    def Display(self):
        print(f"Account Holder Name is {self.Name} and current Balance is {self.Amount}")


obj1=BankAccount("John",5000)  

obj2=BankAccount("Jim",5000)

print("*** Account Details ***")
obj2.Display()
print("-" * 30)

print("*** Deposit ***")
obj2.Deposit()
obj2.Display()
print("-" * 30)

print("*** Withdrawal ***")
obj2.Withdraw()
obj2.Display()
print("-" * 30)

print("*** Interest Calculation ***")
Interest = obj2.CalculateInterest()
print(f"Calculated Interest (at {BankAccount.ROI}% ROI): INR {Interest:.2f}")
print("-" * 30)

print("*** Account Details ***")
obj1.Display()
print("-" * 30)

print("*** Deposit ***")
obj1.Deposit()
obj1.Display()
print("-" * 30)

print("*** Withdrawal ***")
obj1.Withdraw()
obj1.Display()
print("-" * 30)

print("*** Interest Calculation ***")
Interest = obj1.CalculateInterest()
print(f"Calculated Interest (at {BankAccount.ROI}% ROI): INR {Interest:.2f}")
print("-" * 30)

# Output
# C:\Users\Shree\Desktop\Assignment_27>python Assignment27_2.py
# *** Account Details ***
# Account Holder Name is Jim and current Balance is 5000
# ------------------------------
# *** Deposit ***
# Enter the Amount need to Deposit:-1000
# Account Holder Name is Jim and current Balance is 6000.0
# ------------------------------
# *** Withdrawal ***
# Enter the Amount need to Withdraw:-8000
# Insufficient balance. Available: INR 6000.0
# 
# Can  not execute Transaction
# 
# C:\Users\Shree\Desktop\Assignment_27>python Assignment27_2.py
# *** Account Details ***
# Account Holder Name is Jim and current Balance is 5000
# ------------------------------
# *** Deposit ***
# Enter the Amount need to Deposit:-100
# Account Holder Name is Jim and current Balance is 5100.0
# ------------------------------
# *** Withdrawal ***
# Enter the Amount need to Withdraw:-1100
# Account Holder Name is Jim and current Balance is 5100.0
# ------------------------------
# *** Interest Calculation ***
# Calculated Interest (at 10.5% ROI): INR 535.50
# ------------------------------
# *** Account Details ***
# Account Holder Name is John and current Balance is 5000
# ------------------------------
# *** Deposit ***
# Enter the Amount need to Deposit:-200
# Account Holder Name is John and current Balance is 5200.0
# ------------------------------
# *** Withdrawal ***
# Enter the Amount need to Withdraw:-1200
# Account Holder Name is John and current Balance is 5200.0
# ------------------------------
# *** Interest Calculation ***
# Calculated Interest (at 10.5% ROI): INR 546.00
# ------------------------------

