n = "Your name is"
name = input("Please enter your name: ")

print(n, name)

def calTax(money):
    deduc = (money / 100) * 45
    tax = money - deduc
    s = print("Your salary after deductions is")
    
    return s, tax

print(calTax(45000))


