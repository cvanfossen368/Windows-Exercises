#The Loop control statements change the execution from its normal sequence. When the execution leaves a scope, all automatic objects that were created in that scope are destroyed.

#Break Statement : Terminates the loop statement and transfers execution to the statement immediately following the loop.
for letter in 'Python': #First Example
    if letter == 'h':
       break
    print('Current Letter :', letter)

var = 10                #Second Example
while var > 0:
    print ('Current variable value:', var)
    var = var -1
    if var == 5:
       break

print("Good bye!")

#The following program demonstrates use of the brwak in a for loop iterating over a list. User inputs a number, which is searched in the list. If it is found, then the loop..
#..terminates with the 'found' message.

no = int(input('any number: '))
numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num == no:
      print('number found in list')
      break
else:
    print('number not found in list')

#Continue Statement : Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")
