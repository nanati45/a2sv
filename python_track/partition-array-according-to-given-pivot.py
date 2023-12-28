from collections import Counter
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        greater=[]
        p=[]
        for i in nums:
            if  i<pivot:
                less.append(i)
            elif i==pivot:
                p.append(i)
            else:
                greater.append(i)
        return less+p+greater                
