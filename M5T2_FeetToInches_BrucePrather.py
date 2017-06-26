# This program will convert feet to inches
# June 26 2017
# CTI-110 M5T2_FeetToInches
# Bruce Prather

# Define main function

def main():   
    print ('This will help you convert feet to inches')
    feet()  #call on the feet function

#Define the feet function and convert the feet to inches
         
def feet():
    num_feet = int(input('Please enter the number of feet '))
    num_of_inches = num_feet * 12
    print ('The number of inches is  ' , num_of_inches)
    

#This will run the main function and call on the feet function
main ()
