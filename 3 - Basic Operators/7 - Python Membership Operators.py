#Python's membership operators test for membership in a..
#..sequence, such as strings, lists, or tuples. There are..
#..two membership operators as explained below.

a = 10
b = 20
list = [1, 2, 3, 4, 5]

# in : Evaluates to True if it finds variable in the specified
#sequence and False otherwise.
#x in y, here in results in a 1 if x is a member of sequence y.
if ( a in list):
    print("Line 1 - a is available in the given list.")
else:
    print("Line 1 - a is not available in the given list.")

# not in : Evaluates to True if it does not find a variable in..
#..the specified sequence and False otherwise.
#x not in y, here not in results in a 1 if, x is not a member of..
#..sequence y.
if ( b not in list ):
    print("Line 2 - b is not available in given list.")
else:
    print("Line 2 - b is available in the given list.")

c = 1
c = b/a

if (c in list ):
    print("Line 3 - a is available in the given list.")
else:
    print("Line 3 - a is not available in the given list.")


