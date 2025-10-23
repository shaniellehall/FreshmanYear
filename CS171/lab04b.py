def inOrder(string):
    i = 0 #index of the string
    while i < len(string) - 1:
        if string[i] > string[i + 1]:
            return False
        i += 1
    return True

if __name__ == '__main__':
    if inOrder:
        print("In ascending order")
    else:
        print("Not in order")