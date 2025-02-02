# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]

        cell, l, r, t, b = [0, 0], 0, n - 1, 0, m - 1
        lr, tb, rl, bt = True, False, False, False

        while head:
            i, j = cell
            ans[i][j] = head.val
            
            if lr:
                if j + 1 < r: j += 1
                elif j + 1 == r: lr, tb, j, t = False, True, j + 1, t + 1
                else: i += 1
            elif tb:
                if i + 1 < b: i += 1
                elif i + 1 == b: tb, rl, i, r = False, True, i + 1, r - 1
            
            elif rl:
                if j - 1 > l: j -= 1
                elif j - 1 == l: rl, bt, j, b = False, True, j - 1, b - 1
            
            elif bt:
                if i - 1 > t: i -= 1
                elif i - 1 == t: bt, lr, i, l = False, True, i - 1, l + 1
            
            cell = [i, j]
            head = head.next

        return ans



        