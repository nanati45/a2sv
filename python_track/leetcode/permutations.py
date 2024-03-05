class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(ls, visited):
            if len(nums) == len(ls):
                ans.append(ls.copy())
                return 

            for i in range( len(nums)):
                if nums[i] in visited :
                    continue
                ls.append(nums[i])
                visited.add(nums[i])
                backtrack(ls, visited )
                ls.pop()
                visited.discard(nums[i])
        visited = set()
        backtrack([], visited)
        return  ans