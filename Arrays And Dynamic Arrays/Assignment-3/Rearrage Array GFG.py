# Problem: https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/

# Approach 1) Time and Space Complexity = O(N)
"""arr = [int(i) for i in input().split()]
n = len(arr)
for i in range(n):
    if arr[i] >= 0:
        idx = arr[i]
        val = i
        while idx != i:
            tmp = arr[idx]
            arr[idx] = (-1)*(val + 1)
            val = idx
            idx = tmp
    arr[idx] = (-1)*(val+1)

for i in range(n):
    arr[i] = (-1)*arr[i]-1

print(arr)"""

# Approach 2) Time Complexity O(N), Space Complexity O(1) but it is only valid for N < 10**4
arr = [int(i) for i in input().split()]
n = len(arr)
for i in range(n):
    arr[arr[i]%n] += n*i

for i in range(n):
    arr[i] = int(arr[i]/n)

print(arr)
