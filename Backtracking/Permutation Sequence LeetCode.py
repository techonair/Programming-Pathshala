# Link: https://leetcode.com/problems/permutation-sequence/

def permutation(i, aux, n):
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
print(num)