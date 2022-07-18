# Trouble Sort sorts even and odd indices seprately
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#arr = [4, 1, 3, 9, 7]
n = len(arr)

flag = False
while not flag:

    flag = True
    i = 0

    while (i < n-2):
        if arr[i] > arr[i+2]:
            arr[i], arr[i+2] = arr[i+2], arr[i]
            flag = False
        i += 1

print(arr) # Output: [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# better use two arrays of even and odd elements in them
# apply merge sort
# recombine the two array