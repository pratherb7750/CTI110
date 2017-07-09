# This program list all of the numbers in the numbes.txt file and add them
# up. It then presents the sum of all of the numbers
# July 8, 1017
# CTI-110 M6LAB
# Bruce Prather
#






def main():
    num_file = open('numbers.txt' , 'r')
    print ('We will list all of the numbers and then add them up.')
    print ()  

    total = 0
    count = 0

    for line in num_file:
        num = int(line)
        count += 1
        print (count, ':' ,'\t' , num , sep='')
        total += num

    num_file.close()

    print ('----------')
    print ('The total of all the numbers is: ' , total)

main()
