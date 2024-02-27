class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mn = float('inf')
        for i in range(len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack :
                if nums[i] > stack[-1][1]:
                    return True
            stack.append((nums[i],mn ))    
            mn = min(nums[i], mn) 
            
        return False