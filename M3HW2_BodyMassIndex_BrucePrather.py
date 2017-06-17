# This program calculates and displays a person's BMI.
# Also, it will let them know if it is normal or not.
# June 16, 2017
# CTI-110 M3HW2 - Body Mass Index
# Bruce Prather
#

# Get the person's weight in pounds.

weight = int(input('How many pounds do you weigh? '))

# Get the person's height in inches.

height = int(input('How tall are you in inches? '))

# Calculate the BMI

BMI = weight * (703/height**2)

# Display the BMI to the User.

print ('Your body mass index is' ,(BMI))

# Let the user know if their BMI is normal, low or high.

if BMI < 18.5:
    print ('Your BMI is low, You should gain some weight')

elif BMI >= 18.5 and BMI <= 25:
    print ('Your BMI is perfect, keep doing what you are doing')

else:
    print ('Your BMI is high, you should try to loose some weight.')


