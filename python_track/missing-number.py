class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_=len(nums)
        s=set(nums)
        r=set(range(0,len_+1))
        rr=r-s
        return rr.pop()

        