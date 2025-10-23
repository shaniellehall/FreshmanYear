def colorDistance(color1, color2):
    return ((color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)**0.5

def sortByColorDistance(otherColors, thisColor):
    distances = []
    for color in otherColors:
        distances.append(colorDistance(color, thisColor))
    n = len(otherColors)
    for i in range(n):
        for j in range(0, n - i - 1):
            if distances[j] > distances[j + 1]:
                distances[j], distances[j + 1] = distances[j + 1], distances[j]
                otherColors[j], otherColors[j + 1] = otherColors[j + 1], otherColors[j]

if __name__ == "__main__":
    chartreuse = [127, 255, 0]
    colors = [[255, 0, 0], [0, 0, 127], [128, 0, 128]]
    
    print("Orignal Colors:", colors)
    
    sortByColorDistance(colors, chartreuse)
    print("Sorted Colors by Distance to Chartreuse:" , colors)
    print(colorDistance([120, 60, 30], [30, 60, 90]))