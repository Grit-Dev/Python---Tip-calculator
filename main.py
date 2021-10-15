#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

billcost = 0 
howManyPeople = 0
percentOfTip = 0
totalValueOverall = 0
totalsplit = 0
perQ = 0
ONEHUNDRED = 100

billcost = float(input("How much did the bill come up to? \n"))

howManyPeople = (int(input("How many people are paying for the bill? \n")))

percentOfTip = (int(input("What percent of tip are you leaving? 10, 12 or 15?")))

perQ = percentOfTip / ONEHUNDRED

perQ = (billcost * perQ)
totalValueOverall = billcost + perQ
totalsplit = (totalValueOverall / howManyPeople)


print("Total", totalValueOverall, "Everyone pays £", "{:.2f}".format(totalsplit))
