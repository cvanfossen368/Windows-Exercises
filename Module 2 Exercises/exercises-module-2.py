#Module 2: Practice Exercises
#Exercise 1
#input the number of elements in the list
n=int(input())
#create the split slit
l=[int(x) for x in input().split() [:n]]
#print the list
print(l)
#lock in/tuple the list
tuple(l)
#hash/secure the tuple
hash(tuple)

#Explaining: if name == main in relation with Functions
# Python program to execute  
# main directly

# block 2
if __name__ == "__main__": 
    print("Executed when invoked directly")
else: 
    print("Executed when imported")

# Python program to execute  
# function directly 
def my_function(): 
      print("I am inside function")
  
# We can test function by calling it. 
my_function() 

from itertools import islice

def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))

#Exercise 2
#Take the following two lists. Create a third list by picking a odd-index elements from the first list and even-index elements from the second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)

#Exercise 3
#Take the following list. Slice it into three equal chunks and reverse each list.
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sampleList)

length = len(sampleList)
chunkSize  = int(length/3)
start = 0
end = chunkSize
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize

#Exercise 4
#Iterate through a given list and check if a given element already exists in a dictionary as a key’s value. If not, delete it from the list.
rollNumber  = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict  ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97} 

print("List -", rollNumber)
print("Dictionary - ", sampleDict)

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)

#What is a Lambda function?
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
full_name('guido', 'van rossum')

#Extra Points
#1. Write a Python program that converts a tuple to a string.
#Create immutable objects
tuple = ('Greg', 'James', 'Sam', 'Cole', 'Lisa', 'Shaina', 'Jennifer')
#Join each element of the tuple by a string separator and return the string.
str = ''.join(tuple)
#print the string
print(str)

#2. Write a Python program to check whether an element exists within a tuple.
# declare a tuple
t = (4,5,7,14)
# find value/element
element = 7
if element in t:
    #If element exists, outcome will be true.
    print(element,"exists in tuple")
else:
    #If element does not exist, outcome will be false.
    print(element,"does not exist in tuple")

#3. Write a Python program to print a tuple with string formatting.
#Declare the tuple.
tuple = (100, 200, 300)
#Print the string.
#{0} is a placeholder for the first argument.
#.format() returns a formatted representation of the given value controlled by the format specifier.
print('This is a tuple {0}'.format(tuple))

