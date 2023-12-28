class Solution:
    def checkPossibility(self, nums: List[int]) -> bool: 
        stack = []
        num=0
        count=0
        nums.append(10**5+1)
        while num < len(nums) - 1 :
            if count>1:
                return False
            if len(stack)==0:
                stack.append(nums[num])
            elif stack[-1] <= nums[num] :
                stack.append(nums[num])
            else:
                count+=1 
                if stack[-1]<= nums[num+1]:
                    pass
                else:
                    stack.pop()
                    continue
            num+=1
        return True if count<2 else False                   
