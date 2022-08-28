# link: https://leetcode.com/problems/diameter-of-binary-tree/

# Method 1)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getHt(root, tmp):
            
            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            # because we are calculating edges
            tmp = 1 + max(getHt(root.left, tmp), getHt(root.right, tmp))
            return tmp
        
        def getDia(root):
            
            if not root:
                return 0
            
            # if we were calculating nodes we would add 1+ to getHt(left)+getHt(right)
            return max(
                getHt(root.left, 0) + getHt(root.right, 0), 
                getDia(root.left), getDia(root.right)
            )
            
        return getDia(root)

"""
Time Complexity = 
            getHt() - O(H)
            Total getDia() calls - O(N) 
        Overall Time Complexity = O(N(2*H))
        But in worst case height of tree will be O(N)
        Worst Time Complexity = O(N**2)

Space Complexity = O(N) in worst case height of tree can be N as well the call stack 
"""

# Method 2)

# In each getHt() call we were visiting leaf node, we can improve on this by storing height of each node* in a hashmap{Key=Location : Value=Height} 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        heights = {}
        
        def getHt(root, heights):
            
            if not root:
                heights[root] = 0
                return 0
            
            # because we are calculating edges
            heights[root] = 1 + max(getHt(root.left, heights), getHt(root.right, heights))
            return heights[root]
        
        def getDia(root):
            
            if not root:
                return 0
            
            # if we were calculating nodes we would add 1+ to getHt(left)+getHt(right)
            return max(
                heights[root.left] + heights[root.right], 
                getDia(root.left), getDia(root.right)
            )
            
        getHt(root.left, heights)
        getHt(root.right, heights)
        
        return getDia(root)

"""
Time Complexity = 
            getHt() - O(H)
            Total getDia() calls - O(N) 
        Overall Time Complexity = O(N + H)
        But in worst case height of tree will be O(N)
        Worst Time Complexity = O(N)

Space Complexity = O(2*N) in worst case height of tree can be N as well the call stack 
"""


# Method 3)

# In method 2, we are storing all heights of node but we only wnat the max. height and therefore storing all heights is unnecessary

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getHt(root):
            nonlocal ans
            
            if not root:
                return 0
            
            lh = getHt(root.left)
            rh = getHt(root.right)
            
            ans = max(ans, lh+rh)
            
            return 1+max(lh, rh)
            
        ans = 0
        getHt(root)
        
        return ans

"""
Time Complexity = 
            getHt() - O(2*H)
        Overall Time Complexity = O(H)
        But in worst case height of tree will be O(N)
        Worst Time Complexity = O(N)

Space Complexity = O(N) in worst case height of tree can be N as well the call stack 
"""

# Method 4) 

# In previous method, we returned heights only in getHt() but I can simply return Diameter and Height combined.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Method 4: T.C. = O(N), S.P.: O(H)
        
        def getDH(root):
            nonlocal ans
            
            if not root:
                return [0,0]
            
            lh = getDH(root.left)
            rh = getDH(root.right)
            
            h = 1+max(lh[0], rh[0])
            d = max(lh[0]+rh[0], lh[1], rh[1])
            
            return [h, d]
        
        ans = getDH(root)
        
        return ans[1]

"""
Time Complexity = 
            getHt() - O(2*H)
        Overall Time Complexity = O(H)
        But in worst case height of tree will be O(N)
        Worst Time Complexity = O(N)

Space Complexity = O(N) in worst case height of tree can be N as well the call stack 
"""     