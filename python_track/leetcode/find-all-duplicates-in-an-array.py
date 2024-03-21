class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = Counter(nums)
        ans = []
        for i in dup :
            if dup[i] == 2:
                ans.append(i)
        return ans        

