# This is a file reader program
# July 11, 2017
# CTI-110 M6HW2 - Random Number File Reader
# Bruce Prather
#


import random

def main():
    num_file=open('rand_num.txt' , 'r')
    total = 0
    count = 0

    for line in num_file:
        num = int(line)
        count += 1
        print (count, ':' ,'\t' , num , sep='')
        total += num
        avg = total/count
    num_file.close()
    

    print ('----------')
    print ('The total of all the numbers is: ' , total)
    print()
    print ('The number of random numbers read from the file is: ' , count)
    print ()
    print ('The average of all the random numbers is: ' , avg)

main()
