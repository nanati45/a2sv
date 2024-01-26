class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        pref_counter = defaultdict(int)
        pref_counter[0] = 1
        running_sum = 0

        for i in  range(len(nums)):
            running_sum += nums[i]
            diff = running_sum % k
            if diff in pref_counter:
                ans += pref_counter[diff]
            pref_counter[diff] += 1
            
        return ans 