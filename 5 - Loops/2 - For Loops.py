# For Loop : Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

#The range() function:
#The built-in function range() is the right function to iterate over a sequence of numbers. It generates an iterator of..
#..arithmetic progression.

#Example:
range(5)
range(0,5)
list(range(5))
[0, 1, 2, 3, 4, 5]

#Example:
#Range() generates an iterator to progress integers starting with 0 up to n-1. To obtain a list object of the sequence, it..
#..is typecasted to list(). Now this list can be iterated using the for statement.
for var in list(range(5)):
    print(var)

#Example:
for letter in 'Python': #traversal of a string sequence
    print('Current Letter :', letter)
print()
fruits = ['banana', 'apple', 'mango']

for fruit in fruits: #traversal of List sequence
    print('Current fruit :', fruit)

print("Good bye!")

#Iterating by Sequence Index
#An alternative way of iterating through eeach item is by index offset into the sequence itself.

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('Current fruit :', fruits [index])

print("Good bye!")

#Here, we took the assistance of the len() built-in function, which provides the total number of elements in the tuple as well as the range()..
#..built-in function to give us the actual sequence to iterate over.

#Using else Statement with Loops
#Python supports having an else statement associated with a loop statement.
#*If the else statement is used with a for loop, the else block is executed only if for loop terminates normally (and not by encountering break statement.).
#*If the lese statement is used with a while loop, the else statement is executed when the condition becomes false.

#The following example illustrates the combination of an else statement with a for statement that searches for even number in given list.

number = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
    if num%2 == 0:
        print('The list contains an even number')
        break
else:
    print('The list does not contain an even number')

