def doubleLetterWords(words):
    list = []
    for word in words:
        lowerWord = word.lower()
        doubleLetterFound = False
        for i in range(len(word)-1):
            if lowerWord[i] == lowerWord[i + 1]:
                doubleLetterFound = True
        if doubleLetterFound and word not in list:
            list.append(word)
    return list

def getWordsFromPhrase():
    phrase = input("Enter phrase: ")
    words = phrase.split()
    return words

def main():
    words = getWordsFromPhrase()
    doubleLetterWordsList = doubleLetterWords(words)
    if doubleLetterWordsList:
        print("Double Letter Words:")
        for word in doubleLetterWordsList:
            print(word)
    else:
        print("No double letter words found.")

if __name__ == "__main__":
    main()