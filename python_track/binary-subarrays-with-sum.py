class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0
        sums = {}  # A dictionary to store the frequency of each sum

        curr_sum = 0
        for num in nums:
            curr_sum += num

            if curr_sum == goal:
                count += 1

            if curr_sum - goal in sums:
                count += sums[curr_sum - goal]

            if curr_sum in sums:
                sums[curr_sum] += 1
            else:
                sums[curr_sum] = 1

        return count  

