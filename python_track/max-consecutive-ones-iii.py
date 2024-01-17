class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        mx = 0

        for i, num in enumerate(nums):
            k -= (1-num)
            while k < 0:
                k +=(1-nums[l])
                l +=1
            mx = max(mx, i-l+1)

        return mx
