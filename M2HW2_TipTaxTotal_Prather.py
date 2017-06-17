# This program calculates the total cost of a meal including tax and tip
# June 8,2017
# CTI-110 M2HW2 - Tip Tax Total
# Bruce Prather

#Input the cost of the meal
cost_meal = float(input('What is the price of the meal? '))

#Calculate the tip at 18% of the cost of the meal
tip = float(cost_meal * .18)

#Calculate the tax at 7% of the cost of the meal
tax = float(cost_meal * .07)

#Add cost of meal, tip and tax for the total
total_cost = (cost_meal + tip + tax)

#Display the cost of the tip
print ('The tip will be: $' , tip)
       
#Display the cost of the tax
print ('The tax will be: $' , tax)


#Display the total cost of the meal
print ('The combined cost of your meal to include tax and tip is: $' ,total_cost)
       

