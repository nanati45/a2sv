class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=set(nums1)
        n2=set(nums2)
        
        common = n1.intersection(n2)
        return min(common) if common else -1