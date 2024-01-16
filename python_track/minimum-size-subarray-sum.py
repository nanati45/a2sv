class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        min_length = n + 1
        left = 0
        current_sum = 0
        for right in range(1, n + 1):
            current_sum = prefix_sum[right] - prefix_sum[left]
            while current_sum >= target:
                min_length = min(min_length, right - left)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != n + 1 else 0