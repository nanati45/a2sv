class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        nums.sort()
        s = list(set(nums))
        s.sort()
        total = 0
        for i in range(len(s)):
            total += c[s[i]]*i
        return total    