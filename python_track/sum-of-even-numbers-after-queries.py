class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]   
        sum_=sum([i for i in nums if i%2==0])

        for [value,index] in queries:
            if nums[index] % 2 == 0:
                sum_ -= nums[index]
            nums[index]+=value    
            if nums[index] % 2 == 0:
                sum_ += nums[index]
            ans.append(sum_)  

        return ans    