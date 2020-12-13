#Bitwise operator works on bits and performs bit-by-bit operation.
#Assume if a = 60; and b = 13; Now in binary format they will be..
#..as follows.
a = 60
b = 13
# a = 0011 1100
# b = 0000 1100

# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a = 1100 0011

#Python's built-in function bin() can be used to obtain binary..
#..representation of an integer number.
#The following Bitwise operatators are supported by Python language.

# & Binary AND : Operator copies a bit to the result if it exists..
#.. in both operands.
# (a & b) (means 0000 1100)
print('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

# & Binary AND : Operator copies a bit to the result if it exists..
#.. both operands.
# (a & b) (means 0000 1100)
c = a & b; # 12 = 0000 1100
print("result of AND is ", c,':', bin(c))

# | Binary OR : Copies a bit if it exists in either operand.
# (a | b) = 61 (means 0011 1101)
c = a | b; # 61 = 0011 1101
print("result of OR is ", c,':',bin(c))

# ^ Binary XOR : Copies the bit if it is set in one operand but not both.
# (a ^ b) = 49 (means 0011 0001)
c = a ^ b; # 49 = 0011 0001
print("result of EXOR is ", c, ':',bin(c))

# ~ Binary Ones Complement : Is unary and hass the effect of 'flipping' bits.
# (~a) = -61 (means 1100 0011) in 2's complement form due to a signed binary number.
c = ~a; # -61 = 1100 0011
print("result of COMPLEMENT is ", c, ':',bin(c))

# << Binary Left Shift : The left operands value is moved left by the number..
#..of bits specified by the right operand.
# a << = 240 (means 1111 0000)
c = a << 2; # 240 = 1111 0000
print("result of LEFT SHIFT is ", c, ':',bin(c))

# >> Binary Right Shift : The left operands value is moved right by the number..
#..of bits specified by the right operand.
# a >> = 15 (means 0000 1111)
c = a >> 2; # 15 = 0000 1111
print("result of RIGHT SHIFT is ", c, ':',bin(c))

