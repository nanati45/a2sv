class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {n: i for i, n in enumerate(nums)}
        print(d)
        for i in operations:
            num, repl = i
            index = d[num]
            nums[index] = repl
            d[repl] = index
            del d[num]   
        return nums