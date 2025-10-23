def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesList = apples
    orangesList = oranges
    applesCounter = 0
    orangesCounter = 0
    
    
    for i in range(0, len(applesList)):
        applesDistance = a + applesList[i]
        if applesDistance >= s:
            if applesDistance <= t:
                applesCounter += 1
                
                
    for i in range(0, len(orangesList)):
        orangesDistance = b + orangesList[i]
        if orangesDistance >= s:
            if orangesDistance <= t:
                orangesCounter += 1
    final = [applesCounter, orangesCounter]
    return final


