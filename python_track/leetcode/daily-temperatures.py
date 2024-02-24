class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))] 
        stack = []

        for i , temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                p = stack.pop()
                res[p] = i - p
                
            stack.append(i)
        return res    
