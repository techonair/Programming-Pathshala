# link: https://leetcode.com/problems/reverse-linked-list/

""" Method 1: Iterative Way"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head = prev
        return head

"""
Time Complexity = O(N) as we are visiting each node constant number of time
Space Complexity = O(1)
"""

""" Method 2: Recursive Way """

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def revLL(curr):
            if not curr or not curr.next:
                return curr
                
            tmp = curr.next
            curr.next = None
            head = revLL(tmp) 
            tmp.next = curr
            return head
        return revLL(head)

"""
Time Complexity = O(N) as we are visiting each node constant number of time
Space Complexity = O(N) due to recursion call stack
"""