1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if head == None :
9            return None
10        current = head
11
12        prev = None
13        while current:
14            next_node = current.next
15            current.next = prev
16            prev = current
17            current = next_node
18        return prev