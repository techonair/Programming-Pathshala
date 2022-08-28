# link: https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def countLeaves(root):
    # Code here
    if not root:
        return 0
    if root.left == None and root.right == None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)

"""
Time Complexity = O(N) as we are visiting each cell of matrix constant number of time
Space Complexity = O(N) in worst case height of tree can be N as well the call stack 
"""