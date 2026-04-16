1class Solution:
2    def hasCycle(self, head: Optional[ListNode]) -> bool:
3        slow = fast = head
4        while fast and fast.next:
5            slow = slow.next
6            fast = fast.next.next
7            if slow ==fast:
8                return True
9        return False