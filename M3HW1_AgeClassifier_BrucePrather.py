# This program will determine if a person is an infant, child, teenager or adult. 
# Date: June 14, 2017
# CTI-110 M3HW1 - Age Classifier
# Bruce Prather


# Get the person's age
age = int(input ("What is the individual's age? "))

if age <= 1:
    person = "infant"

elif age > 1 and age < 13:
    person = "child"

elif age >= 13 and age < 20:
    person = "teenager"

elif age >= 20 and age <120:
    person = "adult"

else:
    person = "a very dead person"

print ("This is a ",person)      
