class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def ways(left , right ):
            if left == right :
                return nums[right]

            left_side = nums[left] - ways(left+1 , right)
            right_side = nums[right] - ways(left , right - 1)
            return max(left_side, right_side)

        return ways(0 , len(nums)-1) >= 0       