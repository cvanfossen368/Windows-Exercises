#Identy operators compare the memory locations of two objects.
#Python built-in function id() returns a unique integer as identity of object.
#There are two Identy operators as explained below.

# is : Evaluates to true if the variables on either side of the..
#..operator point to the same object and false otherwise.
# x is y, here is results in 1 if id(X) equals id(y).

a = 20
b = 20
print('Line 1', 'a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
    print("Line 2 - a and b have same identy.")
else:
    print("Line 2 - a and b do not have same identity.")

if ( id(a) == id(b) ):
    print("Line 3 - a and b have same identity.")
else:
    print("Line 3 - a and b do not have same identity.")

# is not : Evaluates to false if the variables on either side of the..
#operator point to the same object and true otherwise.
# x is not y, here is not results in 1 if id(x) is not equal to id(y).

b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if (a is not b ):
    print ("Line 5 - a and b do not have same identity.")
else:
    print("Line 5 - a and b have same identity.")

#OTHER EXAMPLES:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print (x is z)
#Returns True because z is the same object as x.

print(x is y)
#Returns False because x is not the same object as y,
#even if they have the same content.

print(x == y)
#To demonstrate the difference between "is" and "==":
#This comparison returns True because x is equal to y.

print(x is not y)
#Returns True because x is not the same object as y,
#even if they have the same content.

