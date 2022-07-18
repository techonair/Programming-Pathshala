# link: https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        n = len(nums)-1
        low = 0
        high = n
        #print("first-time", low, high)
        while low <= high:
            
            m = low + (high - low)//2
            #print("in", m, low, high)
            if m == 0:
                if nums[m] > nums[m+1]:
                    break
                else:
                    low = m + 1
                    print(low, high)
            elif m == n:
                if nums[m] > nums[m-1]:
                    break
                else:
                    high = m-1
            else:
                if nums[m-1] < nums[m] > nums[m+1]:
                    break
                elif nums[m+1] < nums[m]:
                    high = m-1
                else:
                    low = m+1
        
        return m