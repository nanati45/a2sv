class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {n: i for i, n in enumerate(nums)}
        print(d)
        for [num, op] in operations:
            index = d[num]
            nums[index] = op
            d[op] = index
            del d[num]   
        return nums