# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(start):
            prev, curr = None, start
            while curr:
                keep = curr.next
                curr.next = prev
                prev, curr = curr, keep
            return prev

        # reverse the list
        l1, l2 = rev(l1), rev(l2)

        # sum the up, and return the reversed value
        carry, ans = 0, None

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sm = ListNode((a + b + carry) % 10, ans)
            ans = sm
            
            carry = (a + b + carry) // 10

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry != 0: 
            ans = ListNode(carry, ans)
        
        return ans