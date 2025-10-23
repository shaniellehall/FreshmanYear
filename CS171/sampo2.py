#Program: 	TemperatureConverter.py
#Purpose: 	Given a temperature in Farenheit, calculate the corresponding
#			temperature in Celcius and Kelvin Degrees
#Author:	Shanielle Hall
#Date: 		April 1, 2025

#Tell the user what the program does
print("Temperature Converter")

#get the temperature in Farenheit from the user
tempF = float(input("Enter the original temperature in Farenheit: "))

#Convert the temperature to celcius
tempC = (tempF - 32) * 5 / 9

#Convert temperature to Kelvin
tempK = tempC + 273.15

#Display the results
print("Original temperature in F:",tempF)
print("Temperature in C:",tempC)
print("Temperature in K:",tempK)
