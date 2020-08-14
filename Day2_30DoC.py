mealcost = float(input())
tippercent = int(input())
taxpercent = int(input())

tip = mealcost * (tippercent/100)
tax = mealcost * (taxpercent/100)

totalcost = mealcost + tip + tax
print(round(totalcost))