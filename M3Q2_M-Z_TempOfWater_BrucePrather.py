# Question M3Q2_M-Z
# Bruce Prther
# June 13, 2017

# This will determine type of sample of water based on the temperature

water_temp = float(input('Enter the temperature of the water: '))

if water_temp <= 0:
    type = "ice"
elif water_temp <= 100:
    type = "liquid water"
elif water_temp > 100:
    type = "steam"
print ('The condition of the water is: ', type)

