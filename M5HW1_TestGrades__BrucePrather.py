# This program will average test scores and determine final grade
# Date June 29, 2017
# CTI-110 M5HW1 - Test Average and Grade
# Bruce Prather
#

#The main function will get test scores and average them,
#It will also determine the letter grade and print the output.
def main ():
    ts1 = int(input('Enter score for test 1  '))
    ts2 = int(input('Enter score for test 2  '))
    ts3 = int(input('Enter score for test 3  '))
    ts4 = int(input('Enter score for test 4  '))
    ts5 = int(input('Enter score for test 5  '))
    print ('______________________________') 
    print ('Final Score\t ' , 'Letter Grade')
        
    average = calc_average (ts1, ts2, ts3, ts4, ts5)
      
    
    grade = determine_grade(average)
    
    print (average , '\t' , '\t' , '\t' , grade)    




    

#This will average the test score and return average to main function.
        
def calc_average (ts1 ,ts2 , ts3 , ts4 ,ts5):
    average = (ts1 + ts2 + ts3 + ts4 + ts5) /5
    return average
    
   
    
# This will determine final grade
def determine_grade (score):
    
    if score >= 90:
        grade = ('A')
    elif score >= 80 and score < 90:
        grade = ('B')
    elif score >= 70 and score < 80:
        grade = ('C')
    elif score >= 60 and score < 70:
        grade = ('D')
    else:
        grade = ('F')
    return grade


main()
