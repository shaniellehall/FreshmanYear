import math
def slicesPerPizza(diameter):
    radius = diameter / 2
    sliceArea = 14.125
    pizzaArea = math.pi * (radius ** 2)

    numSlice = pizzaArea / sliceArea
    return int(numSlice)

if __name__ == "__main__":
    print("Welcome to Mario and Luigi's Pizzeria\n")
    dia = int(input("Enter the diameter of the pizzas you want to order (in inches): "))
    people = int(input("Enter the number of people in your party: "))
    pizza = (people * 3)/slicesPerPizza(dia)
    print("For a party of", people, "people you need to order", math.ceil(pizza), "pizza(s).")
    print("A", dia, "inch pizza will yield", slicesPerPizza(dia), "slices.")
    