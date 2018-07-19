#CTI-110
#P3HW2 Software Sales
#KYLE CASSIDY
#JULY 18,2018

units = int(input("Enter number of units:"))

if (units <= 10):
    print("no discount:")

elif (units <= 19):
     print("10% discount:")
           

elif (units <= 49):
     print("20% discount:")

elif (units <= 99):
     print("30% discount:")

else:
     print("40% discount:") 
