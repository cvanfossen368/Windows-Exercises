#1. Guess a number between 1 to 9 given by the user.
import random

target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

#2. Check the validity of password input by the user. Hint. Re which does matching operations much like Perl.
#Validation:
#At least 1 letter between [a-z] and 1 letter between [A-Z].
#At least 1 number between [0-9].
#At least 1 character from [$#@].
#Minimum length 6 characters.
#Maximum length 16 characters.
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

#3. Get input of the age of 3 people by user and determine oldest and youngest among them.
#Input Ages
number1 = int(input("Enter First Person's Age : "))
number2 = int(input("Enter Second Person's Age : "))
number3 = int(input("Enter Third Person's Age : "))
#Check For The Oldest Person
if number1 > number2 and number1 > number3:
    print("The firt person is the oldest")
elif number2 > number1 and number2 > number3:
    print("The second person is the oldest")
elif number3 > number1 and number3 > number2:
    print("The third person is the oldest")
#Check For The Youngest Person
if number1 < number2 and number1 < number3:
    print("The first person is the youngest")
elif number2 < number1 and number2 < number3:
    print("The second person is the youngest")
elif number3 < number1 and number3 < number2:
    print("The third person is the youngest")

#4. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
#Take following input from user

#Number of classes held.
totalClassesHeld = eval(input("Enter total number of classes held in school : "))   
#Number of classes attended.
totalClassesAttend = eval(input("Enter total number of classes attended by the student : "))
#And print percentage of class attended
percent = (totalClassesAttend / totalClassesHeld) * 100
#Is student is allowed to sit in exam or not?
if percent < 75:
    print("You cannot sit in the exams as your attendance is too low!")
else:
    print("You can sit in the exams as your attendance is fine.")

#5. Get an integer N from the user and perform the following actions:
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
if __name__ == '__main__':
    N = int(input())
num = N % 2
if num > 0:
    print("Weird")
elif num == 0 and range(6,20):
    print("Weird")
elif num == 0 and range(2,5):
    print("Not Weird")
elif num == 0 and N > 20:
    print("Not Weird")

#Extra Points
#1. Write a Python program to reverse a string.
#[::-1] reverses string from last character.
str = "1234abcd" [::-1]
#prints reversed string
print(str)

#2.  Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))

#3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')
