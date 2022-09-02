#link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Method 1: Queue + Extra Space for storing level in Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        ans = []
        
        q.append((root, 0))
        ans = []
        current_level = 0
        tmp = []

        while (len(q)):

            (node, level) = q.pop(0)
            
            if level > current_level:
                current_level = level
                ans.append(tmp)
                tmp = []
            tmp.append(node.val)
            
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            
        # when both children are Null/None tmp remains empty so need not append it in ans
        if len(tmp):
            ans.append(tmp)
                    
        return ans

"""
Time Complexity: O(N) We are touching every node twice 
Space Complexity: O(W+N) W-Width of tree, N-storing level number of nodes in queue 
"""

# Method 2: Optimized Approach without extra space
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = []
        ans = []
        
        q.append(root)
        ans = [[root.val]]
        
        while (len(q)):
            size = len(q)
            tmp = []
            while size:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    tmp.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    tmp.append(node.right.val)
                size -= 1
            # when both children are Null/None tmp remains empty so need not append it in ans
            if len(tmp):
                ans.append(tmp)
                    
        return ans

"""
Time Complexity: O(N) We are touching every node twice 
Space Complexity: O(W) W-Width of tree
"""           