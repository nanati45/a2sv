class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        def gcd(mn , mx):
            if mx == 0 :
                return mn
            return gcd(mx , mn%mx) 
        return(gcd(mn , mx))        
