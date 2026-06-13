#What is the purpose of getsizeof()? Why memory size is different for different datatype?
from sys import getsizeof
a=10
b='10'
c=10.0
print(a)
print(getsizeof(a))
print(b)
print(getsizeof(b))
print(c)
print(getsizeof(c))

#getsizeof() return the sizeof memory required to store the value and it is different for each datatype.