import numpy

def arrays(arr):
#Definite arrays, used to store multiple values in one single varriable, as arr.
    numpy.set_printoptions(legacy='1.13')
#Set to 1.13 legacy printing option.
#This includes a space in the sign posiition of floats and different behavior for 0d arrays.
    arr = numpy.array(arr[ : : -1], dtype = "float")
    #arr is the array that will be printed in reverse, and each element will be a float.
    return(arr)
    #Return arr back to the caller, array.
arr = input().strip().split(' ')
#Take the input (input()).
#Delete the white spaces from the beginning to the end of the input (strip()).
#Split the input into elements of a list with (' ') being as separator.
result = arrays(arr)
#The result is arrays(arr)
print(result)
#print result