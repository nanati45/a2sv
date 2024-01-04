class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans=0
        s=list(zip(*strs))
        for i in s:
            if list(i)!=sorted(list(i)):
                ans+=1
        return ans