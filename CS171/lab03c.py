import math

if __name__ == '__main__':
    
    num1 = int(input(""))
    num2 = int(input(""))
    num3 = int(input(""))
    
    if (num1 <= num2 <= num3) or (num3 <= num2 <= num1):
        med = num2
    elif (num2 <= num1 <= num3) or (num3 <= num1 <= num2):
        med = num1
    else:
        med = num3
            
    print(med)