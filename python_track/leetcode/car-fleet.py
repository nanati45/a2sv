class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls = list(zip (position , speed ))
        ls.sort()
        stack =[]
        for i in ls:
            t = (target - i[0]) / i[1]
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)

        return len(stack)      
            