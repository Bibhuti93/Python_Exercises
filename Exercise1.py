#Question: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

#Starting python version 3 raw_input has been renamed to input
name = input("Please enter your name\n")
age = int(input("Please enter your age\n"))
print_freq = int(input("How many times you want to print this message ?\n"))

for i in range(0,print_freq):
	print ("""Hello """,name,""" !
	Your age is: """,age)

	#Get current year
	now = datetime.datetime.now()
	year_when_age_100 = (100 - age) + now.year

	print ("You will be of 100 years in: ",year_when_age_100)
