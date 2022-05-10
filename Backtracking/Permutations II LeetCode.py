# Link : https://leetcode.com/problems/permutations-ii/

def permutation(i, aux):
        if i == len(nums):
            ans.append(aux.copy())
            return
        freq = [0]*26
        for j in range(i, len(nums)):
            if freq[nums[j] - 1] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                permutation(i+1, aux)
                nums[i], nums[j] = nums[j], nums[i]
            freq[nums[j] - 1] += 1

ans= []
nums = [int(i) for i in input().split(",")]
permutation(0, nums)
print(ans)