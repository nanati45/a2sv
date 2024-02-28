# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, val):
            if not node:
                ins = TreeNode(val)
                return ins

            if node.val > val :
                if node.left:
                    search(node.left, val)
                else:
                    ins = TreeNode(val)
                    node.left = ins

            else  :
                if node.right:
                    search( node.right, val)
                else:
                    ins = TreeNode(val)
                    node.right = ins

            return node        
        return search(root, val) 
                    
