# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # using while loop
        parent, curr = None, root

        while curr:
            if key == curr.val:
                # Case 1: Leaf node
                if not curr.left and not curr.right:
                    if not parent: # deleting the root node
                        return None
                    else:
                        if key < parent.val:
                            parent.left = None
                        else:
                            parent.right = None
                # Case 2: If the current node has one child
                elif not curr.left or not curr.right:
                    if not parent:
                        root = curr.left if curr.left else curr.right
                    else:
                        if key < parent.val:
                            parent.left = curr.left if curr.left else curr.right
                        else:
                            parent.right = curr.left if curr.left else curr.right
                # Case 3: Current node with two children
                else:
                    # Find the inorder sucessor
                    sp  = curr
                    sc = curr.right
                    while sc and sc.left: 
                        sp = sc
                        sc = sc.left
                    
                    # remove the inderoder succesor
                    if sc.val < sp.val: sp.left = sc.right
                    else: sp.right = sc.right
                    
                    # replace the curr with inorder sucessor value
                    curr.val = sc.val

                break
            elif key < curr.val:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        
        return root