class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=[]
        max_=0
        for i in nums:
            if i == 1:
                l.append(i)
                max_=max(len(l),max_)
            else:
                max_=max(len(l),max_)  
                l=[]  
        return max(max_,len(l))              