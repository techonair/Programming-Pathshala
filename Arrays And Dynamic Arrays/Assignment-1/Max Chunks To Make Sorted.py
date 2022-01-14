# Problem: https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        count_max = -10**9

        count = 0

        for i in range(len(arr)):
            count_max = max(count_max, arr[i])
            if count_max == i:
                count += 1

        return count