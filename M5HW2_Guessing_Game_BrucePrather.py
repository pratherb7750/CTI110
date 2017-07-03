# This program wil generate a random number and then ask user to guess it.
# July 1, 2017
# CTI-110 M5HW2 - Random Number Guessing Game
# Bruce Prather
#


import random


# the main function get a random number, and calls on 2 other funtions.
def main():
    randNum = random.randint(1, 100)
               
    guess = 0 
   


    while guess != randNum:  # if not random will repeat guess_num and compare_nums.
            guess = guess_num ()
            compare_nums(guess, randNum)

    if guess == randNum:
        print ('Congratulations, you guessed right')

    print ()
    print ("Let's Play Again!")
    print ()
    main()  # repeats main() to play again

# this function will have the user input a guess for the random number.
def guess_num ():
    guess = int(input('Give me a number between 1 and 100 '))
    return guess

# this function compares the guessed number to the random number.
def compare_nums(num1 , num2):
    if num1 > num2:
        print ('Too high, try again')
    elif num1 < num2:
        print ('Too low, try again')
    
        
        
    

main ()
