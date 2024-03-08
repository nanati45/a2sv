class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def checker(num):
            ans = 0
            for i in range(len(nums)) :
                ans += ceil(nums[i] / num)
            return ans

        l = 1
        nums.sort()
        r = nums[-1] 
        
        while l <= r :
            mid = l + (r - l) // 2
            if checker(mid) <= threshold :
                r = mid - 1
            else:
                l = mid + 1
        return l              




                    