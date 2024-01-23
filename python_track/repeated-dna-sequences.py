class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sSet = set()
        l = 0
        r = 10
        ans = set()
        while r < len(s)+1 :
            ss = s[l:r]
            if ss not in sSet:
                sSet.add(ss)
            else:
                ans.add(ss)
            l +=1
            r +=1  

        return list(ans)    
              


