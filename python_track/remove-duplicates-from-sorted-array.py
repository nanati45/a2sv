class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        ss=len(s) 
        l=0
        i=1
        if ss==len(nums):
            return ss
        while l<ss:
            if nums[i]==nums[l]:
                nums.append("_") 
                nums.pop(i)
            else:
                l+=1
                i+=1       
        return len(s)     