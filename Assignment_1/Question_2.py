a=10
b=10
print(id(a))
print(id(b))
a=[10]
b=[10]
print(id(a))
print(id(b))

#Output:-
140729241814424
140729241814424
1827775362496
1827775246272
#a=10 and b=10 are integer values of a and b will have same value and same memory address (Hash Address)
#a=[10] and b=[10] are two list objects haveing integer 10 but have different memory address (Hash Address)