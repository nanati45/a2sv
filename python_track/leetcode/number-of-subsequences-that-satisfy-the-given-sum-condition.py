class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def finder (num) :
            l = 0 
            r = len(nums) - 1
            while l <= r :
                mid = l + (r - l) // 2
                if nums[mid] > num:
                    r = mid - 1
                else:
                    l = mid + 1
            return r
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] * 2 <= target :
                idx = finder(target - nums[i])
                if idx != len(nums):
                    ans += 2 **(idx - i)
                else:
                    ans += 2 **(idx - i - 1)
            else:
                break           
        return ans %  (10**9 + 7 )          

