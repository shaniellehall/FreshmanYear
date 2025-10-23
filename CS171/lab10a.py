def verboseBubbleSort(nums):
    n = len(nums)
    total_swaps = 0
    number = 1
    
    print(f"Original List: {nums}")
    
    while True:
        swaps = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps += 1
        total_swaps += swaps
        print(f"After Pass {number}: {nums} ({swaps} swaps)")
        number += 1
        if swaps == 0:
            break
        if number > n - 1:
            break
    return total_swaps

if __name__ == "__main__":
    print("Enter integers, separated by spaces")
    entry = input().split()
    nums = []
    for t in entry:
        nums.append(int(t))
    swaps = verboseBubbleSort(nums)