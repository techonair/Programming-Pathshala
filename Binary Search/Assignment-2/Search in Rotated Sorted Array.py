# link:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        # pivot index finding
        
        # [PART2 with pivot, PART1]
        
        def pivotIndex(nums):
            low = 0
            high = n-1
            while low <= high:
                m = (low + high)//2
                if nums[m] <= nums[n-1]:
                    high = m-1
                else:
                    if nums[m] > nums[m+1]:
                        return m
                    else:
                        low = m+1
                    
            return high
        
        pivot = pivotIndex(nums)
            
        def binarySearch(start, end):
            while start <= end:
                m = (start+end)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    end = m-1
                elif nums[m] < target:
                    start = m+1
            return -1
        
        # if (if (edge case: number of rotation in array == 0) else (search part 1)) 
        # else (search part 2)
        if target <= nums[n-1]:
            if pivot == -1:
                ans = binarySearch(0, n-1)
            else:
                ans = binarySearch(pivot+1, n-1)
        else:
            ans = binarySearch(0, pivot)
            
        return ans
       