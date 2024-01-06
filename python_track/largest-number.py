class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)

        l= len(nums)
        i = 0
        while i < l-1:
            j = i+1
            while j < l:
                if nums[i] + nums[j] < nums[j] + nums[i] :
                    nums[i], nums[j] = nums[j] , nums[i]
                j+=1
            i += 1

        return str(int("".join(nums)))               
        