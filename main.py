#For this assignment, you will create a program that that calculates the compound interest of a starting pool of money after a variable number of years. Your program should do the following:

#Ask for the user's name and capture it for display later.
#Ask for the starting sum of money and capture it for use later.
#Ask for the number of years the money will be saved and interest rate and capture them for use later.
#Then your program will calculate the total of money in the account after the number of years entered by the user.
#Your program must display the user name and the statement "after XX years, you will have $XXXXX"

def printname(user_name):
  return (user_name)


name = input("please enter your name ")
printname(name)         #calls the function created earlier and uses name as the parameter

def moneyfunc(money):      #creates the function moneysum
  return (money)          #return saves the value given to money 


startingmoney = int(input("what is the starting value: $"))
moneyfunc(startingmoney)

def timefunc(time, interest):
  return (time, interest)


years = int(input("How many years will it be saved "))
rate = float(input("what is the interest rate in decimal "))
timefunc(years,rate)

#XX = money(1 + rate/times compunded)^TC*years
X = startingmoney * (1 + (rate/1)**years)



print(name + ", after " + str(years) + " years, you will have $" + str(X))