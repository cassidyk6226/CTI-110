#CTI-110
#P3HW1 Age Classifier
#KYLE CASSIDY
#JULY 17,2018


#If the person is 1 year old or less, he or she is an infant.
#If the person is older than one year, but younger than 13 years old, he or she is a child.
#If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
#If the person  is at least 20 years old, he or she is an adult.

goOn = 'y'

while goOn == "y":
    
        age = int(input('what is your age,?'))
    

        if (age < 1):
            {print ("Infant:")}

        elif (age < 13):
            {print ("Child:")}

        elif (age < 20):
            {print ("Teenager:")}
        else:
            {print ("Adult:")}
        goOn = input("Would you like to go again? ")
    
     
