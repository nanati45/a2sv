class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st=list(map(str,digits))
        s=''.join(st)
        num=int(s)+1
        ans=list(str(num))
        ans=list(map(int,ans))
        return ans