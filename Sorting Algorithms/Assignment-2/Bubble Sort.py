arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#arr = [4, 1, 3, 9, 7]
n = len(arr)

# Method 2: (Optimized Bubble Sort) Based on Sliding window of size 2

flag = False
while not flag:

    flag = True
    i = 0

    while (i < n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = False
        i += 1

print(arr)

# Method 1: Pure Bubble Sort
"""
def check(arr):
    for i in range(1, n-1):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        k = i
        while k < n-1 and arr[k] > arr[k+1]:
            arr[k], arr[k+1] = arr[k+1], arr[k]
            k += 1
    flag = False
    while not flag:
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                check(arr)
                break
            else:
                flag = True
        
check(arr)

print(arr)
"""

 