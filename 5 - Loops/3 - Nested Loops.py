# Nested Loops : You can use one or more loop inside any other while, or for loop.
#Python programming language allows the usage of one loop inside another loop.

#Example:
#The following program uses a nested-for loop to display multiplication tables from 1-10

import sys
for i in range(1,11):
   for j in range(1,11):
       k = i*j
       print(k, end=' ')
   print()

#The print() function innter loop has end='' which appends a space instead of default newline. Hence, the numbers will appear in one row.
#Last print() will be executed at the end of inner for loop