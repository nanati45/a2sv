class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Getting the product of prefixes
        pref = []
        pref.append(nums[0])
        for i in range(1,len(nums)):
            pref.append(pref[i-1] * nums[i])

        # Getting the product of the suffixes and reversing it 
        suffix = [] 
        suffix.append(nums[-1])
        n = nums[::-1]
        for i in range(1,len(nums)):
            suffix.append(suffix[i-1] * n[i])
        suffix.reverse()  

        # Iterating over the nums and getting the product of the left and the right side
        ans = []
        for i in range(len(nums)):
            if i - 1 < 0:
                ans.append(suffix[i + 1])
            elif i + 1 > len(nums) - 1:
                ans.append(pref[i - 1])
            else:
                ans.append(pref[i-1] * suffix[i + 1]) 

        return ans       
