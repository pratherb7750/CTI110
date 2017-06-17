# This program totals number of bugs a collector collects in 5 days
# June 15, 2017
# CTI-110 M4T1 - Bug Collector
# Bruce Prather
#

#Initialize the accumulator
total = 0
    
#Get the number of bugs collected each day.

for day in range(1 , 6):
    
    #Ask (prompt) the user how many bugs.
    print ('How many bugs did you collect on day?' , day)

    #Input the number of bugs
    bugs = int(input("enter the number of bugs here "))
    total = total + bugs

# Display the total amount of bugs collected
print ("The total number of bugs collected for 5 days is:" , total)


