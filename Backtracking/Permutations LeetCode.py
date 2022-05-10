# Link: https://leetcode.com/problems/permutations/

def swap(i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return 0

def permutation(i, aux):
    if i == n:
        print(aux)
        ans.append(aux[:])
        return
    for j in range(i, n):
        swap(i, j)
        permutation(i+1, aux)
        swap(i, j)

ans= []
i = 0
nums = [int(i) for i in input().split(",")]
n = len(nums)
permutation(i, nums)
print(ans)

"""
def permutation(i, aux):
        if i == len(nums):
            ans.append(aux[:])
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            permutation(i+1, aux)
            nums[i], nums[j] = nums[j], nums[i]

ans= []
nums = [int(i) for i in input().split(",")]
permutation(0, nums)
return ans
"""