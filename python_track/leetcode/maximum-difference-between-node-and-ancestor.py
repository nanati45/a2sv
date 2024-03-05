# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def traverse(node):
            mn = float('inf')
            mx = float('-inf')
            nonlocal max_diff
            l = r = (float('inf'), float('-inf'))
            if not node.left and not node.right :
                return (node.val, node.val)
            if node.left:
                l = traverse(node.left)
            if node.right:
                r = traverse(node.right)
            mn = min(node.val ,l[0], r[0])
            mx = max(node.val , l[1], r[1])
            max_diff = max(abs(node.val - mn),abs(mx - node.val), max_diff)
            return (mn , mx) 
        traverse(root)
        return max_diff 
              


