class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_=[0]*len(nums)
        new_[0]=nums[0]
        for i in range(1,len(new_)):
            new_[i]=new_[i-1] + nums[i]
        return  (new_)