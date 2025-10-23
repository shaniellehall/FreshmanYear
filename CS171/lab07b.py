def decimalToBinary(number):
    string = ""
    if number == 0:
        return 0
    while number > 0:
        remainder = number % 2
        string = str(remainder) + string
        number = number // 2
    return string
if __name__ == "__main__":
    print(decimalToBinary(8))
    print(decimalToBinary(2))
    print(decimalToBinary(25))