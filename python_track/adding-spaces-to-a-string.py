class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        start=0
        for i in spaces:
            res+=s[start:i]
            res+=" "
            start=i 
        res+=s[start:]    
        return "".join(res)          