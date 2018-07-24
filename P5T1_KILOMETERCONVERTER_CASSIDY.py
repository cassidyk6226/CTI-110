#CTI-110
#P5T1 Kilometer Converter
#KYLE CASSIDY
#JULY 24,2018

def main():

    

#Get the distance in kilometers.
    km = float(input("Enter a distance in kilometers: "))

#Display the distance converted to miles.
    show_miles(km)

def show_miles(km):
    CONVERSION_FACTOR = 0.6214
    #Calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, "kilometers equals", miles, "miles.")
    

main()

