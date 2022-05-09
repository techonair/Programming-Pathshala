# Problem: https://leetcode.com/problems/subsets/

nums = [int(i) for i in input().split()]
n = len(nums)
ans = []
arr= []

def bitmaskGenerator(b):

    for i in range(b):
        b << 1

for i in range(0, 2**n):
    bits = bitmaskGenerator(i)
    for j in range(len(bits)):
        if bits[j]:
            arr.append(nums[j])
    ans.append(arr)
    arr.clear()

print(ans)