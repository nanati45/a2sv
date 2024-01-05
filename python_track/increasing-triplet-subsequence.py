class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i,j=float("inf"),float("inf")
        for n in range(len(nums)):
            if nums[n] <= i:
                i=nums[n]
            elif nums[n] <= j:
                j = nums[n]
            else:
                return True
        return False                
            
