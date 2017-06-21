#This program calculates the amount in dollars of working for pennies
#June 19,2017
#CTI-110 M4HW2_Pennies_For_Pay
#Bruce Prather


#Set the accumlator, totalAmount, to 0.
totalAmount = 0

# Ask user how many days

num_days = int(input('How many days did you work?'))

# Name columns for table
print ('\t' , "DAY" , '\t' , '\t' ,'\t' , "PAY")

#Set range to number of days worked plus 1.
for days in range (1, (num_days + 1)):
    
    #if day worked is 1 or 2 then divide that by 100
    if days == 1 or days ==2:
        print ('The salary for day' , days , 'is,' , '\t' , '$', (days /100))
        
    #if days worked is more than 2 then subtract 1 and use for exponent for 2
    #the divide by 100.    
    else:
        print ('The salary for day' , days , 'is' , '\t' ,  '$',  (2 ** (days - 1)/100))

#Calculate the total amount of dollars earned.
penniesPerDay = 2 ** days
totalAmount += penniesPerDay
totalSalary = (totalAmount - 1) / 100


print ('Your total Salary =' , '\t', '\t' , '$' ,(totalSalary))


        
    


    
