#Decision-making is the anticipation of conditions occuring during the excution of..
#..a program and specified actions taken according to the conditions.

#Decision structures evaluate multiple expressions, which produce TRUE or FALSE as..
#..the outcome. You need to determine which action to take and which statements to..
#..execute if the outcome is TRUE or FALSE otherwise.

#The following is the general form of a typical decision making structure found in..
#..most of the programming languages.

#                    |
#                    |
#                    |
#                    V
#                Condition__________
#                    |              |
#        If condition|              |
#             is true|  If condition|
#                    V      is false| 
#                Condition          V
#                  Code             |
#                    |              |
#                    |______________|
#                    |
#                    V
#                  _____
#                  |   |
#                  |___|

#Python programming language assumes any non-zero and non-null values as TRUE, and..
#..any zero or null values are FALSE value.

#Python programming language provides the following types of decision-making statements.
# if statements : An if statement consists of a boolean expression followed by one or..
#..more statements.
var1 = 100
if var1:
    print("1 - Got a true expression value.")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value.")
    print(var2)
print("Good bye!")

# if...else statements : An if statement can be followed by an optional else statement, which..
#..executes when the boolean expression is FALSE.
amount = int(input("Enter amount: "))

if amount<1000:
    discount = amount*0.05
    print("Discount",discount)
else:
    discount = amount*0.10
    print("Discount",discount)
print("Net payable:",amount-discount)

# nested if statements :You can use one if or else if statement inside another if or else if statments(s).
num = int(input("Enter number:"))
if num%2 == 0:
   if num%3 == 0:
      print("Divisible by 3 and 2")
   else:
      print("Divisible by 2 not divisible by 3")
else:
   if num%3 == 0:
      print("Divisible by 3 not divisible by 2")
   else:
      print("Not divisible by 2 not divisible by 3")
