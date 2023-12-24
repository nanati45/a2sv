class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        max_=max(candies)
        for i in candies:
            if i+extraCandies>=max_:
                ans.append(True)
            else:
                ans.append(False)
        return ans            
        