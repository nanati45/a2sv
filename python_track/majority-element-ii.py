from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=dict(Counter(nums))
        len_=len(nums)//3
        res=[]
        for i in c:
            if c[i]> len_:
                res.append(i)
        return res        
