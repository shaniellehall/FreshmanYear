#Program hw_01.py
#Name : Shanielle Hall
#Date : 4/1/2025
#Purpose : Write a program to compute Gross Pay and Net Pay

print("Welcome to Gross and Net Pay Estimator.")

print("Enter Hourly Wage in dollars (float): ")
hourlyPay = float(input(""))
print("Enter Hours Per Week (integer): ")
hoursWorked = float(input(""))
print("Enter Weeks Per Year Worked (integer): ")
weeksWorked = float(input(""))
print("")

#Calculates the gross pay for the week and year
grossPay = (hourlyPay * hoursWorked)
grossYearlyPay = grossPay * weeksWorked

print("Gross Pay Information")
print("You will make ${:,.2f}". format(grossPay), "per week.")
print("You will make ${:,.2f}". format(grossYearlyPay), "per year.")
print("")

#Calculates all taxes
socialSecurityTaxes = grossYearlyPay * 0.06
payLeft = grossYearlyPay - socialSecurityTaxes

medicareTaxes = payLeft * 0.02
payLeft = payLeft - medicareTaxes

irsWageTax = payLeft * 0.12
payLeft = payLeft - irsWageTax

paStateTax = payLeft * 0.0307
payLeft = payLeft - paStateTax

philadelphiaTax = payLeft * 0.0375
payLeft = payLeft - philadelphiaTax

healthInsuranceTax = 396 * 12

#Calculates the net pay (pay after deductions)
totalDeductions = socialSecurityTaxes + medicareTaxes + irsWageTax + paStateTax + philadelphiaTax + healthInsuranceTax
print("Taxes and Deductions")
print("You will pay ${:,.2f}". format(socialSecurityTaxes), "in Social Security Taxes.")
print("You will pay ${:,.2f}". format(medicareTaxes) , "in Medicare Taxes.")
print("You will pay ${:,.2f}".  format(irsWageTax), "in IRS Taxes.")
print("You will pay ${:,.2f}". format(paStateTax) , "in PA State Taxes.")
print("You will pay ${:,.2f}". format(philadelphiaTax) , "in Phila Taxes.")
print("You will pay ${:,.2f}". format(healthInsuranceTax) , "for health insurance.")
print("")

#Calculates Take home pay, the hourly and
#weekly take home pay,
#and the percentage that you take home each year.
takeHomePay = grossYearlyPay - totalDeductions
hourlyTakeHome = (takeHomePay / weeksWorked)/ hoursWorked
weeklyTakeHome = (takeHomePay / weeksWorked)
percentage = (takeHomePay / grossYearlyPay) * 100
percentage = round(percentage,2)

print("Net Pay Information")
print("Your take home pay will be ${:,.2f}". format(takeHomePay), "per year.")
print("This is an hourly take home pay of ${:,.2f}". format(hourlyTakeHome), ".")
print("This is a weekly take home pay of ${:,.2f}". format(weeklyTakeHome), ".")
print("Your Net Pay is" ,percentage, "percent of your Gross Pay.")