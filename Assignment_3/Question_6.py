from sys import getsizeof
print("Enter Variable value:")
var1=input()
print("Data Type is",type(var1))
print("Address is",id(var1))
print("Size is ",getsizeof(var1))