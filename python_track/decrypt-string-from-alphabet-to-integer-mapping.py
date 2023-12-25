class Solution:
    def freqAlphabets(self, s: str) -> str:
        l=[]
        r=0
        while r<len(s):
            if r+2 < len(s) and s[r+2]!="#":
                l.append(int(s[r]))
                r+=1

            elif(r+2 == len(s)):
                l.append(int(s[r]))
                l.append(int(s[r+1]))
                break

            else:
                l.append(int(s[r:r+2]))
                r+=3   
        print(l)
        res=""
        for i in l:
            res+=chr(96+i)
        return res            
