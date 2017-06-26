# This will convert kilometers in miles
# June 26 2017
# CTI-110 M5T1_KilometerConverter 
# Bruce Prather
#


# Define the main function
def main():
    kilometers = int(input('Enter the distance in kilometers   '))
    miles = kilometers * 0.6214
    print ('The distance you traveled is ' , format(miles, ',.2f'), 'miles')


# Call the main function

main()

