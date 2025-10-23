#Program HW04_magic.py
#Name : Shanielle Hall
#Date : May 3, 2025
#Purpose : 	Write a program that asks the user what size square they want to create,
#			then lets the user enter numbers to fill in the square then let us know whether or not this
#			is a magic square.

def populateSquare(size):
    square = []
    usedValues = []
    minimumValue = 1
    maximumValue = size * size

    for row in range(size):
        print(f"Row {row + 1}")
        currentRow = []
        for column in range(size):
            valid = False
            while not valid:
                value = input("Enter a value for the square: ")
                if value.isdigit():
                    value = int(value)
                    if value < minimumValue or value > maximumValue:
                        print("Value out of bounds. Please try again.")
                    elif value in usedValues:
                        print("Error: this value already exists in the square. Enter a different value.")
                    else:
                        currentRow.append(value)
                        usedValues.append(value)
                        valid = True
                else:
                    print("Invalid input. Please try again.")
        square.append(currentRow)
    return square


def printSquare(square):
    print("Here is your square:")
    for row in square:
        print(" ".join(str(value) for value in row))


def isMagicSquare(square):
    size = len(square)
    target = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != target:
            return False

    # Check columns
    for columns in range(size):
        columnSum = 0
        for row in range(size):
            columnSum += square[row][columns]
        if columnSum != target:
            return False

    # Check main diagonal
    diagonal1 = 0
    for i in range(size):
        diagonal1 += square[i][i]
    if diagonal1 != target:
        return False

    # Check other diagonal
    diagonal2 = 0
    for i in range(size):
        diagonal2 += square[i][size - 1 - i]
    if diagonal2 != target:
        return False

    return True


def main():
    print("Welcome to the Magic Square Game")

    validSize = False
    while not validSize:
        sizeInput = input("Enter the size of your square (between 3 and 9): ")
        if sizeInput.isdigit():
            size = int(sizeInput)
            if size < 3 or size > 9:
                print("Value out of bounds. Please try again.")
            else:
                validSize = True
        else:
            print("Invalid input. Please try again.")

    square = populateSquare(size)
    printSquare(square)

    if isMagicSquare(square):
        print("This is a magic square!!")
    else:
        print("This is not a magic square.")

if __name__ == "__main__":
    main()