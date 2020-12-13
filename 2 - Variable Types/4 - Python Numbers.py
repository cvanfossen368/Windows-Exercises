#Number data typles store numeric values. Number objects are..
#created when you assign a value to them.
var1 = 1
var2 = 10
print(var1)
print(var2)
#You can  delete the reference to a number object by use the del..
#..statement. The syntax of the del statement is -
#del var1[,var2[,var3][...,varN]]
#Single object deletion
del var1
del var2
#Store new values
var1 = 2
var2 = 20
print(var1)
print(var2)
#Multiple Object Deletion
del var1, var2
#You will receive an error if you attempt to print var1 or var2 again..
#..without a value being assigned to them.

#Three supported numerical types
#int (signed integers)
#float (floating point real values)
#complex (complex numbers)
int = 10
float = 0.0
complex = 3.14j
#Complex numbers consist of an ordered pair of real floating-point numbers..
#..denoted by x + yj, where x and y are real numbes and j is the imaginary..
#..unit.
print(int)
print(float)
print(complex)