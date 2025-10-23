def playGame(host):
    low = host.getMinValue()
    high = host.getMaxValue()
    
    while low <= high:
        middle = (low + high) // 2
        result = host.guess(middle)
        
        if result == "Correct":
            return middle
        elif result == "Higher":
            low = middle + 1
        elif result == "Lower":
            high = middle - 1
        elif result == "Out of Guesses":
            return -1