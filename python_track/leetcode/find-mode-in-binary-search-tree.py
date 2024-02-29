# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def inorder(root):
            if not root:
                return

            freq[root.val] +=1
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        ans = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        mx = ans[0][1]
        res = []
        for i in range(len(ans)):
            if ans[i][1]== mx :
                res.append(ans[i][0])
            else:
                break
        return res

