class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        counter=1
        mx=0
        i=1
        if len(nums)==0:
            return 0
        while i<len(nums):
            if nums[i]-nums[i-1]==1:
                i+=1
                counter+=1
            elif nums[i]==nums[i-1]:
                i+=1
                continue
            else:
                mx=max(mx,counter)
                counter=1
                i+=1
        return  max(counter,mx)                     

