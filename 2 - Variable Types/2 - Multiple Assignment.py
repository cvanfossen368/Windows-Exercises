#You can assign a single value to several variables simultaneously.
a = b = c = 1
#Here, an integer object is created with the value 1, and all three..
#..variables are assigned to the same memory location. You can also..
#..assign multiple objects to multiple variables.
print(a)
print(b)
print(c)
#All printed answers will be 1 up above.
a, b, c = 1, 2, "John"
#Here, two integer objects with values 1 and 2 are assigned to the..
#..variables a and b respectively, and one string object with the..
#..value "John" is assigned to the variable c.
print(a)
print(b)
print(c)
