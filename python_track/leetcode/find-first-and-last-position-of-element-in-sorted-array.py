class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_search (nums , target) :
            left , right = 0 , len(nums) - 1
            idx = -1
            while left <= right :
                mid = left + (right - left ) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target :
                    left = mid + 1    
                else :
                    idx = mid
                    right = mid - 1
            return idx

        def right_search (nums , target) :
            left , right = 0 , len(nums) - 1
            idx = -1
            while left <= right :
                mid = left + (right - left ) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target :
                    left = mid + 1    
                else:
                    idx = mid
                    left = mid + 1
            return idx

        return [left_search(nums, target) , right_search(nums, target)]      

                    