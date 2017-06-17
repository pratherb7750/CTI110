# This program will calculate Area of a Rectangle
# Date June 12, 2017
# CTI-110 M3T1 - Areas of Rectangles
# Bruce Prather

#Input the Lengtn and Width of rectangle 1

Length_1 = int(input('What is the length in feet of first rectangle? '))

Width_1 = int(input('What is the Width in feet of first rectangle? '))

Area_1 = Length_1 * Width_1

# Calculate and print the area of rectangles 1

print ('The area of the Rectangle 1 is ' , (Area_1) ,'square feet')

# Input the Length and Width of rectanble 2

Length_2 = int(input('What is the length in feet of second rectangle? '))

Width_2 = int(input('What is the Width in feet of second rectangle? '))

Area_2 = Length_2 * Width_2

# Calculate and print the area of rectangles 2

print ('The area of the Rectangle 2 is ' , (Area_2) ,'square feet')


# Determine which rectangle has more area or if same

if Area_1 > Area_2:
	print ('area_1 is greater')

if Area_2 > Area_1:
        print ('area_2 is greater')

if Area_1 == Area_2:
        print ('both are same')

print ('Done')


    






             
