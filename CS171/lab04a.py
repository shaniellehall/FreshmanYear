def rotateChar(character):
    result = ""
    for char in character:
        if character.islower():
            result += chr(((ord(char) - ord("a") + 13) % 26) + ord("a"))
        elif character.isupper():
            result += chr(((ord(char) - ord("A") + 13) % 26) + ord("A"))
        else:
            result += char
    return result
    
def rotateString(string):
    letter = ""
    for char in string:
        letter += rotateChar(char)
    return letter
    

