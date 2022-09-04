# link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Method 1: Using DFS (recursion) + Sorting 

class Solution:
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Part 1: storing all nodes of tree in this form -> 
        # (node.val, level, horizontal distance) as shown in tree diagrams in example
        
        tmp = []
        
        def dfs(root, level, hd):
            
            if not root:
                return
            
            tmp.append([root.val, level, hd])
            dfs(root.left, level+1, hd-1)
            dfs(root.right, level+1, hd+1)
            
        dfs(root, 0, 0)
        #print(tmp)
        
        # Part 2: Custom Sorting, Lambda
        # Rule 1: Horizontal Distance of node (ascending order)
        # Rule 2: Node level (ascending order)
        # If conflict:
            # Rule 3: Node Value (ascending order) 
        
        tmp = sorted(tmp, key = lambda x: (x[2], x[1], x[0]))
        #print(tmp)
        
        
        # Part 3: Desing Format of ans
        
        ans = [ [ tmp[0][0] ] ]

        for i in range(1, len(tmp)):
            # if horizontal distance of nodes is equal then without worry append at ans[-1] as we already solved conflict by sorting array based on node val 
            if tmp[i][2] == tmp[i-1][2]:
                ans[-1].append(tmp[i][0])
                
            else:
                ans.append( [tmp[i][0]] )
                
        return ans
        
"""
Time Complexity:
    Traversal: O(N)
    Sorting: O(NlogN)
    Formating: O(N)

    Total Time Complexity: O(NlogN + 2N)

Space Complexity: 
    (ans + tmp) array: O(2N)
    dfs recursion stack: O(H), H=Height of the tree

    Total Space Complexity: O(H+2N)
"""

# Method 2: Forget everything about Method 1, because we don't want Sorting (NlogN)

# Version 1: No lambda function used

from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        hashmap = {}
        
        q.append( [root, 0, 0] )
        
        minHD = float('inf')
        maxHD = float('-inf')
        
        while len(q):
            
            (node, hd, level) = q.popleft()
            
            maxHD = max(maxHD, hd)
            minHD = min(minHD, hd)
            
            if hd not in hashmap:
                hashmap[hd] = [ (level, node.val) ]
            else:
                hashmap[hd].append( (level, node.val) )
            
            if node.left:
                q.append([node.left, hd-1, level+1])
            if node.right:
                q.append([node.right, hd+1, level+1])
            
        ans = []
        for key in range(minHD, maxHD+1):
            tmp = []
            for value in sorted(hashmap[key]):
                tmp.append(value[1])
            ans.append(tmp)
            
        return ans

# Version 2: Lambda Function used
class Solution:
    
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        hashmap = {}
        
        q.append( [root, 0, 0] )
        
        minHD = float('inf')
        maxHD = float('-inf')
        
        while len(q):
            
            (node, hd, level) = q.popleft()
            
            maxHD = max(maxHD, hd)
            minHD = min(minHD, hd)
            
            if hd not in hashmap:
                hashmap[hd] = [ (node.val, level) ]
            else:
                hashmap[hd].append( (node.val, level) )
            
            if node.left:
                q.append([node.left, hd-1, level+1])
            if node.right:
                q.append([node.right, hd+1, level+1])
            
        ans = []
        for key in range(minHD, maxHD+1):
            tmp = []
            for value in sorted(hashmap[key], key=lambda x: (x[1], x[0])):
                tmp.append(value[0])
            ans.append(tmp)
            
        return ans

"""
Time Complexity: O(N), considering there is no skewed tree case
Space Complexity: O(N) W-Width of tree
"""  