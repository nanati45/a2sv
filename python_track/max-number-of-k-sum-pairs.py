class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = len(nums) - 1
        l = 0
        counter = 0
        while l < r:
            if nums[l] + nums[r] == k:
                r -=1
                l +=1
                counter+=1
            elif nums[l] + nums[r] > k :
                r -=1
            else:
                l +=1       
        return counter