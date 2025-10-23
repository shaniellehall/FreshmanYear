def largestValueBelowThreshold(values, threshold):
    largestNumber = None
    
    for number in values:
        if number < threshold:
            if largestNumber is None or number > largestNumber:
                largestNumber = number
    return largestNumber


if __name__ == "__main__":
    threshold = int(input("Enter threshold value: "))
    inputValues = int(input("How many values in the list? "))
    
    values = []
    
    for i in range (inputValues):
        j = int(input(f"Enter value {i + 1}: "))
        values.append(j)
        
    result = largestValueBelowThreshold(values, threshold)
    
    if result is None:
        print(f"The largest value in the list {values} less than 50 is {result}.")
    else:
        print(f"The largest value in the list {values} less than {threshold} is {result}.")