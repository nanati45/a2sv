class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r :
            mid = l + (r - l) // 2
            if mid*mid == x or (mid*mid < x and (mid+1)*(mid+1)>x):
                return mid
            elif mid * mid < x :
                l = mid + 1 
            else:
                r = mid - 1

