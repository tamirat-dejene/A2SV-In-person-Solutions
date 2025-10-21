# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(dict)
        stack = [(root, 0, 0)]

        while stack:
            nd, row, col = stack.pop()
            if not nd: continue
            
            if row not in store[col]:
                store[col][row] = []
            store[col][row].append(nd.val)

            stack.append((nd.left, row + 1, col - 1))
            stack.append((nd.right, row + 1, col + 1))
        
        ans = []
        for col in sorted(store.keys()):
            keep = []
            for row in sorted(store[col].keys()):
                keep.extend(sorted(store[col][row]))
            ans.append(keep)
        return ans
        