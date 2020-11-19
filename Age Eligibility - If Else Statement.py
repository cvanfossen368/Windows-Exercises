#option 1
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
    
#option 2
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

#option 3
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

#option 4
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
#Repeat to show you can have the same code in twice, but will still get only one result.
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

