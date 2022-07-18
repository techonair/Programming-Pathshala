# link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: 
        
        n = len(nums)-1
        
        def left(nums):
            
            low = 0
            high = n
            
            while low <= high:
                
                m = (low + high)//2
                
                if nums[m] < target:
                    low = m + 1
                    
                elif nums[m] > target:
                    high = m -1
                    
                elif nums[m] == target:
                    if m == 0 or nums[m-1] != target:
                        return m
                    high = m- 1
            return -1
        
        def right(nums):
            
            low = 0
            high = n
            
            while low <= high:
                m = (low + high)//2
                
                if nums[m] < target:
                    low = m + 1
                    
                elif nums[m] > target:
                    high = m - 1
                    
                elif nums[m] == target:
                    if m == n or nums[m+1] != target:
                        return m
                    low = m + 1
            return -1
                
                
        start = left(nums)
        end = right(nums)
        
        return [start, end]