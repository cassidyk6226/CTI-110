#CTI-110
#P3LAB - DEBUGGING / GRADES
#KYLE CASSIDY
#JULY 19,2018

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    
    # TO DO: define the rest of the scores

    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
        print('Your numeric grade of',score,'is an A!')
    
    elif score > B_score:
        print('Your grade is: B')
        print('Your numeric grade of',score,'is an B!')
     
    elif score > C_score:
        print('Your grade is: C')
        print('Your numeric grade of',score,'is an C!')
              
    elif score > D_score:
        print('Your grade is: D')
        print('Your numeric grade of',score,'is an D!')
              
    else:
        print('Your grade is: F') 
        print('Your numeric grade of',score,'is an F!')
              
    
            





# program start
main()
