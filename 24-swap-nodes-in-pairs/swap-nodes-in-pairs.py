# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head
        prev = None
        cnt = 0

        while curr and curr.next:
            keep = curr.next.next
            curr.next.next = curr

            if prev:
                prev.next = curr.next
            else:
                head = curr.next

            prev = curr
            curr = keep
            prev.next = curr
        
        return head

        



        