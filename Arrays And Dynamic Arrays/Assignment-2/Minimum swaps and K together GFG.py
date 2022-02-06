# Problem : https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1

arr = [int(i) for i in input().split()]
k = int(input())
n = len(arr)

k_count = 0

# size of window
for i in range(n):
    if arr[i] <= k:
        k_count += 1

swap = 0
count = 0
for j in range(k_count):
    if arr[j]<=k:
        count += 1
    swap = max(swap, count)

for j in range(1, n-k_count+1):
    if arr[j-1]<=k:
        count -= 1
    if arr[j+k_count-1]<=k:
        count += 1
    swap = max(swap, count)   

print(k_count-swap)
