#Program: 	HW07_TVShows.py
#Name: 		Shanielle Hall
#Date: 		May 25, 2025
#Purpose:	Program that processes a text file containing an unsorted list of TV shows and their
#			corresponding number of seasons. The file alternates between a number (representing the
#			number of seasons) and a TV show title.

def getFile(prompt):
    while True: #asks the user for a filename and runs until a valid filename is given
        filename = input(prompt)
        try:
            file = open(filename, "r")
            return file
        except FileNotFoundError:
            print(f"Error: {filename} not found. Try again.")
            
def collectData(inFile):
    data = {} #dictionary that keeps seasonCount and show title
    lines = []
    
    for line in inFile:
        line = line.strip()
        if line != "":
            lines.append(line)
    
    index = 0
    while index < len(lines) - 1:
        try:
            season = int(lines[index])
            title = lines[index + 1]
            
            if season not in data:
                data[season] = []
            
            data[season].append(title)
        except:
            print("Skipping bad data at lines", index, "and", index + 1)
        
        index = index + 2
    
    return data

def saveSortedTitles(dataDictionary):
    #takes all the show titles, sorts them inalphabetical order and writes them to showTitles.txt
    allTitles = []
    for season in dataDictionary:
        titles = dataDictionary[season]
        for title in titles:
            allTitles.append(title)
    
    allTitles.sort()
    
    outFile = open("showTitles.txt", "w")
    for title in allTitles:
        outFile.write(title + "\n")
    outFile.close()

def saveSeasonsData(dataDictionary):
    #saves season data dictionary to seasonsData.txt, sorted
    outFile = open("seasonsData.txt", "w")
    
    keys = list(dataDictionary.keys())
    keys.sort()
    for season in keys:
        line = str(season) + " : "
        titles = dataDictionary[season]
        
        for i in range(len(titles)):
            line = line + titles[i]
            if i < len(titles) - 1:
                line = line + "; "
        outFile.write(line + "\n")
            
    outFile.close()
            
def main():
    inFile = getFile("Enter the name of the data file to open: ")
    data = collectData(inFile)
    inFile.close()
    
    saveSeasonsData(data)
    saveSortedTitles(data)
    
    print("Results have been saved in the output files.")
    
if __name__ == "__main__":
    main()
