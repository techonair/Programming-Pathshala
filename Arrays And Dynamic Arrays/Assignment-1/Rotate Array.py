# Problem: https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [int(i) for i in input().split()]
        k = int(input())
        n = len(nums)
        tmp = nums[:]

        for i in range(n):
            tmp[(i + k) % n] = int(nums[i])

        nums[:] = tmp[:]

        # This "nums[:]" cannot be written as just "num"
        # The previous one can truly change the value of old nums, 
        # but the following one just changes its reference to a new nums not the value of old nums.