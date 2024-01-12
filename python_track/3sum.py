class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums) -1
            target = 0-(nums[i])
            while l < r:
                if nums[l] + nums[r]  == target:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])  
                    l +=1
                    r -=1    
                elif nums[l] + nums[r] < target :
                    l +=1
                else:
                    r -=1

        return ans 
        
        