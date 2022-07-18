# link: https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = len(nums)-1
        
        while x > 0 and nums[x] <= nums[x-1]:
            x -= 1
            
        if x-1 >= 0:
            
            y = len(nums)-1
            
            while y >= x:
                
                if nums[y] > nums[x-1]:
                    nums[x-1], nums[y] = nums[y], nums[x-1]
                    break
                
                y -= 1
        
        i = x
        j = len(nums)-1
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1