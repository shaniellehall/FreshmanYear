seconds = int(input(""))
minutes = int(input(""))
hours = int(input(""))

time = seconds + (minutes * 60) + (hours * 60 * 60)
print(time, "seconds")