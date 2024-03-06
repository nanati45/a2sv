class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mn = nums[0]
        while left <= right :
            mid = left + (right - left) // 2
            
            if nums[mid] >= mn:
                left = mid + 1
            elif nums[mid] < mn:
                right = mid - 1
                mn = nums[mid]
            
        return mn            
            

        