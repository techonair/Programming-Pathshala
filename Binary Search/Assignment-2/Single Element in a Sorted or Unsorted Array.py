
# link: https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        # if starting index of repeating element pair is even then answer is in right
        # else if starting index is odd then the element is in the left 
        
        low = 0
        high = n-1
        
        while low <= high:
            
            m = (low + high)//2
            
            if m == 0:
                if nums[m+1] != nums[m]:
                    return nums[m]
                else:
                    low = m+1
                    
            elif m == n-1:
                if nums[m-1] != nums[m]:
                    return nums[m]
                else:
                    high = m-1
                    
            elif nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            
            else:
                if nums[m] == nums[m+1]:
                    first = m
                else:
                    first = m-1
                if first % 2 == 0:
                    low = m+1
                else:
                    high = m-1
                