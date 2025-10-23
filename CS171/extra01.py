print("Enter the origin currency name")
originalCurr = input("")
print("Enter the destination currency name")
destinationCurr = input("")
print("Enter the exchange rate from", originalCurr, "to", destinationCurr)
exchangeRate = float(input())
print("Enter the amount in", originalCurr)
amount = float(input())

formattedAmount = "{:.2f}".format(amount)

convertedMoney = amount * exchangeRate
formattedConvertedMoney = "{:.2f}".format(convertedMoney)

print(formattedAmount, originalCurr, "is equivalent to", formattedConvertedMoney, destinationCurr)

