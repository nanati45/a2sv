class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        mx = 0
        k = 1

        for i, num in enumerate(nums):
            k -= (1-num)
            while k < 0:
                k +=(1-nums[l])
                l +=1
            mx = max(mx, i-l)

        return mx  

