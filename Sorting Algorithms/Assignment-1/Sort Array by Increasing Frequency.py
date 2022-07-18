# link: https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                
        
        def freqCheck(num):
            return freq[num]
        
        nums.sort(reverse=True)
        nums.sort(key=freqCheck)
        return nums

        """
        # While sorting we want to give
        # first priority to Frequency
        # Then to value of item
        nums.sort(key=lambda x: (-d[x], x))
        #                         ^     ^  
        #                       (freq, value)
        return nums
        """
        
        