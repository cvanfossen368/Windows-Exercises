#In general, statements are executed sequentially - The first statement in a function is executed first, followed by the second, and so on.
#There may be a situation when you need to execute a block of code several number of times.

#Programming languages provide various control structures that allow more complicated execution path.

#A loop statement allows us to execute a statement or group of statements multiple times.

# While Loop : Repeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body.
count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

#Infinite Loop:
#A loop becomes infinite if a condition never becomes FALSE.
#Might be useful in client/server programming where the server needs to run continuously so the client programs can communicate with it as and when required.

var = 1
while var == 1 : #This constructs an infinite loop
    num = int(input("Enter a number  :"))
    print("You enter: ", num)
    break #Break will end infinite loops

print("Good bye!")

#Using else Statements with Loops
#Python supports having an else statement associated with a loop statement.
#* If the else statement is used with a for loop, the else statement is executed when the loop has exhausted iterating the list.
#If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

#The following example illustrates the combination of an else statement with a while statement that prints a number as long as it is less than 5, otherwise the else..
#..statement gets executed.

count = 0
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

#Single statement suites:
#Similar to the if statement syntax, if your while clause consitsts only of a single statement, it may be placed on the same line as the while header.

#One-line while clause -

flag = 1
while (flag): print('Given flag is really true!')
print("Good bye!")
