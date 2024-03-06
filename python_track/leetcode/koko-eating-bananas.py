class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        best = max(piles)
        while left <= right :
            mid = left + (right - left ) // 2

            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i] / mid)

            if hours > h:
                left = mid + 1
            else:
                right = mid - 1        
        return left        