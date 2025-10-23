import math
size = float(input("Enter size:\n"))
cArea = (math.pi * (size / 2) ** 2 )
tArea = (math.sqrt(3)/4) * (size) ** 2
sArea = float(size ** 2)


print("A circle of diameter", size, "has an area of", cArea)
print("An equilateral triangle of size", size, "has an area of", tArea)
print("A square of size", size, "has an area of", sArea)