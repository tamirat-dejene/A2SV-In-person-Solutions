# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
       
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ""

        queue = deque([root])
        res = [str(root.val)]
        
        while queue:
            p = queue.popleft()
            
            res.append(str(p.left.val) if p.left else '')
            res.append(str(p.right.val) if p.right else '')

            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        
        return ','.join(res)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        data = data.split(',')
        size = len(data)
        
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 0

        while queue:
            l = 2 * i + 1
            r = 2 * i + 2
            
            curr = queue.popleft()
            if not curr: continue

            if l < size and data[l]:
                curr.left = TreeNode(int(data[l]))

            if r < size and data[r]:
                curr.right = TreeNode(int(data[r]))
            
            queue.append(curr.left)
            queue.append(curr.right)
            i += 1
        
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans