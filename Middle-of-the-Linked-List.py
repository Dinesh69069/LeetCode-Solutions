1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        slow  = fast  = head
9        while fast and fast.next:
10            slow = slow.next
11            fast = fast.next.next
12        return slow