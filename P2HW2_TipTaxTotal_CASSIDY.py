#CTI-110
#P2HW2 - Tip Tax Total
#KYLE CASSIDY
#JULY 12,2018


FoodCost = float(input("input cost of meal"))
TipAmount = 0.18 * FoodCost
SalesTax = 0.07
SubTotal = FoodCost * SalesTax
TotalCost = FoodCost + SubTotal + TipAmount
 

print("Your Food Cost was",FoodCost)
print("Your Tax is ",SubTotal)
print ("Your TipAmount is ",TipAmount)
print ("Your TotalCost is ",TotalCost)
