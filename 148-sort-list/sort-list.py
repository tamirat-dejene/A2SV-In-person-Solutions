# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def divide(st):
            slow, fast = st, st
            cut = None
            while fast and fast.next:
                cut = slow
                slow = slow.next
                fast = fast.next.next

            cut.next = None
            return slow
        
        def merge(lft, rgt):
            mrgd = ListNode()
            tail = mrgd

            while lft and rgt:
                if lft.val <= rgt.val: 
                    tail.next = lft
                    lft = lft.next
                else: 
                    tail.next = rgt
                    rgt = rgt.next
                tail = tail.next
            
            tail.next = lft if lft else rgt

            return mrgd.next
        
        if not head or not head.next: return head

        lft = head
        rgt = divide(head)

        return merge(self.sortList(lft), self.sortList(rgt))
        

        