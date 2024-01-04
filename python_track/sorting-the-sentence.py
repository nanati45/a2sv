class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        ans=[0]*len(s)
        de={int(i[-1]):i[:-1]  for i in s}
        for i in de:
            ans[i-1]=de[i]

        return " ".join(ans)

