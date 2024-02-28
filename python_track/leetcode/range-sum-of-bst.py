# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if node is None:
                return
            if node.val >= low and node.val <= high:
                ans += node.val
            if not node.val < low:
                dfs(node.left)
            if not node.val > high:
                dfs(node.right)
        dfs(root)
        return ans