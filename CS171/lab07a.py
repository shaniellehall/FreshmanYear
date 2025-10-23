def fibonacci(num):
    if num < 0:
        return -1
    elif num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = fibonacci(num - 1) + fibonacci(num -2)
    return result
    
if __name__ == '__main__':
    n = 7
    print(f"fibonacci({n}) is {fibonacci(n)}")
