# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        min_head, max_head = None, None
        temp1, temp2 = None, None
        temp = head

        while temp:
            if temp.val < x:
                if min_head:
                    temp1.next = temp
                    temp1 = temp
                else:
                    min_head, temp1 = temp, temp

                if not temp.next and temp2: temp2.next = None
            else:
                if max_head:
                    temp2.next = temp
                    temp2 = temp
                else:
                    max_head, temp2 = temp, temp
                
                if not temp.next and temp1: temp1.next = None

            temp = temp.next
    

        if temp1: temp1.next = max_head
        else: return max_head

        return min_head

        