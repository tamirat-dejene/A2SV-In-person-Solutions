# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = defaultdict(ListNode)
        hp = []
        for i, lst in enumerate(lists):
            if not lst: continue
            heappush(hp, (lst.val, i))
            heads[i] = lst.next
        

        res = ListNode()
        tmp = res

        while hp:
            val, i = heappop(hp)
            tmp.next = ListNode(val)
            tmp = tmp.next

            nxt = heads[i]
            if nxt: 
                heappush(hp, (nxt.val, i))
                heads[i] = nxt.next
            else:
                heads.pop(i)
        
        return res.next
        

            


