# link: https://leetcode.com/problems/linked-list-cycle/

# Method 1: Using Hashmap

# Method 2:

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

"""
Time Complexity = O(N)
Space Complexity = O(1)
"""