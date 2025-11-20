# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         store, rsum, tmp = {0: None}, 0, head

#         while tmp:
#             rsum += tmp.val
#             if rsum in  store:
#                 if rsum and store[rsum]:
#                     print(store[rsum].val, rsum)
#                     store[rsum].next = tmp.next
#                 else:
#                     head = tmp.next
#             else:
#                 store[rsum] = tmp
#             tmp = tmp.next
            
#         return None if rsum == 0 else head
        

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prefix_sum = 0
        seen = {0: dummy}
        
        # First pass: build prefix sums
        node = dummy
        while node:
            prefix_sum += node.val
            seen[prefix_sum] = node
            node = node.next
        
        # Second pass: remove zero-sum sublists
        prefix_sum = 0
        node = dummy
        while node:
            prefix_sum += node.val
            # Jump to the last occurrence of this prefix sum
            node.next = seen[prefix_sum].next
            node = node.next
        
        return dummy.next
