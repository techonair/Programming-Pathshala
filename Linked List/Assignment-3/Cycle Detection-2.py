# link: https://leetcode.com/problems/linked-list-cycle-ii/

# Method 0: Using Hashmap, space complexity= O(N)

# Method 1: 
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def hasCycle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return False
        
        slow = hasCycle(head)
        if slow:
            p = head
            while True:
                tmp = slow
                while tmp!=p:
                    tmp = tmp.next
                    if tmp == slow:
                        break
                if tmp == p:
                    return tmp
                p = p.next
                
        return None

# Method 2:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def hasCycle(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return slow
            return False
        
        slow = hasCycle(head)
        
        if slow:
            p = head
            while p != slow:
                p = p.next
                slow = slow.next
        else:
            return None
        return p

"""
Time Complexity = O(N**2) as we are looping L1(N-L2) times and L1 can be N/2 in worst
Space Complexity = O(1)
"""