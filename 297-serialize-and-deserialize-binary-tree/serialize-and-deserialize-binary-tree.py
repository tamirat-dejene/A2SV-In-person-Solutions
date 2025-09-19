# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))