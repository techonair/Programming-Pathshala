# Problem: https://leetcode.com/problems/subsets/

nums = [int(i) for i in input().split()]

# iterative approach
"""
for i in range(n):
    for j in range(i, n):
        for k in range(i, j+1):
            print(arr[k], end=" ")
        print('\n', end='')
"""
# For Subset:

ans = []
arr = []
def printSubset(nums, index, arr):
    if index == len(nums):
        ans.append(arr)
        return ans
    printSubset(nums, index+1, arr)
    printSubset(nums, index+1, arr + nums[index:index+1])

printSubset(nums, 0, arr)
print(ans)
# For Subarray
"""
Things we need to track:
1) array so that we can update values
2) starting index at which we are iteratng 0...N-1 
3) end index of iteration
"""
"""
def subarray(nums, start, end):
    # Termination Condition:
    if end == len(nums):
        return

    elif start > end:
        subarray(nums, 0, end+1)

    elif start == -1 and end == -1:
        print(nums[start+1:end+1])
        subarray(nums, start+1, end+1)

    else:
        print(nums[start : end + 1])
        subarray(nums, start+1, end)

subarray(nums, -1, -1)
"""