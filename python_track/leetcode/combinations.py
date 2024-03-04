class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(nums, i):
            if len(nums) == k:
                ans.append(nums.copy())
                return

            for i in range(i+1 , n + 1):
                nums.append(i)
                backtrack(nums, i)
                nums.pop()

        backtrack([], 0)
        return ans            
                