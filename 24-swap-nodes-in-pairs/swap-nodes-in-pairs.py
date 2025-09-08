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

        while curr and curr.next:
            keep = curr.next.next
            curr.next.next = curr

            if not prev:
                head = curr.next
            else:
                prev.next = curr.next

            curr.next = keep
            prev = curr
            curr = keep

        return head

        



        