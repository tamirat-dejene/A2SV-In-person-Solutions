# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # sum up
        prev, ans, carry = None, l2, 0

        while l1 and l2:
            sm = l1.val + l2.val + carry
            l2.val = sm % 10
            carry = sm // 10
            
            prev = l2
            if not l1.next and not l2.next and carry != 0:
                l2.next = ListNode(carry)
                carry = 0
            l1, l2 = l1.next, l2.next

        while l1:
            sm = l1.val + carry
            prev.next = ListNode(sm % 10)
            prev = prev.next
            carry = sm // 10
            if not l1.next and carry != 0:
                prev.next = ListNode(carry)
                carry = 0
            l1 = l1.next

        while l2:
            sm = l2.val + carry
            l2.val = sm % 10
            carry = sm // 10
            if not l2.next and carry != 0:
                l2.next = ListNode(carry)
                carry = 0
            l2 = l2.next

        return ans