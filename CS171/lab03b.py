def calculateIncomeTax(taxableIncome):
    #Assigns all income brackets to a variable
    bracketLimit1 = 11600
    bracketLimit2 = 47150
    bracketLimit3 = 100525
    bracketLimit4 = 191950
    bracketLimit5 = 243725
    bracketLimit6 = 609350
    
    #Assigns all income bracket percentages to a variable
    limitPercentage1 = 0.10
    limitPercentage2 = 0.12
    limitPercentage3 = 0.22
    limitPercentage4 = 0.24
    limitPercentage5 = 0.32
    limitPercentage6 = 0.35
    limitPercentage7 = 0.37
    
    
    if taxableIncome <= bracketLimit1:
        tax = taxableIncome * limitPercentage1
    elif taxableIncome <= bracketLimit2: 
        tax = (bracketLimit1 * limitPercentage1) + ((taxableIncome - bracketLimit1) * limitPercentage2)
    elif taxableIncome <= bracketLimit3: 
        tax = (bracketLimit1 * limitPercentage1) + ((bracketLimit2 - bracketLimit1) * limitPercentage2) + ((taxableIncome - bracketLimit2) * limitPercentage3)
    elif taxableIncome <= bracketLimit4: 
        tax = (bracketLimit1 * limitPercentage1) + ((bracketLimit2 - bracketLimit1) * limitPercentage2) + ((bracketLimit3 - bracketLimit2) * limitPercentage3) + ((taxableIncome - bracketLimit3) * limitPercentage4)
    elif taxableIncome <= bracketLimit5: 
        tax = (bracketLimit1 * limitPercentage1) + ((bracketLimit2 - bracketLimit1) * limitPercentage2) + ((bracketLimit3 - bracketLimit2) * limitPercentage3) + ((bracketLimit4 - bracketLimit3) * limitPercentage4) +((taxableIncome - bracketLimit4) * limitPercentage5)
    elif taxableIncome <= bracketLimit6: 
        tax = (bracketLimit1 * limitPercentage1) + ((bracketLimit2 - bracketLimit1) * limitPercentage2) + ((bracketLimit3 - bracketLimit2) * limitPercentage3) + ((bracketLimit4 - bracketLimit3) * limitPercentage4) + ((bracketLimit5 - bracketLimit4) * limitPercentage5) +((taxableIncome - bracketLimit5) * limitPercentage6)
    else: 
        tax = (bracketLimit1 * limitPercentage1) + ((bracketLimit2 - bracketLimit1) * limitPercentage2) + ((bracketLimit3 - bracketLimit2) * limitPercentage3) + ((bracketLimit4 - bracketLimit3) * limitPercentage4) + ((bracketLimit5 - bracketLimit4) * limitPercentage5) + ((bracketLimit6 - bracketLimit5) * limitPercentage6) +((taxableIncome - bracketLimit6) * limitPercentage7)
    return round(tax)
    
if __name__ == '__main__':
    taxableIncome = (int(input("Please enter your income: ")))
    result = calculateIncomeTax(taxableIncome)
    print(result)