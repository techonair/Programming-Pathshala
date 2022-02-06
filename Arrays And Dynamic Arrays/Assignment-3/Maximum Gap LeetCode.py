# Problem: https://leetcode.com/problems/maximum-gap/

nums = [int(i) for i in input().split()]
n = len(nums)

INT_MIN = -10**9
INT_MAX = 10**9

def maxGap(array):
    maximum = INT_MIN
    minimum =  INT_MAX
    for i in range(n):
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])
    
    if maximum == minimum:
        return 0

    gap = int((maximum-minimum)/(n-1))
    if (maximum-minimum)%(n-1) != 0:
        gap = int((maximum-minimum)/(n-1)) + 1

    minArr = [INT_MAX]*n
    maxArr = [INT_MIN]*n

    for i in range(n):
        bkt = int((nums[i] - minimum)/gap)
        minArr[bkt] = min(minArr[bkt], nums[i])
        maxArr[bkt] = max(maxArr[bkt], nums[i])

    ans = INT_MIN
    prev = INT_MIN

    for i in range(n):
        if minArr[i] == INT_MAX:
            continue
        if prev == INT_MIN:
            prev = maxArr[i]
        else:
            ans = max(ans, minArr[i]-prev)
            prev = maxArr[i]
        
    return ans

if n > 2:
    answer = maxGap(nums)
    print(answer)
elif n == 2:
    print(abs(nums[i]-nums[i+1]))
else:
    print(0)

# Above code's Time Complexity is O(3n) ~ O(n)
#_______________________________________________________________________________
# Below code takes less time in LeetCode although Time Complexity is O(nlogn)
"""
nums.sort()
        
        if len(nums) == 2:
            return nums[1] - nums[0]
        elif len(nums) == 1 or nums == []:
            return 0
        
        max_diff = 0
        for index in range(len(nums)-1):
            if nums[index+1] - nums[index] > max_diff:
                max_diff = nums[index+1] - nums[index]
        return max_diff

"""