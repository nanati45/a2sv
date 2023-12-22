from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_=defaultdict(int)
        sum_=0
        for i in nums:
            dict_[i]+=1
            sum_+=dict_[i]-1
        return sum_   

