# link : https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        def serialOrder(x):
            return rank[ord(x) - ord('a')]
        
        rank = [26]*26
        
        for i in range(len(order)):
            rank[ord(order[i]) - ord('a')] = i
        
        
        print(rank)
        arr = [i for i in s]
        
        arr.sort(key= serialOrder)
        
        s = "".join(arr)
        
        return s
        
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        rank = [26]*26
        
        for i in range(len(order)):
            rank[ord(order[i]) - ord('a')] = i
        
        return "".join(sorted(list(s), key= lambda x: rank[ord(x) - ord('a')]))
        
"""