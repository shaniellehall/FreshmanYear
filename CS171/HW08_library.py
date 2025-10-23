#Program: 	HW08_library.py
#Name: 		Shanielle Hall
#Date: 		June 1, 2025
#Purpose:	The purpose of this homework assignment is to practice algorithm thinking,
#			incremental development, and writing functions.
def countCheckouts(checkouts, bookID):
    i = bookID
    count = 0
    
    for item in checkouts:
        if item == i:
            count += 1
    return count

def mostCheckedOut(checkouts):
    result = []
    
    if len(checkouts) == 0:
        return result
    
    count = {}
    for bookID in checkouts:
        if bookID in count:
            count[bookID] += 1
        else:
            count[bookID] = 1
    maxCount = max(count.values())
    result = [bookID for bookID in count if count[bookID] == maxCount]
    
    return result

def findPopularBooks(checkouts, minimum = 3):
    count = {}
    for bookID in checkouts:
        if bookID in count:
            count[bookID] += 1
        else:
            count[bookID] = 1
    result = [bookID for bookID in count if count[bookID] >= minimum]
    return result

def checkoutRatio(checkouts, bookID):
    total = len(checkouts)
    count = 0
    if total == 0:
        return 0.0
    
    
    for book in checkouts:
        if book == bookID:
            count += 1
    ratio = (count / total) * 100
    return ratio
    
def getUniqueBooks(checkouts):
    seen = []
    for book in checkouts:
        if book not in seen:
            seen.append(book)
    return seen

def topNBooks(checkouts, n=3):
    result = []
    if len(checkouts) == 0 or n <= 0:
        return result
    
    counts = {}
    for book in checkouts:
        if book in counts:
            counts[book] += 1
        else:
            counts[book] = 1

    bookCounts = []
    for book in counts:
        bookCounts.append([book, counts[book]])

    for i in range(len(bookCounts)):
        for j in range(i + 1, len(bookCounts)):
            if bookCounts[j][1] > bookCounts[i][1]:
                bookCounts[i], bookCounts[j] = bookCounts[j], bookCounts[i]

    result = []
    if len(bookCounts) == 0:
        return result

    countSoFar = 0
    cutoff = 0
    for i in range(len(bookCounts)):
        result.append(bookCounts[i][0])
        countSoFar += 1
        if countSoFar == n:
            cutoff = bookCounts[i][1]
            break

    for j in range(i + 1, len(bookCounts)):
        if bookCounts[j][1] == cutoff:
            result.append(bookCounts[j][0])
        else:
            break

    return result 

def generateReport(checkouts):
    counts = {}
    for book in checkouts:
        if book in counts:
            counts[book] += 1
        else:
            counts[book] = 1

    totalBooks = len(checkouts)
    uniqueBooks = len(counts)

    print("Checkout Report")
    print("A total of", uniqueBooks, "unique books were checked out:")

    for book in counts:
        count = counts[book]
        ratio = (count / totalBooks) * 100
        print("Book", book, ":", count, "checkouts. Checkout ratio: {:.2f}%".format(ratio))


    
checkouts = [105, 102, 202, 103, 101, 102, 210, 101, 105, 104, 110, 105, 101, 105,
            106, 102, 205, 101, 109, 215, 105, 201, 102, 103, 107, 109, 107, 105,
            101, 107, 103, 106, 104, 107, 101]

print("*** Library Checkout System ***")
print("Total checkouts:", len(checkouts))

print("Most checked out books:")
for book in mostCheckedOut(checkouts):
    print("Book", book)

print("Popular books (at least 4 checkouts):")
for book in findPopularBooks(checkouts, 4):
    print("Book", book)

print("Top 3 books:")
for book in topNBooks(checkouts, 3):
    print("Book", book)

print("Checkout Report")
print(generateReport(checkouts))

'''
Test Cases
print(countCheckouts ([101, 102, 101, 103], 101)) # should return 2
print(countCheckouts([201, 202], 203)) # should return 0
print(countCheckouts([], 203)) # should return 0
print(countCheckouts ([104, 102, 101, 103, 102, 101, 101], 104)) #should return 1
print(countCheckouts ([104, 102, 101, 103, 102, 101, 101], 101)) #should return 3
print(countCheckouts ([205, 202, 203, 205, 205, 205, 202], 205))

print(mostCheckedOut([101, 102, 101, 103, 102, 101])) # should return [101]
print(mostCheckedOut([210, 201, 103, 102, 103, 107])) # should return [103]
print(mostCheckedOut([])) # should return None
print(mostCheckedOut([101, 102, 103, 102, 101])) # should return [101, 102]
print(mostCheckedOut([105, 102, 107])) # should return [105, 102, 107]

print(findPopularBooks([101, 101, 101, 102, 103, 103, 103]))
print(findPopularBooks([101, 101, 101, 102, 103, 103, 103], 2))
print(findPopularBooks([101, 101, 101, 102, 103, 103, 103], 5))
print(findPopularBooks([], 5))
print(findPopularBooks([101, 101, 101, 102, 103, 103, 103], 3))

print(checkoutRatio([101, 102, 101, 103], 101))
print(checkoutRatio([101, 102, 101, 103], 110))
print(checkoutRatio([], 101))
print(checkoutRatio([101, 102, 101, 103, 205], 205))
print(checkoutRatio([101, 102, 101, 103, 205, 205], 205))

print(getUniqueBooks([104, 102, 101, 103, 102, 101, 101]))
print(getUniqueBooks([104, 104, 104, 107, 108, 107, 105]))
print(getUniqueBooks([202, 202, 202, 110, 110, 202, 110, 110, 202, 202]))
print(getUniqueBooks([])
)

print(topNBooks([101, 102, 101, 103, 101, 102, 104, 105, 104, 105, 105], 2))
print(topNBooks([101, 102, 101, 103, 101, 102, 104, 105, 104, 105, 105]))
print(topNBooks([101, 102, 101, 103, 101, 102, 104, 105, 104, 105, 105], 5))
print(topNBooks([], 10))
print(topNBooks([]))

print(generateReport([103, 101, 102, 101, 101, 102]))
print(generateReport([]))
'''