
class TreeNode:
    def __init__(self, val = 0, left= None, right = None):
        self.val = val
        self.right = right
        self.left = left

result = 0
def check(root : TreeNode):
    
    if not root:
        return 0, 0
    left_sum, left_count = check(root.left)
    right_sum, right_count = check(root.right)

    s = root.val + left_sum + right_sum
    c = 1 + left_count + right_count

    if s //c == root.val:
        result += 1
    return s, c

root = input(list)
print(check(root, result))
