#CTI-110
#P5T2 Feet To Inches
#KYLE CASSIDY
#JULY 24,2018

def main():

    

#Get the distance in feet.
    ft = float(input("Enter a distance in feet: "))

#Display the distance converted to inches.
    show_inches(ft)

def show_inches(ft):
    CONVERSION_FACTOR = 12
    #Calculate inches.
    inches = ft * CONVERSION_FACTOR

    #Display the inches.
    print(ft, "feet equals", inches, "inches.")
    

main()
