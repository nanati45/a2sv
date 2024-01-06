class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        s = sorted(piles,reverse=True)
        n = len(piles)//3
        ans= 0

        for i in range(1,n*2,2):
            ans += s[i]
           
        return ans      