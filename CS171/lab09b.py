def stringScore(string):
    score = list(string)
    strSum = 0 
    for char in score:
        strSum += ord(char)
    return strSum

def stringHighScore(string, token = " "):
    text = list(string.split(token))
    highScore = -1
    
    hishCorePart = ""
    
    for part in text:
        score = stringScore(part)
        print(f"The value of '{part}' is {score}.")
        if score > highScore:
            highScore = score
            highScorePart = part
    return highScorePart

def main():
    string = input("Enter text: ")
    result = stringScore(string)
    print(f"The sum of these is '{result}' ")
    
    string = input("Enter text: ")
    token = input("Enter token: ")
    if token == "":
        token = " "
    result = stringHighScore(string, token)
    
if __name__ == "__main__":
    main()