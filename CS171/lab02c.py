def countOdds(num1, num2, num3, num4, num5):
    num = num1 % 2
    num += num2 % 2
    num += num3 % 2
    num += num4 % 2
    num += num5 % 2
    
    return num
    

if __name__ == '__main__':
     num1 = int(input())
     num2 = int(input())
     num3 = int(input())
     num4 = int(input())
     num5 = int(input())

     result = countOdds(num1, num2, num3, num4, num5)
     print(f'Total odds: { result }')
