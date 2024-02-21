class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx = max (nums)
        if nums.index(mx) == 0 :
            return mx
        total = nums[0]   
        res = total   
        for i in range(1,len(nums)):
            total += nums[i]
            avg = math.ceil(total / (i + 1))
            res = max(avg , res) 
        return res     
