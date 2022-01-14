# Problem: https://leetcode.com/problems/max-chunks-to-make-sorted/

arr = [int(i) for i in input().split()]

count_max = -10**9

count = 0

for i in range(len(arr)):
    count_max = max(count_max, arr[i])
    if count_max == i:
        count += 1

print(count)