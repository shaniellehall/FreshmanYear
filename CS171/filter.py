def filter(filename):
    database = {}
    try:
        file = open(filename, "r")
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        return database
    
    for line in data:
        line = line.strip()
        if isnumeric(line):
            file.write(line + "\n")
        else:
            file.write(line + "\n")
            
            
if __name__=="__main__":
    filenames = ["small.txt","large.txt"]
    
    outfile1 = "numbers.txt"
    file = open(outfile1,"w")
    
    outfile2 = "other.txt"
    file = open(outfile2,"w")