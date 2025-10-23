def museumParkingPrice(entryDay, entryHour, entryMinute, exitHour, exitMinute, visitType):
    hourlyRate = 2
    maxRate = 55

    def calcTotalMinutes(entryHour, entryMinute, exitHour, exitMinute):
        start = entryHour * 60 + entryMinute
        end = exitHour * 60 + exitMinute
        if end < start:
            end += 24 * 60
        return end - start

    totalMinutes = calcTotalMinutes(entryHour, entryMinute, exitHour, exitMinute)
    if totalMinutes == 0:
        return 0

    totalHours = (totalMinutes + 59) // 60

    if visitType == "Member" and totalHours <= 1:
        return 0

    if entryDay == "Friday":
        if (entryHour > 17 or (entryHour == 17 and entryMinute == 0)):
            if visitType == "Visitor" or visitType == "Member":
                fridayMinutes = calcTotalMinutes(entryHour, entryMinute, 24, 0)
                if totalMinutes <= fridayMinutes:
                    return 10
                else:
                    saturdayMinutes = totalMinutes - fridayMinutes
                    saturdayHours = (saturdayMinutes + 59) // 60
                    saturdayCost = saturdayHours * hourlyRate
                    if saturdayCost > (maxRate - 10):
                        return maxRate
                    return 10 + saturdayCost

    if visitType == "Public":
        if totalHours <= 4:
            return 39
        extraHours = totalHours - 4
        cost = 39 + extraHours * hourlyRate
        if cost > maxRate:
            return maxRate
        return cost

    if visitType == "Visitor":
        if totalHours <= 4:
            return 20
        extraHours = totalHours - 4
        cost = 20 + extraHours * hourlyRate
        if cost > maxRate:
            return maxRate
        return cost

    if visitType == "Member":
        if totalHours <= 4:
            return 15
        extraHours = totalHours - 4
        cost = 15 + extraHours * hourlyRate
        if cost > maxRate:
            return maxRate
        return cost

    return 0


print(museumParkingPrice("Tuesday", 10, 15, 13, 45, "Visitor")) #20
print(museumParkingPrice("Wednesday", 9, 45, 13, 46, "Member")) #17
print(museumParkingPrice("Sunday", 13, 45, 10, 15, "Public")) #55
print(museumParkingPrice("Friday", 18, 18, 19, 7, "Member")) #0
print(museumParkingPrice("Friday", 18, 18, 7, 9, "Visitor")) #26

print(museumParkingPrice('Friday', 18, 18, 19, 7, 'Member')) #0
print(museumParkingPrice('Friday', 20, 40, 22, 42, 'Member')) #10
print(museumParkingPrice('Friday', 23, 41, 23, 5, 'Member')) #58