# Problem: https://leetcode.com/problems/rotate-array/

nums = [int(i) for i in input().split()]
k = int(input())
n = len(nums)
tmp = nums[:]

for i in range(n):
    tmp[(i + k) % n] = nums[i]

nums = tmp[:]

print(nums)