class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = 0
        end = len(nums) - 1
        mx = 0
        for i in range(end):
            mx = max(mx, i + nums[i])
            if mx <= i :
                return False
        return True        
            
            