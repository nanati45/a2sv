class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)- 2, -1 , -1):
            if nums[i] < nums[i+1]:
                continue
            split_into = ceil(nums[i] / nums[i+1] )
            prev = nums[i] // split_into
            ans += split_into - 1
            nums[i] = prev

        return ans        