class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        c=""
        for i in range(len(s)):
            c+=s[indices.index(i)]
        return c   
