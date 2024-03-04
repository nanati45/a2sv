class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn = float('inf')
        if len(cookies) == k :
            return max(cookies)
        def backtrack(bucket , idx):
            nonlocal mn
            if len(cookies) == idx:
                mn = min(mn , max(bucket))
                return
            for i in range(k):
                bucket[i] += cookies[idx] 
                backtrack(bucket , idx + 1)
                bucket[i] -= cookies[idx]
        backtrack([0]*k , 0)
        return mn