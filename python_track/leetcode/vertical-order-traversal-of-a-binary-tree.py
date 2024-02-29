# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = []
        def traverse(node , row , col):
            if not node: 
                return
            ls.append((col , row , node.val))
            traverse(node.left , row + 1 , col-1 )
            traverse(node.right , row + 1 , col+1 ) 

        traverse(root , 0 , 0)
        ls.sort()
        d = defaultdict(list)
        ans = []
        for i in range(len(ls)):
            d[ls[i][0]].append(ls[i][2])

        for i in d.values():
            ans.append(i)
        return ans
