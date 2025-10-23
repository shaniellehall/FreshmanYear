#Program HW02_fluids.py
#Name : Shanielle Hall
#Date : April 8, 2025
#Purpose : Write a program that asks the user to input a number of fluid ounces, as an integer.
#          Allocate the fluid ounces into the various units, first starting with barrels, then gallons, and
#          so on, finishing with tablespoons. Then display the results.


def calcFluids(fluid):
    barrel = fluid // 5376
    fluid %= 5376
    
    gallon = fluid // 128
    fluid %= 128
    
    quart = fluid // 32
    fluid %= 32
    
    pint = fluid // 16
    fluid %= 16
    
    cup = fluid // 8
    fluid %= 8
    
    gill = fluid // 4
    fluid %= 4
    
    ounce = fluid // 1
    fluid %= 1
    
    tablespoons = fluid // 0.5
    fluid %= 0.5
    
    fluidRemaining = fluid // 1
    
    print(int(barrel), "barrel(s)")
    print(int(gallon), "gallons(s)")
    print(int(quart), "quart(s)")
    print(int(pint), "pint(s)")
    print(int(cup), "cup(s)")
    print(int(gill), "gill(s)")
    print(int(ounce), "ounce(s)")
    print(int(tablespoons), "tablespoon(s)")

if __name__ == "__main__":
    fluid = int(input("How many fluid ounces do you have? "))
    print(fluid, "fluid ounces can be divided into:")
    calcFluids(fluid)