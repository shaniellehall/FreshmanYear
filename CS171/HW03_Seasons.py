#Program HW03_Seasons.py
#Name : Shanielle Hall
#Date : April 19, 2025
#Purpose : Write a Python program that takes a Gregorian date and tells the
#		   user what Celtic Season it falls in.

def monthToNumber(abbreviation):
    month = abbreviation.lower() #converts input to lowercase
    if month == "jan" or month == "feb" or month == "mar" or month == "apr" or month == "may" or month == "jun" or month == "jul" or month == "aug" or month == "sep" or month == "oct" or month == "nov" or month == "dec":
        return True #check if abbreviation matches any of the months
    else:
        print("Invalid Month\nGood-bye!")
        return False

def isValidDate(month, day):
    month = month.lower() #converts input to lowercase
    #months with 31 days
    if month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec":
        if day >= 1 and day <= 31:
            return True
    #months with 30 days
    elif month == "apr" or month == "jun" or month == "sep" or month == "nov":
        if day >= 1 and day <= 30:
            return True
    elif month == "feb":
        if day >= 1 and day <= 29:
            return True
    print("Invalid Day\nGood-bye!")
    return False

def getCelticSeason(month, day): #determines the Celtic season
    lower = month.lower()
    if (lower == "jan" and day == 31) or (lower == "feb") or (lower == "mar" and day <= 20):
        season = "Imbolc"
    elif (lower == "mar" and day >= 21) or (lower == "apr") or (lower == "may" and day <= 1):
        season = "Ostara"
    elif (lower == "may" and day >= 2) or (lower == "jun" and day <= 20):
        season = "Beltane"
    elif (lower == "jun" and day >= 21) or (lower == "jul") or (lower == "aug" and day <= 1):
        season = "Litha"
    elif (lower == "aug" and day >= 2) or (lower == "sep" and day <= 22):
        season = "Lughnasadh"
    elif (lower == "sep" and day >= 23) or (lower == "oct") or (lower == "nov") or (lower == "dec") or (lower == "jan" and day <= 30):
        season = "Samhain"
    print("The Celtic Season is", season)

def main():
    print("Welcome to the Celtic Season converter.")
    month = input("Enter the Month (3-letter abbreviation): ")
    if not monthToNumber(month):
        return
    day_input = input("Enter Day of the Month (1 - 31): ")
    if day_input >= "0" and day_input <= "9" or day_input >= "10" and day_input <= "31":
        day = int(day_input)
    else:
        print("Invalid Day\nGood-bye!")
        return
    if not isValidDate(month, day):
        return
    getCelticSeason(month, day)

if __name__ == "__main__":
    main()
