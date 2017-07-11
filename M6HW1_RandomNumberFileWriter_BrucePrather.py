# This program will write random numbers to a file.
# July 11, 2017
# CTI-110 M6HW1 - Random Number File Writer
# Bruce Prather
#

import random

def main():
    num_nums=int(input('How many numbers do you wish to create? '))
    num_file=open('rand_num.txt' , 'w')
    print()
    print('These random numbers were written to rand_num.txt: ')
    
    for count in range(1 , num_nums + 1):
        randNum=random.randint(1, 500)
        num_file.write (str(randNum)+ '\n')
   
        print(randNum)
    num_file.close()


main()

    
    
