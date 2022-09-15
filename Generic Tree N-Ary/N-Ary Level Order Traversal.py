# link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        q = deque()
        ans = []
        tmp = []
        
        q.append((root, 0))
        curr_level = 0
        
        while len(q):
                 
            (node, level) = q.popleft()
            
            if level != curr_level:
                curr_level = level      
                ans.append(tmp) 
                tmp = []
            
            if node:
                tmp.append(node.val)

                for i in range(len(node.children)):
                    q.append((node.children[i], curr_level+1))
                
        if len(tmp):
            ans.append(tmp)
        
        return ans
        