# Predict the output
a=10
b=10
print(id(a)==id(b))
# Output:-
#True

# As identifier a and b both have same value and have same datatype.
# As per python internal architecture and memory management python will not create new memory address for b. 
#It will point it to same memory address where value of a is stored.
# as a and b have same value and same datatype