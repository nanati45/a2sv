class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while (l<r):
            _sum=numbers[l] + numbers[r]
            if _sum==target:
                ans=[l+1,r+1]
                return ans
            elif(_sum<=target):
                l+=1
            else:
                r-=1
        return []