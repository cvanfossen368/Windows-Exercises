#The following logical operators are supported by Python language.
#Assume variable a holds True and variable b holds False.

# and Logical AND : If both the operands are true then condition..
#..becomes true.
#(a and b) is False.
x = 20
print(x < 5 and x < 10)

# or Logical OR : If any of the two operands are non-zero then..
#..condition becomes true.
#(a or b is true)
print(x > 5 or x > 4)

# not Logical NOT : Used to reverse the logical state of its operand.
# Not(a and b) is true
print(not(x < 5 and x < 10))