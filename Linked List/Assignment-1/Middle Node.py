# link: https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow =  head
        fast  = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
        
"""
Time Complexity = O(N) as we are visiting each node constant number of time
Space Complexity = O(1)
"""