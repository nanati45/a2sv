class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        counter = Counter(nums1)
        
        for i in nums2:
            if i in counter :
                counter[i]-=1
                ans.append(i)
            if counter[i] <= 0:
                del counter[i]  

        return ans        
        