def paymentCalculator(balance, payment, interest):
    month = 0
    while balance > 0:
        balance += balance * interest
        balance -= payment
        month += 1
        
        if balance <= 0:
            balance = 0
    return month


if __name__ == '__main__':
    balance = float(input(""))
    payment = float(input(""))
    interest = float(input(""))
    
    result = paymentCalculator(balance, payment, interest)
    if result > 1:
        print(result, "payments")
    else:
        print(result, "payment")