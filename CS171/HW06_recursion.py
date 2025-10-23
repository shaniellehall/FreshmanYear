#Program HW04_Text_Assistant.py
#Name : Shanielle Hall
#Date : May 17, 2025
#Purpose : Practicing designing and implementing recursive functions. 

def flattenList(myList):
    flattened_list = []
    for item in myList: #checks every item in the list
        if isinstance(item, list): #if the item is in the list
            flattened_list.extend(flattenList(item))
        else:
            flattened_list.append(item)
    return flattened_list

def longestCommonPrefix(strings):
    if not strings:
        return ""
    prefix = ""
    i = 0
    while True: #check if index is in bounds for the string
        if i >= len(strings[0]):
                return prefix
        current_character = strings[0][i]
        for s in strings:
            if i >= len(s) or s[i] != current_character:
                return prefix
        prefix += current_character
        i += 1

def hailstoneSequence(number):
    hail = [number] #initial number
    while number != 1: #check to see that number is not 1
        if number % 2 == 0: #checks to see if the number is even
            number = number // 2
        else: #checks to see if the number is od
            number = (number * 3) + 1
        hail.append(number) #adds the current number to the list
    return hail #returns the list with the sequence of numbers