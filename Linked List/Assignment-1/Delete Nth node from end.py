# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        if slow.next:
            slow.next = slow.next.next
        
        return head

"""
Time Complexity = O(N) as we are visiting each node constant number of time
Space Complexity = O(1) in worst case recursion can store all nodes
"""