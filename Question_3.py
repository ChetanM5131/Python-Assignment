# What does id() return?Is the value return by fid() same for two variable holding the same value
a=10
b='10'
c=10.0
d=10
print(a)
print(id(a))
print(b)
print(id(b))
print(c)
print(id(c))
print(d)
print(id(d))

#Output:-
10
140729241814424
10
2691961604592
10.0
2691961363568
10
140729241814424

# id() function return memory address of object but it depend on datatype of object
