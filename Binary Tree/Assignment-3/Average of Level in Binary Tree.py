# link: https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        ans = []
        
        q = deque()
        q.append(root)
        
        while len(q):
            size = len(q)
            sum_of_level = 0
            num_of_elements = 0
            
            while size:
                
                node = q.popleft()
                sum_of_level += node.val
                num_of_elements += 1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                size -= 1
            
            ans.append(round(sum_of_level / num_of_elements, 5))
                
        return ans
        
        
"""
Time Complexity: O(N) We are touching every node twice 
Space Complexity: O(W) W-Width of tree
"""