# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = None
        def common(node , p , q):
            nonlocal found
            if not node :
                return False

            if p.val <=  node.val <= q.val :
                found = node
                return True
            elif p.val >= node.val >= q.val :
                found = node
                return True 
            elif node.val >= p.val and node.val >= q.val:
                return common(node.left , p , q)
            elif node.val <= p.val and node.val <= q.val:
                return common(node.right , p , q)   
            
            
        common(root, p , q)
        return  found       





              

                 
