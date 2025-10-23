#Program HW04_Text_Assistant.py
#Name : Shanielle Hall
#Date : April 26, 2025
#Purpose : Write a group of functions that will allow the user to analyze and edit text.


def displayMenu():
    print("What would you like to do?")
    print("C - Number of non-whitespace characters")
    print("W - Number of words")
    print("F - Fix capitalization")
    print("S - Shorten spaces")
    print("Q - Quit")

def countNonWhiteChars(string):
    count = 0
    space = " "
    index = 0

    while index < len(string):
        char = string[index]
        if char != space and char != '\n' and char != '\t':
            count += 1
        index += 1    
    print("Number of non-whitespace characters:", count)

def countWords(string):
    words = string.split()
    count = len(words)
    print("Number of words:", count)

def fixCapitalization(string):
    index = 0
    result = ""
    capitalize = True
    count = 0

    while index < len(string):
        char = string[index]

        if capitalize and char >= 'a' and char <= 'z':
            upperCharacter = chr(ord(char) - 32)
            result = result + upperCharacter
            count = count + 1
            capitalize = False
        else:
            result = result + char

        if char == '.' or char == '?' or char == '!':
            capitalize = True
        elif char != ' ' and char != '\n' and char != '\t':
            capitalize = False

        index = index + 1

    print("Number of letters capitalized:", count)
    return result

def shortenSpace(string):
    index = 0
    result = ""
    space = False

    while index < len(string):
        char = string[index]
        if char == ' ':
            if not space:
                result = result + char
                space = True
        else:
            result = result + char
            space = False
        index = index + 1
    return result

if __name__ == '__main__':
    print("Welcome to CS 171 Text Assistant")
    print("Enter your text:")
    string = input("")
    
    option = ""
    while option != "q":
        displayMenu()
        option = input("Choose an option: ")
        option = option.lower()
        if option == "c":
            countNonWhiteChars(string)
        elif option == "w":
            countWords(string)
        elif option == "f":
            string = fixCapitalization(string)  
            print("Edited text:\n" + string)
        elif option == "s":
            string = shortenSpace(string)  
            print("Edited text:\n" + string)
        elif option == "q":
            print("Goodbye!")
        else:
            print("Invalid choice. Try again.")