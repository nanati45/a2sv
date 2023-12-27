from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count=Counter(arr)
        ans=0
        for num,freq in count.items():
            print(freq/len(arr))
            if freq/len(arr)>=0.25:
                ans= num
        return ans        
