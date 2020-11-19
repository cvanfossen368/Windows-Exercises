#Example 1
high_income = False
good_credit = True

if high_income and good_credit:
  print("Eligible")
else:
    print("Not eligible")

#Example 2
high_income = True
good_credit = True

if high_income or good_credit:
  print("Eligible")
else:
    print("Not eligible")   

#Example 3
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
  print("Eligible")
else:
    print("Not eligible")  

#Example 4
high_income = True
good_credit = True
student = False

if not student:
  print("Eligible")
else:
    print("Not eligible") 

#Example 5
#Short Circuit
high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

#Example 6
#Short circuit
high_income = False
good_credit = True
student = True

if high_income or good_credit and or student:
    print("Eligible")
