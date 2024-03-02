# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sequence(node , nums):
            if not node :
                return 0

            nums = nums * 10 + node.val     
            if not node.left and not node.right :
                return nums

            l = sequence(node.left , nums)  
            r = sequence(node.right , nums) 
            return l + r

        
        return sequence(root , 0)                           
