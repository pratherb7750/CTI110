# This file will display a list of integers
# July 5, 2017
# CTI-110 M6T1 - File Display
# Bruce Prather
#


def main():
    myfile = open("numbers.txt" , "r")

    
    for line in myfile:
        line = line.rstrip()
        print(line)
    myfile.close()

main()

