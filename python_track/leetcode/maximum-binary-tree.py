# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def find_max(ls):
            mx = 0
            for i in range(len(ls)):
                if ls[mx] < ls[i] :
                    mx = i
            return mx        
        def recur(lis):
            if not lis :
                return
            idx = find_max(lis)
            left = lis[: idx]
            right = lis[idx + 1 :]
            l = recur(left)
            r = recur(right)
            node = TreeNode(lis[idx] , l , r )
            return node
        return recur(nums)    
            
