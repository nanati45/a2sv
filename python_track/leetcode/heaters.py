class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        def binary_search(pos):
            l = 0
            r = len(heaters) - 1
            ans = 10 ** 9
            while l <= r :
                mid = l + (r - l) // 2
                diff = pos - heaters[mid]
                if diff == 0:
                    return 0
                elif diff < 0 :
                    ans = min(ans , abs(diff))
                    r = mid - 1
                else:
                    ans = min(ans , diff)
                    l = mid + 1
            return ans

        for i in range(len(houses)) :
            res = max( res, binary_search(houses[i]))
        return res    



