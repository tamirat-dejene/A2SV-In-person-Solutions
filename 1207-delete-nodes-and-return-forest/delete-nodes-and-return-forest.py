# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        store = [(None, root)]
        todel = set(to_delete)
        ans = [root] if root.val not in todel else []


        while store:
            p, c = store.pop()

            if c.val in todel:
                if p and c == p.left:
                    p.left = None
                if p and c == p.right:
                    p.right = None
                
                if c.left and c.left.val not in todel:
                    ans.append(c.left)
                if c.right and c.right.val not in todel:
                    ans.append(c.right)

            if c.left:
                store.append((None if c.val in todel else c, c.left))
            if c.right:
                store.append((None if c.val in todel else c, c.right))
        
        return ans
