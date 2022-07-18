arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#arr = [4, 1, 3, 9, 7]
n = len(arr)

for i in range(1, n):
    if arr[i] < arr[i-1]:
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

print(arr)