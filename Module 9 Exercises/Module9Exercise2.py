import numpy
#Import Numpy, which contains multi-dimensional array and matrix data structures.
#It can be used to perform a number of mathematical operations on arrays such as..
#..trigonometric, statistical, and algebraic routines.
arr = list(map(float,input().split()))
#Arr is made into a list, and map executes the function.
#The input value will be read as a float
#The input will be split into a list of elements.
value = int(input())
#The input value will be read as an integer.
print(numpy.polyval(arr,value))
#Print the polynomial evaluated as a specific value.