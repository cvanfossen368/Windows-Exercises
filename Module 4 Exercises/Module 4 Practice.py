#Defining Functions
#Functions become even more useful when we begin to define our own, organizing functionality to be used in multiple places. In Python, functions are defined with the def statement. For example, we can encapsulate a version of our Fibonacci sequence code from the previoussection as follows:
def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
#Run with fibonacci(10)
#Result - [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#If you're familiar with strongly-typed languages like C, you'll immediately notice that there is no type information associated with the function inputs or outputs. Python functions can return any Python object, simple or compound, which means constructs that may be difficult in other languages are straightforward in Python.

#For example, multiple return values are simply put in a tuple, which is indicated by commas:

def real_imag_conj(val):
    return val.real, val.image, val.conjugate()
    r, i, c = real_image_conj(3 + 4j)
    print(r, i, c)
