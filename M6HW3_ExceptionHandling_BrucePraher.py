# This is a exception handler program
# July 16, 2017
# CTI-110 M6HW3 - Exception Handling
# Bruce Prather
#


import random

def main():
    try:
        fileName= input('Enter a random number filename: ')
        num_file=open(fileName , 'r')
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

    except IOError:
        print('An error occured trying to read the file:' , fileName)

    except ValueError:
        print('Non-numeric data found in the file: ' , fileName)
    except:
        print ('A error occured.')
        

main()
