def letterFrequency(text):
    letterDictionary = {}
    for character in text:
        if character in letterDictionary:
            letterDictionary[character] += 1
        else:
            letterDictionary[character] = 1
    return letterDictionary

def topN(dict, n):
    result = []
    
    def value(item):
        return item[1]
    
    sortedItems = sorted(dict.items(), key = value, reverse = True)
    for i in range(min(n, len(sortedItems))):
        result.append(sortedItems[i][0])
    return result
    
if __name__ == '__main__':
    print(letterFrequency("Hello, CS 171"))
